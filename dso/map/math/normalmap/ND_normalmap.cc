// Copyright 2024 DreamWorks Animation LLC
// SPDX-License-Identifier: Apache-2.0

/// @file ND_normalmap.cc

#include "attributes.cc"
#include "ND_normalmap_ispc_stubs.h"

#include <moonray/rendering/shading/MapApi.h>

using namespace scene_rdl2::math;
using namespace scene_rdl2::rdl2;

RDL2_DSO_CLASS_BEGIN(ND_normalmap, Map)
public:
    ND_normalmap(SceneClass const &sceneClass, std::string const &name);
    void update() override;

private:
    static void sample(const Map *self, moonray::shading::TLState *tls,
                       const moonray::shading::State &state, Color *sample);

    ispc::ND_normalmap mIspc;

    // needed for object space transformations
    std::unique_ptr<moonray::shading::Xform> mXform;

RDL2_DSO_CLASS_END(ND_normalmap)

ND_normalmap::ND_normalmap(const SceneClass& sceneClass,
        const std::string& name) :
    Parent(sceneClass, name)
{
    mSampleFunc = ND_normalmap::sample;
    mSampleFuncv = (SampleFuncv) ispc::ND_normalmap_getSampleFunc();
}

void
ND_normalmap::update()
{
    mIspc.mDisableMode = (get(disableAttr) || (getenv("DISABLE_MATERIALX_STUBS") != nullptr));
    mIspc.mNormalUseDefault = (!getBinding(normalAttr) && isDefault(normalAttr));
    mIspc.mTangentUseDefault = (!getBinding(tangentAttr) && isDefault(tangentAttr));

    mXform = std::make_unique<moonray::shading::Xform>(this);
    mIspc.mXform = mXform->getIspcXform();
}

void
ND_normalmap::sample(const Map* self, moonray::shading::TLState *tls,
                 const moonray::shading::State& state, Color* sample)
{
    const ND_normalmap* me = static_cast<const ND_normalmap*>(self);

    Vec3f inValue;
    inValue = evalVec3f(me, inAttr, tls, state);

    if (me->mIspc.mDisableMode) {
        *sample = Color(inValue.x, inValue.y, inValue.z);
        return;
    }

    int spaceValue;
    spaceValue = me->get(spaceAttr);

    float scaleValue;
    scaleValue = evalFloat(me, scaleAttr, tls, state);

    Vec3f N;
    if (me->mIspc.mNormalUseDefault) {
        N = state.getN();
    } else {
        N = evalVec3f(me, normalAttr, tls, state);
    }

    Vec3f T;
    if (me->mIspc.mTangentUseDefault) {
        T = state.getdPds();
    } else {
        T = evalVec3f(me, tangentAttr, tls, state);
    }

    Vec3f outValue;
    
    if (spaceValue == 0) { // tangent --> render

        const ReferenceFrame frame(normalize(N), normalize(T));
        inValue = normalize(2.f * inValue - Vec3f(1.f));
        outValue = frame.localToGlobal(inValue);

    } else { // object --> render
        outValue = me->mXform->transformNormal(ispc::SHADING_SPACE_OBJECT, // object
                                               ispc::SHADING_SPACE_RENDER, // render
                                               state,
                                               inValue);
    }

    outValue = normalize(lerp(state.getN(), outValue, scaleValue));
    
    *sample = Color(outValue.x, outValue.y, outValue.z);
}
