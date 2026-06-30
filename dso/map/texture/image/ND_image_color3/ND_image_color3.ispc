// SPDX-License-Identifier: Apache-2.0
// Copyright Contributors to the Moonray Project

/// @file "ND_image_color3.ispc"

#include "attributes.isph"

#include <moonray/rendering/shading/ispc/BasicTexture.isph>
#include <moonray/rendering/shading/ispc/Shading.isph>
#include <moonray/rendering/shading/ispc/MapApi.isph>


enum AddressModeType {
    CONSTANT = 0,
    CLAMP = 1,
    PERIODIC = 2,
    MIRROR = 3,
};
ISPC_UTIL_EXPORT_ENUM_TO_HEADER(AddressModeType);

struct ND_image_color3
{
    const uniform BASIC_TEXTURE_Data * uniform mTexture;
    uniform bool mDisableMode;
    uniform bool mTexCoordUseDefault;
    uniform Color mDefaultColor;
    uniform Color mFatalColor;
    uniform AddressModeType mUAddressMode;
    uniform AddressModeType mVAddressMode;
};
ISPC_UTIL_EXPORT_UNIFORM_STRUCT_TO_HEADER(ND_image_color3);

static Color
sample(const uniform Map *            uniform  map,
             uniform ShadingTLState * uniform  tls,
       const varying State &                   state)
{
    const uniform ND_image_color3* uniform me = MAP_GET_ISPC_CPTR(ND_image_color3, map);

    if (me->mDisableMode) {
        return Color_ctor(0.0f, 0.0f, 0.0f);
    }

    if (!me->mTexture) {
        return me->mFatalColor;
    }

    varying Vec2f texcoordValue;
    if (me->mTexCoordUseDefault) {
        texcoordValue = getSt(state);
        // OIIO texture flip
        texcoordValue.y = 1.f - texcoordValue.y;
    } else {
        texcoordValue = evalTexcoordAttr(map, tls, state);
    }
    

    varying float derivatives[4] = {0.f, 0.f, 0.f, 0.f};

    switch(me->mUAddressMode) {
    case(MIRROR):
        if (texcoordValue.x < 0.f) {
            texcoordValue.x = -texcoordValue.x;
            derivatives[0] = -getdSdx(state);
            derivatives[2] = -getdSdy(state);
        } else {
            derivatives[0] = getdSdx(state);
            derivatives[2] = getdSdy(state);
        }
        break;
    default:
        derivatives[0] = getdSdx(state);
        derivatives[2] = getdSdy(state);
        break;
    }

    switch(me->mVAddressMode) {
    case(MIRROR):
        if (texcoordValue.y < 0.f) {
            texcoordValue.y = -texcoordValue.y;
            derivatives[1] = getdTdx(state);
            derivatives[3] = getdTdy(state);
        } else {
            derivatives[1] = -getdTdx(state);
            derivatives[3] = -getdTdy(state);
        }
        break;
    default:
        derivatives[1] = -getdTdx(state);
        derivatives[3] = -getdTdy(state);
        break;
    }

    const varying Vec2f st = texcoordValue;
    varying Col4f tx = BASIC_TEXTURE_sample(me->mTexture,
                                            tls,
                                            state,
                                            st,
                                            derivatives);

    Color outValue = Color_ctor(tx.r, tx.g, tx.b);
    return outValue;
}

DEFINE_MAP_SHADER(ND_image_color3, sample)

