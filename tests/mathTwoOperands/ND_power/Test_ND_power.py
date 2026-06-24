from pxr import Gf, Kind, Usd, Sdf, UsdGeom, UsdShade
import materialx_shaders.shaders as shaders

stage = Usd.Stage.CreateNew('Test_ND_power.usda')
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

index=-1

#
# ND_power_float
#
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture1 = shaders.create_CheckerboardMap(stage,material,'checkerboard1', num_u_tiles=2, num_v_tiles=2, color_A=(0.9,0.8,0.7), color_B=(0.6,0.5,0.4))
texture2 = shaders.create_CheckerboardMap(stage,material,'checkerboard2', num_u_tiles=4, num_v_tiles=4, color_A=(1.0,2.0,3.0), color_B=(3.0,1.0,2.0))
texture = shaders.create_ND_power_float(stage, material,'my_power_float', in1=texture1, in2=texture2)
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# ND_power_vector2
#
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture1 = shaders.create_CheckerboardMap(stage,material,'checkerboard1', num_u_tiles=2, num_v_tiles=2, color_A=(0.9,0.8,0.7), color_B=(0.6,0.5,0.4))
texture2 = shaders.create_CheckerboardMap(stage,material,'checkerboard2', num_u_tiles=4, num_v_tiles=4, color_A=(1.0,2.0,3.0), color_B=(3.0,1.0,2.0))
texture = shaders.create_ND_power_vector2(stage, material,'my_power_vector2', in1=texture1, in2=texture2)
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# ND_power_vector3
#
# test Checkerboard -> Color -> Map -> Bool -> Map
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture1 = shaders.create_CheckerboardMap(stage,material,'checkerboard1', num_u_tiles=2, num_v_tiles=2, color_A=(0.9,0.8,0.7), color_B=(0.6,0.5,0.4))
texture2 = shaders.create_CheckerboardMap(stage,material,'checkerboard2', num_u_tiles=4, num_v_tiles=4, color_A=(1.0,2.0,3.0), color_B=(3.0,1.0,2.0))
texture = shaders.create_ND_power_vector3(stage, material,'my_power_vector3', in1=texture1, in2=texture2)
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# ND_power_vector4
#
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture1 = shaders.create_CheckerboardMap(stage,material,'checkerboard1', num_u_tiles=2, num_v_tiles=2, color_A=(0.9,0.8,0.7), color_B=(0.6,0.5,0.4))
texture2 = shaders.create_CheckerboardMap(stage,material,'checkerboard2', num_u_tiles=4, num_v_tiles=4, color_A=(1.0,2.0,3.0), color_B=(3.0,1.0,2.0))
# convert Color to Rgba
texture1 = shaders.create_TestVec4fOutputMap(stage, material,'convertToRgba1', inAttr=texture1)
texture2 = shaders.create_TestVec4fOutputMap(stage, material,'convertToRgba2', inAttr=texture2)
texture = shaders.create_ND_power_vector4(stage, material,'my_power_vector4', in1=texture1, in2=texture2)
# convert the Rgba to a Color
texture = shaders.create_TestInputsMap(stage, material,'convertToColor', inRgba=texture, select="Rgba")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# ND_power_color3
#
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture1 = shaders.create_CheckerboardMap(stage,material,'checkerboard1', num_u_tiles=2, num_v_tiles=2, color_A=(0.9,0.8,0.7), color_B=(0.6,0.5,0.4))
texture2 = shaders.create_CheckerboardMap(stage,material,'checkerboard2', num_u_tiles=4, num_v_tiles=4, color_A=(1.0,2.0,3.0), color_B=(3.0,1.0,2.0))
texture = shaders.create_ND_power_color3(stage, material,'my_power_color3', in1=texture1, in2=texture2)
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# ND_power_color4
#
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture1 = shaders.create_CheckerboardMap(stage,material,'checkerboard1', num_u_tiles=2, num_v_tiles=2, color_A=(0.9,0.8,0.7), color_B=(0.6,0.5,0.4))
texture2 = shaders.create_CheckerboardMap(stage,material,'checkerboard2', num_u_tiles=4, num_v_tiles=4, color_A=(1.0,2.0,3.0), color_B=(3.0,1.0,2.0))
# convert Color to Rgba
texture1 = shaders.create_TestVec4fOutputMap(stage, material,'convertToRgba1', inAttr=texture1)
texture2 = shaders.create_TestVec4fOutputMap(stage, material,'convertToRgba2', inAttr=texture2)
texture = shaders.create_ND_power_color4(stage, material,'my_power_color4', in1=texture1, in2=texture2)
# convert the Rgba to a Color
texture = shaders.create_TestInputsMap(stage, material,'convertToColor', inRgba=texture, select="Rgba")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# ND_power_vector2FA
#
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture1 = shaders.create_CheckerboardMap(stage,material,'checkerboard1', num_u_tiles=2, num_v_tiles=2, color_A=(0.7,1.0,0.5), color_B=(0,0,0))
texture2 = shaders.create_CheckerboardMap(stage,material,'checkerboard2', num_u_tiles=4, num_v_tiles=4, color_A=(1.0,2.0,3.0), color_B=(3.0,1.0,4.0))
texture = shaders.create_ND_power_vector2FA(stage, material,'my_power_vector2FA', in1=texture1, in2=texture2)
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# ND_power_vector3FA
#
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture1 = shaders.create_CheckerboardMap(stage,material,'checkerboard1', num_u_tiles=2, num_v_tiles=2, color_A=(0.9,0.8,0.7), color_B=(0.6,0.5,0.4))
texture2 = shaders.create_CheckerboardMap(stage,material,'checkerboard2', num_u_tiles=4, num_v_tiles=4, color_A=(1.0,2.0,3.0), color_B=(3.0,1.0,4.0))
texture = shaders.create_ND_power_vector3FA(stage, material,'my_power_vector3FA', in1=texture1, in2=texture2)
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# ND_power_vector4FA
#
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture1 = shaders.create_CheckerboardMap(stage,material,'checkerboard1', num_u_tiles=2, num_v_tiles=2, color_A=(0.9,0.8,0.7), color_B=(0.6,0.5,0.4))
texture2 = shaders.create_CheckerboardMap(stage,material,'checkerboard2', num_u_tiles=4, num_v_tiles=4, color_A=(1.0,2.0,3.0), color_B=(3.0,1.0,4.0))
# convert Color to Rgba
texture1 = shaders.create_TestVec4fOutputMap(stage, material,'convertToRgba1', inAttr=texture1)
texture = shaders.create_ND_power_vector4FA(stage, material,'my_power_vector4FA', in1=texture1, in2=texture2)
# convert the Rgba to a Color
texture = shaders.create_TestInputsMap(stage, material,'convertToColor', inRgba=texture, select="Rgba")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# ND_power_color3FA
#
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture1 = shaders.create_CheckerboardMap(stage,material,'checkerboard1', num_u_tiles=2, num_v_tiles=2, color_A=(0.9,0.8,0.7), color_B=(0.6,0.5,0.4))
texture2 = shaders.create_CheckerboardMap(stage,material,'checkerboard2', num_u_tiles=4, num_v_tiles=4, color_A=(1.0,2.0,3.0), color_B=(3.0,1.0,4.0))
texture = shaders.create_ND_power_color3FA(stage, material,'my_power_color3FA', in1=texture1, in2=texture2)
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# ND_power_color4FA
#
index+=1
testName= '/MyMaterialTest'+str(index)
material = UsdShade.Material.Define(stage,testName)
texture1 = shaders.create_CheckerboardMap(stage,material,'checkerboard1', num_u_tiles=2, num_v_tiles=2, color_A=(0.9,0.8,0.7), color_B=(0.6,0.5,0.4))
texture2 = shaders.create_CheckerboardMap(stage,material,'checkerboard2', num_u_tiles=4, num_v_tiles=4, color_A=(1.0,2.0,3.0), color_B=(3.0,1.0,4.0))
# convert Color to Rgba
texture1 = shaders.create_TestVec4fOutputMap(stage, material,'convertToRgba1', inAttr=texture1)
texture = shaders.create_ND_power_color4FA(stage, material,'my_power_color4FA', in1=texture1, in2=texture2)
# convert the Rgba to a Color
texture = shaders.create_TestInputsMap(stage, material,'convertToColor', inRgba=texture, select="Rgba")
pbrShader = shaders.create_UsdPreviewSurface(stage, material,'MyMaterialShader', roughness=0.4, metallic=0.0, diffuseColor=texture)
material.CreateSurfaceOutput().ConnectToSource(pbrShader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(geometry[index]).Bind(material)

#
# save off a .usda file
#
stage.Save()
