from pxr import Gf, Kind, Usd, Sdf, UsdGeom, UsdShade
import shaders

stage = Usd.Stage.CreateNew('TestMaterialInputTypes.usda')
xformPrim = UsdGeom.Xform.Define(stage, '/hello')

# set some values to make usdchecker happy
UsdGeom.SetStageMetersPerUnit(stage, 0.01)
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
stage.SetDefaultPrim(stage.GetPrimAtPath("/hello"))

geometry = []
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube1',  0.1, -1.2,  0.7, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube2',  0.1, -0.9,  0.7, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube3',  0.1, -0.6,  0.7, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube4',  0.1, -0.3,  0.7, 0))

geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube5',  0.1, -1.2,  0.4, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube6',  0.1, -0.9,  0.4, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube7',  0.1, -0.6,  0.4, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube8',  0.1, -0.3,  0.4, 0))

geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube9',  0.1, -1.2,  0.1, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube10', 0.1, -0.9,  0.1, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube11', 0.1, -0.6,  0.1, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube12', 0.1, -0.3,  0.1, 0))

geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube13', 0.1, -1.2, -0.2, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube14', 0.1, -0.9, -0.2, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube15', 0.1, -0.6, -0.2, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube16', 0.1, -0.3, -0.2, 0))

geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube17', 0.1, -1.2, -0.5, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube18', 0.1, -0.9, -0.5, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube19', 0.1, -0.6, -0.5, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube20', 0.1, -0.3, -0.5, 0))

geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube21', 0.1, -1.2, -0.8, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube22', 0.1, -0.9, -0.8, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube23', 0.1, -0.6, -0.8, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube24', 0.1, -0.3, -0.8, 0))

geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube25', 0.1,  0.1,  0.7, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube26', 0.1,  0.4,  0.7, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube27', 0.1,  0.7,  0.7, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube28', 0.1,  1.0,  0.7, 0))

geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube29', 0.1,  0.1,  0.4, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube30', 0.1,  0.4,  0.4, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube31', 0.1,  0.7,  0.4, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube32', 0.1,  1.0,  0.4, 0))

geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube33', 0.1,  0.1,  0.1, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube34', 0.1,  0.4,  0.1, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube35', 0.1,  0.7,  0.1, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube36', 0.1,  1.0,  0.1, 0))

geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube37', 0.1,  0.1, -0.2, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube38', 0.1,  0.4, -0.2, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube39', 0.1,  0.7, -0.2, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube40', 0.1,  1.0, -0.2, 0))

geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube41', 0.1,  0.1, -0.5, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube42', 0.1,  0.4, -0.5, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube43', 0.1,  0.7, -0.5, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube44', 0.1,  1.0, -0.5, 0))

index=-1

