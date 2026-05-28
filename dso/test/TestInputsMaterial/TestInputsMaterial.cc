// Copyright 2024 DreamWorks Animation LLC
// SPDX-License-Identifier: Apache-2.0

/// @file TestInputsMaterial.cc

#include "attributes.cc"
#include "TestInputsMaterial_ispc_stubs.h"

#include <moonray/rendering/shading/MaterialApi.h>
#include "labels.h"

using namespace scene_rdl2::math;
using namespace moonray::shading;

RDL2_DSO_CLASS_BEGIN(TestInputsMaterial, Material)
public:
    TestInputsMaterial(SceneClass const &sceneClass, std::string const &name);
    void update();

private:

    static void shade(const Material *self, moonray::shading::TLState *tls,
                       const moonray::shading::State &state, BsdfBuilder& bsdfBuilder);
    // mIspc needs to be the first use of storage by this derived class
    // since ISPC cheats and gets it's offset by knowing it's first
    ispc::TestInputsMaterial mIspc;

RDL2_DSO_CLASS_END(TestInputsMaterial)

TestInputsMaterial::TestInputsMaterial(const SceneClass& sceneClass,
        const std::string& name) :
    Parent(sceneClass, name)
{
    mShadeFunc = TestInputsMaterial::shade;
    mShadeFuncv = (ShadeFuncv) ispc::TestInputsMaterial_getShadeFunc();
}

void
TestInputsMaterial::update()
{
    String select = get(selectAttr);
    if ((select == "bool") || (select == "Bool")) {
        mIspc.choice= ispc::INPUT_BOOL;
    } else if ((select == "int") || (select == "Int")) {
        mIspc.choice= ispc::INPUT_INT;
    } else if (select == "String") {
        {
            String inStringValue = get(inStringAttr);
            int firstSpace = inStringValue.find(' ');
            int secondSpace = inStringValue.rfind(' ');
            if ((firstSpace != std::string::npos) && (secondSpace != std::string::npos)) {
                Color outValue;
                mIspc.colorValue.r = std::stof(inStringValue.substr(0,firstSpace));
                mIspc.colorValue.g = std::stof(inStringValue.substr(firstSpace+1, secondSpace - firstSpace - 1));
                mIspc.colorValue.b = std::stof(inStringValue.substr(secondSpace+1));
            } else {
	            mIspc.colorValue.r = 0.0f;
                mIspc.colorValue.g = 0.0f;
                mIspc.colorValue.b = 0.0f;
            }
            mIspc.choice= ispc::INPUT_STRING;
		}
    } else if (select == "Float") {
        mIspc.choice= ispc::INPUT_FLOAT;
    } else if (select == "Vec2f") {
        mIspc.choice= ispc::INPUT_VEC2F;
    } else if (select == "Vec3f") {
        mIspc.choice= ispc::INPUT_VEC3F;
    } else if (select == "Vec4f") {
        mIspc.choice= ispc::INPUT_VEC4F;
    } else if (select == "Color") {
        mIspc.choice= ispc::INPUT_COLOR;
    } else if (select == "Rgba") {
        mIspc.choice= ispc::INPUT_RGBA;
    } else if (select == "Mat3f") {
        mIspc.choice= ispc::INPUT_MAT3F;
    } else if (select == "Mat4f") {
        mIspc.choice= ispc::INPUT_MAT4F;
    } else if (select == "SceneObject") {
        mIspc.choice= ispc::INPUT_SCENEOBJECT;
    } else if (select == "BoolVector") {
        mIspc.choice= ispc::INPUT_BOOLVECTOR;
    } else if (select == "IntVector") {
        mIspc.choice= ispc::INPUT_INTVECTOR;
    } else if (select == "StringVector") {
        {
            StringVector inStringVectorValue = get(inStringVectorAttr);
            Color outValue= Color(0.0f, 0.0f, 0.0f);
            if (inStringVectorValue.size() > 0) {
                String inStringValue = inStringVectorValue[0];
                if (inStringValue == "red") {
                    outValue = Color(1.0f, 0.0f, 0.0f);
                } else if (inStringValue == "green") {
                    outValue = Color(0.0f, 1.0f, 0.0f);
                } else if (inStringValue == "blue") {
                    outValue = Color(0.0f, 0.0f, 1.0f);
                } else if (inStringValue == "cyan") {
                    outValue = Color(0.0f, 1.0f, 1.0f);
                } else if (inStringValue == "magenta") {
                    outValue = Color(1.0f, 0.0f, 1.0f);
                } else if (inStringValue == "yellow") {
                    outValue = Color(1.0f, 1.0f, 0.0f);
                } else if (inStringValue == "white") {
                    outValue = Color(1.0f, 1.0f, 1.0f);
                } else if (inStringValue == "black") {
                    outValue = Color(0.0f, 0.0f, 0.0f);
                }
            }
			mIspc.colorValue.r = outValue.r;
	        mIspc.colorValue.g = outValue.g;
	        mIspc.colorValue.b = outValue.b;
        }
        mIspc.choice= ispc::INPUT_STRINGVECTOR;
    } else if (select == "FloatVector") {
        mIspc.choice= ispc::INPUT_FLOATVECTOR;
    } else if (select == "Vec2fVector") {
        mIspc.choice= ispc::INPUT_VEC2FVECTOR;
    } else if (select == "Vec3fVector") {
        mIspc.choice= ispc::INPUT_VEC3FVECTOR;
    } else if (select == "Vec4fVector") {
        mIspc.choice= ispc::INPUT_VEC4FVECTOR;
    } else if (select == "RgbVector") {
        mIspc.choice= ispc::INPUT_RGBVECTOR;
    } else if (select == "RgbaVector") {
        mIspc.choice= ispc::INPUT_RGBAVECTOR;
    } else if (select == "Mat3fVector") {
        mIspc.choice= ispc::INPUT_MAT3FVECTOR;
    } else if (select == "Mat4fVector") {
        mIspc.choice= ispc::INPUT_MAT4FVECTOR;
    } else if (select == "SceneObjectVector") {
        mIspc.choice= ispc::INPUT_SCENEOBJECTVECTOR;
    } else {
        mIspc.choice= -1;
    }
}

