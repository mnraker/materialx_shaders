// Copyright 2024 DreamWorks Animation LLC
// SPDX-License-Identifier: Apache-2.0

/// @file ND_image_vector3.cc

#include "attributes.cc"
#include "ND_image_vector3_ispc_stubs.h"

#include <moonray/common/mcrt_macros/moonray_static_check.h>
#include <moonray/rendering/shading/BasicTexture.h>
#include <moonray/rendering/shading/MapApi.h>

#include <memory>

using namespace scene_rdl2::math;
using namespace scene_rdl2::rdl2;

RDL2_DSO_CLASS_BEGIN(ND_image_vector3, Map)
public:
    ND_image_vector3(SceneClass const &sceneClass, std::string const &name);
    void update();

private:
    static void sample(const Map *self, moonray::shading::TLState *tls,
                       const moonray::shading::State &state, Color *sample);
    ispc::ND_image_vector3 mIspc;
    
    std::unique_ptr<moonray::shading::BasicTexture> mTexture;

RDL2_DSO_CLASS_END(ND_image_vector3)

ND_image_vector3::ND_image_vector3(const SceneClass& sceneClass,
        const std::string& name) :
    Parent(sceneClass, name)
{
    mSampleFunc = ND_image_vector3::sample;
    mSampleFuncv = (SampleFuncv) ispc::ND_image_vector3_getSampleFunc();

    mTexture = std::make_unique<moonray::shading::BasicTexture>(this, sLogEventRegistry);
}

void
ND_image_vector3::update()
{
    mIspc.mDisableMode = (get(disableAttr) || (getenv("DISABLE_MATERIALX_STUBS") != nullptr));
    mIspc.mTexCoordUseDefault = (!getBinding(texcoordAttr) && isDefault(texcoordAttr));
    
    // NYI
    String framerangeValue;
    framerangeValue = get(framerangeAttr);
    // NYI
    Int frameoffsetValue;
    frameoffsetValue = get(frameoffsetAttr);
    // NYI
    Int frameendactionValue;
    frameendactionValue = get(frameendactionAttr);

    const scene_rdl2::rdl2::SceneVariables &sv = getSceneClass().getSceneContext()->getSceneVariables();
    mIspc.mFatalColor = asIspc(sv.get(scene_rdl2::rdl2::SceneVariables::sFatalColor));
    auto dflt = get(defaultAttr);
    mIspc.mDefaultColor = asIspc(Color(dflt[0], dflt[1], dflt[2]));

    mIspc.mUAddressMode = (ispc::AddressModeType) get(uaddressmodeAttr);
    mIspc.mVAddressMode = (ispc::AddressModeType) get(vaddressmodeAttr);
    moonray::shading::WrapType wrapS, wrapT;
    if (mIspc.mUAddressMode == ispc::PERIODIC ||
        mIspc.mUAddressMode == ispc::MIRROR) {
        wrapS = moonray::shading::WrapType::Periodic;
    } else {
        wrapS = moonray::shading::WrapType::Clamp;
    }
    if (mIspc.mVAddressMode == ispc::PERIODIC ||
        mIspc.mVAddressMode == ispc::MIRROR) {
        wrapT = moonray::shading::WrapType::Periodic;
    } else {
        wrapT = moonray::shading::WrapType::Clamp;
    }

    // Update BasicTexture and make sure it is valid
    if (hasChanged(fileAttr)) {
        std::string errorStr;
        if (!mTexture->update(get(fileAttr),
                              static_cast<ispc::TEXTURE_GammaMode>(0), // gamma off
                              wrapS,      // wrapS
                              wrapT,      // wrapT
                              true,                      // use default color
                              asCpp(mIspc.mDefaultColor), // default color 
                              asCpp(mIspc.mFatalColor),
                              errorStr)) {
            fatal(errorStr);
            mTexture = nullptr;
            mIspc.mTexture = nullptr;
            return;
        }
        mIspc.mTexture = &mTexture->getBasicTextureData();
    }

}

void
ND_image_vector3::sample(const Map* self, moonray::shading::TLState *tls,
                 const moonray::shading::State& state, Color* sample)
{
    const ND_image_vector3* me = static_cast<const ND_image_vector3*>(self);

    if (me->mIspc.mDisableMode) {
        *sample = Color(0.f, 0.f, 0.f);
        return;
    }

    if (me->mTexture == nullptr) {
        *sample = asCpp(me->mIspc.mFatalColor);
        return;
    }

    Vec2f texcoordValue;
    if (me->mIspc.mTexCoordUseDefault) {
        texcoordValue = state.getSt();
        // OIIO texture flip
        texcoordValue[1] = 1.f - texcoordValue[1];
    } else {
        texcoordValue = evalVec2f(me, texcoordAttr, tls, state);
    }

    Color outValue;
    float derivatives[4];

    switch(me->mIspc.mUAddressMode) {
    case(ispc::MIRROR):
        if (texcoordValue[0] < 0.f) {
            texcoordValue[0] = -texcoordValue[0];
            derivatives[0] = -state.getdSdx();
            derivatives[2] = -state.getdSdy();
        } else {
            derivatives[0] = state.getdSdx();
            derivatives[2] = state.getdSdy();
        }
        break;
    default:
        derivatives[0] = state.getdSdx();
        derivatives[2] = state.getdSdy();
        break;
    }

    switch(me->mIspc.mVAddressMode) {
    case(ispc::MIRROR):
        if (texcoordValue[1] < 0.f) {
            texcoordValue[1] = -texcoordValue[1];
            derivatives[1] = state.getdTdx();
            derivatives[3] = state.getdTdy();
        } else {
            derivatives[1] = -state.getdTdx();
            derivatives[3] = -state.getdTdy();
        }
        break;
    default:
        derivatives[1] = -state.getdTdx();
        derivatives[3] = -state.getdTdy();
        break;
    }

    const Vec2f st = texcoordValue;

    const Color4 tx = me->mTexture->sample(tls, state, st, derivatives);
    outValue = Color(tx[0], tx[1], tx[2]);
    
    *sample = Color(outValue);
}

