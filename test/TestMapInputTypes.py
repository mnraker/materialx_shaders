from pxr import Gf, Kind, Usd, Sdf, UsdGeom, UsdShade
import shaders

stage = Usd.Stage.CreateNew('TestMapInputTypes.usda')
xformPrim = UsdGeom.Xform.Define(stage, '/hello')

# set some values to make usdchecker happy
UsdGeom.SetStageMetersPerUnit(stage, 0.01)
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
stage.SetDefaultPrim(stage.GetPrimAtPath("/hello"))

geometry = []
y=0.7
x=-1.2
xStep=0.3
yStep=-0.28
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube1',  0.1, x+0*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube2',  0.1, x+1*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube3',  0.1, x+2*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube4',  0.1, x+3*xStep, y, 0))

y+=yStep
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube5',  0.1, x+0*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube6',  0.1, x+1*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube7',  0.1, x+2*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube8',  0.1, x+3*xStep, y, 0))

y+=yStep
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube9',  0.1, x+0*xStep,  y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube10', 0.1, x+1*xStep,  y, 0))

y+=yStep
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube13', 0.1, x+0*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube14', 0.1, x+1*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube15', 0.1, x+2*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube16', 0.1, x+3*xStep, y, 0))

y+=yStep
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube17', 0.1, x+0*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube18', 0.1, x+1*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube19', 0.1, x+2*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube20', 0.1, x+3*xStep, y, 0))

y+=yStep
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube21', 0.1, x+0*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube22', 0.1, x+1*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube23', 0.1, x+2*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube24', 0.1, x+3*xStep, y, 0))

y=0.7
x=0.1
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube25', 0.1, x+0*xStep,  y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube26', 0.1, x+1*xStep,  y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube27', 0.1, x+2*xStep,  y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube28', 0.1, x+3*xStep,  y, 0))

y+=yStep
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube29', 0.1, x+0*xStep,  y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube30', 0.1, x+1*xStep,  y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube31', 0.1, x+2*xStep,  y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube32', 0.1, x+3*xStep,  y, 0))

y+=yStep
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube33', 0.1, x+0*xStep,  y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube34', 0.1, x+1*xStep,  y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube35', 0.1, x+2*xStep,  y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube36', 0.1, x+3*xStep,  y, 0))

y+=yStep
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube37', 0.1, x+0*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube38', 0.1, x+1*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube39', 0.1, x+2*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube40', 0.1, x+3*xStep, y, 0))

y+=yStep
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube41', 0.1, x+0*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube42', 0.1, x+1*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube43', 0.1, x+2*xStep, y, 0))
geometry.append(shaders.create_MeshCube(stage, xformPrim, 'cube44', 0.1, x+3*xStep, y, 0))

index=-1

#
# Bool tests
#
# test Bool default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Bool")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Bool value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Bool", inBool=True)
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Bool -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestBoolOutputMap(stage, material,'MyTestBoolOutputMap')
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inBool=texture, select="Bool")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Bool -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material,'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,1))
texture = shaders.create_TestBoolOutputMap(stage, material,'MyTestBoolOutputMap', inAttr=texture)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inBool=texture, select="Bool")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Int tests
#
# test Int default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Int")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Int value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Int", inInt=16711935)
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Int -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestIntOutputMap(stage, material,'MyTestIntOutputMap')
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inInt=texture, select="Int")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Int -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material,'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,0))
texture = shaders.create_TestIntOutputMap(stage, material,'MyTestIntOutputMap', inAttr=texture)
# this is for triggering an intentional fail mode
#texture = shaders.create_TestIntOutputMap(stage, material,'MyTestIntOutputMap', inAttr=(0.6785,0.0,0.0))
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inInt=texture, select="Int")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# String tests
#
# test String default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="String")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test String value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="String", inString="1.0 0.0 1.0")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# Map evaluation isn't supported for Strings
# test Color default -> Map -> String -> Map
# test Checkerboard -> Color -> Map -> String -> Map

