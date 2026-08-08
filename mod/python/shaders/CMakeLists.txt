# SPDX-License-Identifier: Apache-2.0
# Copyright Contributors to the Moonray Project

# if building at the same time as scene_rdl2 we need to get access to the
# scene_rdl2 python module before it is installed so point to it in the
# build directory. Otherwise it should already be in the environment.

if(WIN32)
    set(MTLX_ENV_PATH_SEPARATOR ";")
else()
    set(MTLX_ENV_PATH_SEPARATOR ":")
endif()

if(EXISTS "${CMAKE_BINARY_DIR}/moonray/scene_rdl2" AND IS_DIRECTORY "${CMAKE_BINARY_DIR}/moonray/scene_rdl2")
    set(PYTHONPATH_WITH_SCENE_RDL2 "${CMAKE_BINARY_DIR}/moonray/scene_rdl2/mod/python/py_scene_rdl2${MTLX_ENV_PATH_SEPARATOR}$ENV{PYTHONPATH}")
elseif(EXISTS "${CMAKE_BINARY_DIR}/openmoonray/moonray/scene_rdl2" AND IS_DIRECTORY "${CMAKE_BINARY_DIR}/openmoonray/moonray/scene_rdl2")
    set(PYTHONPATH_WITH_SCENE_RDL2 "${CMAKE_BINARY_DIR}/openmoonray/moonray/scene_rdl2/mod/python/py_scene_rdl2${MTLX_ENV_PATH_SEPARATOR}$ENV{PYTHONPATH}")
else()
    set(PYTHONPATH_WITH_SCENE_RDL2 "$ENV{PYTHONPATH}")
endif()

if(DEFINED ENV{RDL2_DSO_PATH} AND NOT "$ENV{RDL2_DSO_PATH}" STREQUAL "")
    set(RDL2_DSO_PATH_WITH_BUILD "${CMAKE_BINARY_DIR}/rdl2dso${MTLX_ENV_PATH_SEPARATOR}$ENV{RDL2_DSO_PATH}")
else()
    set(RDL2_DSO_PATH_WITH_BUILD "${CMAKE_BINARY_DIR}/rdl2dso")
endif()


if(WIN32)
    set(MTLX_RUNTIME_PATH
        "${CMAKE_BINARY_DIR}/moonray/scene_rdl2/lib/scene/rdl2;${CMAKE_BINARY_DIR}/moonray/scene_rdl2/lib/render/logging;${CMAKE_BINARY_DIR}/moonray/scene_rdl2/lib/render/util;${CMAKE_BINARY_DIR}/moonray/scene_rdl2/lib/common/math;$ENV{REZ_BOOST_ROOT}/lib;$ENV{REZ_ONETBB_ROOT}/bin;$ENV{REZ_LOG4CPLUS_ROOT}/bin;$ENV{REZ_JSONCPP_ROOT}/bin;$ENV{REZ_PYTHON_ROOT}/bin"
    )
endif()
if(WIN32)
    add_custom_command(
        OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/shaders.py
        COMMAND ${CMAKE_COMMAND} -E env
            "PYTHONPATH=${PYTHONPATH_WITH_SCENE_RDL2}"
            "RDL2_DSO_PATH=${RDL2_DSO_PATH_WITH_BUILD}"
            "PATH=${MTLX_RUNTIME_PATH}"
            ${Python_EXECUTABLE}
            ${GENERATE_PYTHON_CREATE_FUNCTIONS}
            -o ${CMAKE_CURRENT_BINARY_DIR}/shaders.py
        COMMENT "Generating shaders.py"
        DEPENDS
        "${CMAKE_CURRENT_SOURCE_DIR}/../generate_python_create_functions/generate_python_create_functions"
        scene_rdl2
        __scene_rdl2__
        scene_rdl2_module
        VERBATIM
    )
else()
    add_custom_command(
        OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/shaders.py
        COMMAND ${CMAKE_COMMAND} -E env
            "PYTHONPATH=${PYTHONPATH_WITH_SCENE_RDL2}"
            "RDL2_DSO_PATH=${RDL2_DSO_PATH_WITH_BUILD}"
            ${Python_EXECUTABLE}
            ${GENERATE_PYTHON_CREATE_FUNCTIONS}
            -o ${CMAKE_CURRENT_BINARY_DIR}/shaders.py
        COMMENT "Generating shaders.py"
        DEPENDS
        "${CMAKE_CURRENT_SOURCE_DIR}/../generate_python_create_functions/generate_python_create_functions"
        scene_rdl2
        __scene_rdl2__
        scene_rdl2_module
        VERBATIM
    )
endif()

add_custom_target(
	shaders ALL
	DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/shaders.py
)

add_dependencies(shaders all_shader_dsos)

if (EXISTS "${CMAKE_BINARY_DIR}/moonray/scene_rdl2" AND IS_DIRECTORY "${CMAKE_BINARY_DIR}/moonray/scene_rdl2")
	add_dependencies(shaders scene_rdl2 __scene_rdl2__ scene_rdl2_module)
	add_dependencies(shaders DwaEmissiveMaterial CheckerboardMap TestInputsMap TestBoolOutputMap TestColorOutputMap TestDisplacement2Map TestInputsMap TestIntOutputMap TestMat3fOutputMap TestMat4fOutputMap TestNormalMap2Map TestRgbaOutputMap TestVec4fOutputMap TestInputsDisplacement TestInputsNormalMap )
elseif(EXISTS "${CMAKE_BINARY_DIR}/openmoonray/moonray/scene_rdl2" AND IS_DIRECTORY "${CMAKE_BINARY_DIR}/openmoonray/moonray/scene_rdl2")
	add_dependencies(shaders scene_rdl2 __scene_rdl2__ scene_rdl2_module)
	add_dependencies(shaders DwaEmissiveMaterial CheckerboardMap TestInputsMap TestBoolOutputMap TestColorOutputMap TestDisplacement2Map TestInputsMap TestIntOutputMap TestMat3fOutputMap TestMat4fOutputMap TestNormalMap2Map TestRgbaOutputMap TestVec4fOutputMap TestInputsDisplacement TestInputsNormalMap )
endif()

set(python_install_dir
		python/lib/python${Python_VERSION_MAJOR}.${Python_VERSION_MINOR}/${PACKAGE_NAME})

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/shaders.py DESTINATION ${python_install_dir})
