# SPDX-License-Identifier: Apache-2.0
# Copyright Contributors to the Moonray Project

message("CMAKE_BINARY_DIR: ${CMAKE_BINARY_DIR}")

add_custom_command(
	OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/shaders.py
	COMMAND ${CMAKE_COMMAND} -E env RDL2_DSO_PATH=${CMAKE_BINARY_DIR}/rdl2dso:$ENV{RDL2_DSO_PATH} ${GENERATE_PYTHON_CREATE_FUNCTIONS} -o ${CMAKE_CURRENT_BINARY_DIR}/shaders.py
    COMMENT "Generating shaders.py"
	DEPENDS ${CMAKE_SOURCE_DIR}/mod/python/generate_python_create_functions/generate_python_create_functions
)

add_custom_target(
	shaders ALL
	DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/shaders.py
)

add_dependencies(shaders all_shader_dsos)

set(python_install_dir
		python/lib/python${Python_VERSION_MAJOR}.${Python_VERSION_MINOR}/${PACKAGE_NAME})

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/shaders.py DESTINATION ${python_install_dir})