#
# Float tests
#
# test Float default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Float")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test vec2f value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Float", inFloat=0.8)
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Color -> (Float eval) Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestColorOutputMap(stage, material,'MyTestColorMap')
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inFloat=texture, select="Float")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Color -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material,'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(0.8,0.0,0.0), color_B=(0.0,0.2,0.0))
texture = shaders.create_TestColorOutputMap(stage, material,'MyTestColorOutputMap', inAttr=texture)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inFloat=texture, select="Float")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Vec2f tests
#
# test Vec2f default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Vec2f")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test vec2f value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Vec2f", inVec2f=(0.9,0.1))
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Color -> (Vec2f eval) Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestColorOutputMap(stage, material,'MyTestColorMap')
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inVec2f=texture, select="Vec2f")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Color -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material,'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(0.8,0.2,0), color_B=(0.2,0.8,0))
texture = shaders.create_TestColorOutputMap(stage, material,'MyTestColorOutputMap', inAttr=texture)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inVec2f=texture, select="Vec2f")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Vec3f tests
#
# test vec3f default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Vec3f")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Vec3f value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Vec3f", inVec3f=(1.0,0.0,1.0))
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Vec3 default -> Map -> Vec3 -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestColorOutputMap(stage, material,'MyTestColorMap')
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inVec3f=texture, select="Vec3f")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Vec3 -> Map -> Vec3f -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material,'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,0))
texture = shaders.create_TestColorOutputMap(stage, material,'MyTestColorOutputMap', inAttr=texture)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inVec3f=texture, select="Vec3f")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Vec4f tests
#
# test Vec4f default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Vec4f")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Vec4f value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Vec4f", inVec4f=(1.0,0.0,1.0,1.0))
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Vec4f default -> Map -> Vec4f -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestVec4fOutputMap(stage, material,'MyTestVec4fOutputMap')
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inVec4f=texture, select="Vec4f")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Vec4f -> Map -> Vec4f -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material,'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,0))
texture = shaders.create_TestVec4fOutputMap(stage, material,'MyTestVec4fOutputMap', inAttr=texture)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inVec4f=texture, select="Vec4f")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Color tests
#
# test vec3f default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Color")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Color", inColor=(1.0,0.0,1.0))
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Color -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestColorOutputMap(stage, material,'MyTestColorMap')
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inColor=texture, select="Color")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Color -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material,'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,0))
texture = shaders.create_TestColorOutputMap(stage, material,'MyTestColorOutputMap', inAttr=texture)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inColor=texture, select="Color")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Rgba tests
#
# test Rgba default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Rgba")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Rgba value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Rgba", inRgba=(1.0,0.0,1.0,1.0))
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Rgba -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestRgbaOutputMap(stage, material,'MyTestRgbaOutputMap')
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inRgba=texture, select="Rgba")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Rgba -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material,'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,0))
texture = shaders.create_TestRgbaOutputMap(stage, material,'MyTestRgbaOutputMap', inAttr=texture)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inRgba=texture, select="Rgba")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Mat3f tests
#
# test Mat3f default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Mat3f")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Mat3f value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Mat3f", inMat3f=Gf.Matrix3d(1.0,0.0,0.0, 0.0,0.0,0.0, 0.0,0.0,1.0))
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Mat3f -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestMat3fOutputMap(stage, material,'MyTestMat3fOutputMap')
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inMat3f=texture, select="Mat3f")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Mat3f -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material,'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,0))
texture = shaders.create_TestMat3fOutputMap(stage, material,'MyTestMat3fOutputMap', inAttr=texture)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inMat3f=texture, select="Mat3f")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# Mat4f tests
#
# test Mat4f default -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Mat4f")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Mat4f value -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', select="Mat4f", inMat4f=Gf.Matrix4d(1.0,0.0,0.0,0.0, 0.0,0.0,0.0,0.0, 0.0,0.0,1.0,0.0, 0.0,0.0,0.0,0.0))
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Color default -> Map -> Mat4f -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_TestMat4fOutputMap(stage, material,'MyTestMat4fOutputMap')
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inMat4f=texture, select="Mat4f")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

# test Checkerboard -> Color -> Map -> Mat4f -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture = shaders.create_CheckerboardMap(stage,material,'checkerboard', num_u_tiles=16, num_v_tiles=16, color_A=(1,0,0), color_B=(0,1,0))
texture = shaders.create_TestMat4fOutputMap(stage, material,'MyTestMat4fOutputMap', inAttr=texture)
texture = shaders.create_TestInputsMap(stage, material,'MyTestInputsMap', inMat4f=texture, select="Mat4f")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# save off a .usda file
#
stage.Save()