void
TestInputsMaterial::shade(const Material* self, moonray::shading::TLState *tls,
                 const moonray::shading::State& state, BsdfBuilder& bsdfBuilder)
{
    const TestInputsMaterial* me = static_cast<const TestInputsMaterial*>(self);

    Bool   inBoolValue   = evalBool(  me, inBoolAttr,   tls, state);
    Int    inIntValue    = evalInt(   me, inIntAttr,    tls, state);
    Float  inFloatValue  = evalFloat( me, inFloatAttr,  tls, state);
    Vec2f  inVec2fValue  = evalVec2f( me, inVec2fAttr,  tls, state);
    Vec3f  inVec3fValue  = evalVec3f( me, inVec3fAttr,  tls, state);
    Vec4f  inVec4fValue  = evalVec4f( me, inVec4fAttr,  tls, state);
    Color  inColorValue  = evalColor( me, inColorAttr,  tls, state);
    Rgba   inRgbaValue   = evalRgba(  me, inRgbaAttr,   tls, state);
    Mat3f  inMat3fValue  = evalMat3f( me, inMat3fAttr,  tls, state);
    Mat4f  inMat4fValue  = evalMat4f( me, inMat4fAttr,  tls, state);
    SceneObject* inSceneObjectValue = evalSceneObject( me, inSceneObjectAttr,  tls, state);

    BoolVector   inBoolVectorValue   = evalBoolVector(  me, inBoolVectorAttr,   tls, state);
    IntVector    inIntVectorValue    = evalIntVector(   me, inIntVectorAttr,    tls, state);
    StringVector inStringVectorValue = me->get(inStringVectorAttr);
    FloatVector  inFloatVectorValue  = evalFloatVector( me, inFloatVectorAttr,  tls, state);
    Vec2fVector  inVec2fVectorValue  = evalVec2fVector( me, inVec2fVectorAttr,  tls, state);
    Vec3fVector  inVec3fVectorValue  = evalVec3fVector( me, inVec3fVectorAttr,  tls, state);
    Vec4fVector  inVec4fVectorValue  = evalVec4fVector( me, inVec4fVectorAttr,  tls, state);
    RgbVector    inRgbVectorValue  = evalRgbVector(   me, inRgbVectorAttr,  tls, state);
    RgbaVector   inRgbaVectorValue   = evalRgbaVector(  me, inRgbaVectorAttr,   tls, state);
    Mat3fVector  inMat3fVectorValue  = evalMat3fVector( me, inMat3fVectorAttr,  tls, state);
    Mat4fVector  inMat4fVectorValue  = evalMat4fVector( me, inMat4fVectorAttr,  tls, state);
    SceneObjectVector inSceneObjectVectorValue = evalSceneObjectVector(me, inSceneObjectVectorAttr,  tls, state);

    Color outValue = Color(0.0,0.0,0.0);

    switch (me->mIspc.choice) {
      case ispc::INPUT_BOOL:
        if (inBoolValue) {
            outValue = Color(0.75, 0.75, 0.75);
        } else {
            outValue = Color(0.25, 0.25, 0.25);
        }
        break;
      case ispc::INPUT_INT:
        outValue.r = (inIntValue&0xFF)/255.0;
        outValue.g = ((inIntValue>>8)&0xFF)/255.0;
        outValue.b = ((inIntValue>>16)&0xFF)/255.0;
        break;
      case ispc::INPUT_STRING:
		outValue = Color(me->mIspc.colorValue.r, me->mIspc.colorValue.g, me->mIspc.colorValue.b);
        break;
      case ispc::INPUT_FLOAT:
        outValue = Color(inFloatValue);
        break;
      case ispc::INPUT_VEC2F:
        outValue = Color(inVec2fValue.x, inVec2fValue.y, 0.0f);
        break;
      case ispc::INPUT_VEC3F:
        outValue = Color(inVec3fValue.x, inVec3fValue.y, inVec3fValue.z);
        break;
      case ispc::INPUT_VEC4F:
        outValue = Color(inVec4fValue.x, inVec4fValue.y, inVec4fValue.z);
        break;
      case ispc::INPUT_COLOR:
        outValue = inColorValue;
        break;
      case ispc::INPUT_RGBA:
        outValue = Color(inRgbaValue.r,inRgbaValue.g, inRgbaValue.b);
        break;
      case ispc::INPUT_MAT3F:
        outValue = Color(inMat3fValue.vx.x,inMat3fValue.vy.y, inMat3fValue.vz.z);
        break;
      case ispc::INPUT_MAT4F:
        outValue = Color(inMat4fValue.vx.x,inMat4fValue.vy.y, inMat4fValue.vz.z);
        break;
      case ispc::INPUT_SCENEOBJECT:
        if (inSceneObjectValue == nullptr) {
            outValue= Color(0.1,0.1,0.1);
        } else {
            outValue = inSceneObjectValue->get<Color>(std::string("color_value"));
        }
        break;
      case ispc::INPUT_BOOLVECTOR:
        // use 24 bools to pass a decent approximation of the color through
        {
            if (inIntVectorValue.size() > 23) {
                int index = 0;
                int factor = 1;
                int value = 0;
                for (int i=0; i<8; i++) {
                    if (inBoolVectorValue[index]) {
                        value += factor;
                    }
                    index++;
                    factor *= 2;
                }
                outValue.r = value/255.0;
                factor = 1;
                value = 0;
                for (int i=0; i<8; i++) {
                    if (inBoolVectorValue[index]) {
                        value += factor;
                    }
                    index++;
                    factor *= 2;
                }
                outValue.g = value/255.0;
                factor = 1;
                value = 0;
                for (int i=0; i<8; i++) {
                    if (inBoolVectorValue[index]) {
                        value += factor;
                    }
                    index++;
                    factor *= 2;
                }
                outValue.b = value/255.0;
           }
        }
        break;
      case ispc::INPUT_INTVECTOR:
        // The Color is split over three values to pass it through completely
        if (inIntVectorValue.size() > 0) {
            outValue.r = inIntVectorValue[0]/65536.0f;
        }
        if (inFloatVectorValue.size() > 1) {
            outValue.g = inIntVectorValue[1]/65536.0f;
        }
        if (inFloatVectorValue.size() > 2) {
            outValue.b = inIntVectorValue[2]/65536.0f;
        }
        break;
      case ispc::INPUT_STRINGVECTOR:
		outValue = Color(me->mIspc.colorValue.r, me->mIspc.colorValue.g, me->mIspc.colorValue.b);
        break;
      case ispc::INPUT_FLOATVECTOR:
        // The Color is split over three values to pass it through completely
        if (inFloatVectorValue.size() > 0) {
            outValue.r = inFloatVectorValue[0];
        }
        if (inFloatVectorValue.size() > 1) {
            outValue.g = inFloatVectorValue[1];
        }
        if (inFloatVectorValue.size() > 2) {
            outValue.b = inFloatVectorValue[2];
        }
        break;
      case ispc::INPUT_VEC2FVECTOR:
        // The Color is split over two values to pass it through completely
        if (inVec2fVectorValue.size() > 0) {
            Vec2f inVec2fValue = inVec2fVectorValue[0];
            outValue.r = inVec2fValue.x;
            outValue.g = inVec2fValue.y;
        }
        if (inVec2fVectorValue.size() > 1) {
            Vec2f inVec2fValue = inVec2fVectorValue[0];
            outValue.b = inVec2fVectorValue[1].x;
        }
        break;
      case ispc::INPUT_VEC3FVECTOR:
        if (inVec3fVectorValue.size() > 0) {
            Vec3f inVec3fValue = inVec3fVectorValue[0];
            outValue = Color(inVec3fValue.x, inVec3fValue.y, inVec3fValue.z);
        }
        break;
      case ispc::INPUT_VEC4FVECTOR:
        if (inVec4fVectorValue.size() > 0) {
            Vec4f inVec4fValue = inVec4fVectorValue[0];
            outValue = Color(inVec4fValue.x, inVec4fValue.y, inVec4fValue.z);
        }
        break;
      case ispc::INPUT_RGBVECTOR:
        if (inRgbVectorValue.size() > 0) {
            outValue = inRgbVectorValue[0];
        }
        break;
      case ispc::INPUT_RGBAVECTOR:
        if (inRgbaVectorValue.size() > 0) {
            Rgba inRgbaValue = inRgbaVectorValue[0];
            outValue = Color(inRgbaValue.r,inRgbaValue.g, inRgbaValue.b);
        }
        break;
      case ispc::INPUT_MAT3FVECTOR:
        if (inMat3fVectorValue.size() > 0) {
            Mat3f inMat3fValue = inMat3fVectorValue[0];
            outValue = Color(inMat3fValue.vx.x,inMat3fValue.vy.y, inMat3fValue.vz.z);
        }
        break;
      case ispc::INPUT_MAT4FVECTOR:
        if (inMat4fVectorValue.size() > 0) {
            Mat4f inMat4fValue = inMat4fVectorValue[0];
            outValue = Color(inMat4fValue.vx.x,inMat4fValue.vy.y, inMat4fValue.vz.z);
        }
        break;
      case ispc::INPUT_SCENEOBJECTVECTOR:
        break;
      default:
        break;
    }
    bsdfBuilder.addEmission(outValue);
}