#
# Bool tests
#
# test Bool default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Bool")
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Bool value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Bool", inBool=True)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Bool -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestBoolOutputMap(stage, material, 'MyTestBoolOutputMap')
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Bool", inBool=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Bool -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material, 'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,1))
texture = shaders.create_TestBoolOutputMap(stage, material, 'MyTestBoolOutputMap', inAttr=texture)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Bool", inBool=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Int tests
#
# test Int default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Int")
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Int value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Int", inInt=16711935)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Int -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestIntOutputMap(stage, material, 'MyTestIntOutputMap')
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Int", inInt=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Int -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material, 'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,0))
texture = shaders.create_TestIntOutputMap(stage, material, 'MyTestIntOutputMap', inAttr=texture)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Int", inInt=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# String tests
#
# test String default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="String")
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test String value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="String", inString="1.0 0.0 1.0")
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> String -> Map
index+=1
#testName= '/MyMaterialTest'+str(index)
#material = UsdShade.Material.Define(stage,testName)
#texture = shaders.create_TestStringOutputMap(stage, material, 'MyTestStringOutputMap')
#pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="String", inString=texture)
#material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
#UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> String -> Map
index+=1
#testName= '/MyMaterialTest'+str(index)
#material = UsdShade.Material.Define(stage,testName)
#texture = shaders.create_CheckerboardMap(stage,material, 'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,0))
#texture = shaders.create_TestStringOutputMap(stage, material, 'MyTestStringOutputMap', inAttr=texture)
#pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="String", inString=texture)
#material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
#UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Float tests
#
# test Float default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Float")
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test vec2f value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Float", inFloat=0.8)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Color -> (Float eval) Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestColorOutputMap(stage, material, 'MyTestColorMap')
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Float", inFloat=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Color -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material, 'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(0.8,0.0,0.0), color_B=(0.0,0.2,0.0))
texture = shaders.create_TestColorOutputMap(stage, material, 'MyTestColorOutputMap', inAttr=texture)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Float", inFloat=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Vec2f tests
#
# test Vec2f default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Vec2f")
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test vec2f value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Vec2f", inVec2f=(0.9,0.1))
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Color -> (Vec2f eval) Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestColorOutputMap(stage, material, 'MyTestColorMap')
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Vec2f", inVec2f=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Color -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material, 'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(0.8,0.2,0), color_B=(0.2,0.8,0))
texture = shaders.create_TestColorOutputMap(stage, material, 'MyTestColorOutputMap', inAttr=texture)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Vec2f", inVec2f=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Vec3f tests
#
# test vec3f default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Vec3f")
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Vec3f value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Vec3f", inVec3f=(1.0,0.0,1.0))
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Vec3 default -> Map -> Vec3 -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestColorOutputMap(stage, material, 'MyTestColorMap')
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Vec3f", inVec3f=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Vec3 -> Map -> Vec3f -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material, 'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,0))
texture = shaders.create_TestColorOutputMap(stage, material, 'MyTestColorOutputMap', inAttr=texture)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Vec3f", inVec3f=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Vec4f tests
#
# test Vec4f default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Vec4f")
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Vec4f value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Vec4f", inVec4f=(1.0,0.0,1.0,1.0))
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Vec4f default -> Map -> Vec4f -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestVec4fOutputMap(stage, material, 'MyTestVec4fOutputMap')
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Vec4f", inVec4f=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Vec4f -> Map -> Vec4f -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material, 'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,0))
texture = shaders.create_TestVec4fOutputMap(stage, material, 'MyTestVec4fOutputMap', inAttr=texture)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Vec4f", inVec4f=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Color tests
#
# test vec3f default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Color")
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Color", inColor=(1.0,0.0,1.0))
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Color -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestColorOutputMap(stage, material, 'MyTestColorMap')
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Color", inColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Color -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material, 'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,0))
texture = shaders.create_TestColorOutputMap(stage, material, 'MyTestColorOutputMap', inAttr=texture)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Color", inColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Rgba tests
#
# test Rgba default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Rgba")
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Rgba value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Rgba", inRgba=(1.0,0.0,1.0,1.0))
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Rgba -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestRgbaOutputMap(stage, material, 'MyTestRgbaOutputMap')
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Rgba", inRgba=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Rgba -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material, 'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,0))
texture = shaders.create_TestRgbaOutputMap(stage, material, 'MyTestRgbaOutputMap', inAttr=texture)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Rgba", inRgba=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Mat3f tests
#
# test Mat3f default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Mat3f")
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Mat3f value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Mat3f", inMat3f=Gf.Matrix3d(1.0,0.0,0.0, 0.0,0.0,0.0, 0.0,0.0,1.0))
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Mat3f -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestMat3fOutputMap(stage, material, 'MyTestMat3fOutputMap')
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Mat3f", inMat3f=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Mat3f -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material, 'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,0))
texture = shaders.create_TestMat3fOutputMap(stage, material, 'MyTestMat3fOutputMap', inAttr=texture)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Mat3f", inMat3f=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Mat4f tests
#
# test Mat4f default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Mat4f")
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Mat4f value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Mat4f", inMat4f=Gf.Matrix4d(1.0,0.0,0.0,0.0, 0.0,0.0,0.0,0.0, 0.0,0.0,1.0,0.0, 0.0,0.0,0.0,0.0))
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Mat4f -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestMat4fOutputMap(stage, material, 'MyTestMat4fOutputMap')
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Mat4f", inMat4f=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Mat4f -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material, 'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,0))
texture = shaders.create_TestMat4fOutputMap(stage, material, 'MyTestMat4fOutputMap', inAttr=texture)
pbrShader = shaders.create_TestInputsMaterial(stage, material, 'MyMaterialShader', select="Mat4f", inMat4f=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# save off a .usda file
#
stage.Save()
