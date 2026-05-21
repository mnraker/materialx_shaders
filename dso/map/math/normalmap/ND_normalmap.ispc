// Copyright 2024 DreamWorks Animation LLC
// SPDX-License-Identifier: Apache-2.0

/// @file "ND_normalmap.ispc"

#include "attributes.isph"

#include <moonray/rendering/shading/ispc/MapApi.isph>

struct ND_normalmap {
    uniform bool mDisableMode;
    uniform bool mNormalUseDefault;
    uniform bool mTangentUseDefault;
    const uniform Xform * uniform mXform;
};
ISPC_UTIL_EXPORT_UNIFORM_STRUCT_TO_HEADER(ND_normalmap);

static Color
sample(const uniform Map *            uniform  map,
             uniform ShadingTLState * uniform  tls,
       const varying State &                   state)
{
    const uniform ND_normalmap* uniform me = MAP_GET_ISPC_CPTR(ND_normalmap, map);

    varying Vec3f inValue;
    inValue = evalInAttr(map, tls, state);

    if (me->mDisableMode) {
        const varying Color outValue = Color_ctor(inValue.x, inValue.y, inValue.z);
        return outValue;
    }

    uniform int spaceValue;
    spaceValue = getSpaceAttr(map);

    varying float scaleValue;
    scaleValue = evalScaleAttr(map, tls, state);

    varying Vec3f N;
    if (me->mNormalUseDefault) {
        N = getN(state);
    } else {
        N = evalNormalAttr(map, tls, state);
    }

    varying Vec3f T;
    if (me->mTangentUseDefault) {
        T = getdPds(state);
    } else {
        T = evalTangentAttr(map, tls, state);
    }

    varying Vec3f outValue;
    if (spaceValue == 0) { // tangent --> render

        ReferenceFrame frame;
        ReferenceFrame_init(frame, normalize(N), normalize(T));
        inValue = normalize(2.0f * inValue - Vec3f_ctor(1.0f, 1.0f, 1.0f));
        outValue = localToGlobal(frame, inValue);

    } else { // object --> render
        outValue = transformNormal(me->mXform,
                                  SHADING_SPACE_OBJECT,
                                  SHADING_SPACE_RENDER,
                                  state,
                                  inValue);
    }

    outValue = normalize(lerp(getN(state), outValue, scaleValue));

    return Color_ctor(outValue.x, outValue.y, outValue.z);
}

DEFINE_MAP_SHADER(ND_normalmap, sample)
