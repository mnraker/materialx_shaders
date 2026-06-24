# Copyright 2025 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

include(RatsTest)

find_package(Python REQUIRED COMPONENTS Interpreter)

function(wrapping_a_function)

    # The following KEYWORD arguments are supported:
    set(options
        DIFF_HEADERS        # Adds an extra CTest with the 'diff' label to compare the canonical
                            # and result image headers.

        DISABLED            # Disables this test for all execution modes
        DISABLED_SCALAR     # Disables this test for scalar execution mode
        DISABLED_VECTOR     # Disables this test for vector execution mode
        DISABLED_XPU        # Disables this test for xpu execution mode

        NO_SCALAR           # | Execution modes to skip for this test. For example, path guiding is
        NO_VECTOR           # | currently only supported in scalar mode, so tests using path guiding may want
        NO_XPU              # | to pass: NO_VECTOR NO_XPU.

        NO_IMAGE_DIFF       # Do not generate update/diff/header stages for this test.
    )

    set(oneValueArgs
        NAME_SUFFIX         # Suffix to be appended to test base name. This allows adding multiple tests from the same CMakeLists.txt
        OUTPUT              # Name of output image file, will be added to render args as -out <OUTPUT>
        RENDERER            # moonray|hd_render (defaults to moonray)
    )

    set(multiValueArgs
        CANONICALS          # List of output files the test produces.
                            # If empty, no canonical/diff/header stages are created for this test.
                            # example: CANONICALS scene.exr aovs.exr more_aovs.exr

        DEPENDS             # List of tests that should be run before this test (for the update and
                            # render stages) when running ctest with multiple jobs (eg. -j N). For example,
                            # for a test that uses checkpoint/resume rendering the resume test should run _after_
                            # the checkpoint test, and should therefore specify the checkpoint test's basename
                            # in its DEPENDS list.
                            # (Note that CTests are always run in the order they are added when -j is omitted,
                            # but specifying an explicit dependency here allows such tests to run in the correct
                            # order when multiple jobs are used via the -J option to the ctest command).

        INPUTS              # (required) Ordered list of input files the test requires.
                            # example: INPUTS scene.rdla scene.rdlb

        DELTAS              # Ordered list of optional delta files for the test.
                            # example: DELTAS deltas.rdla

        ENVIRONMENT         # List of definitions to be available as env vars during test runtime, for example:
                            # ENVIRONMENT TEST_ASSETS_DIR=/some/path ANOTHER_VAR="another value"

        RENDER_ARGS         # List of renderer args to set/override.
        RENDER_ARGS_SCALAR  # | List of renderer args to set/override per execution mode.
        RENDER_ARGS_VECTOR  # | Example: RENDER_ARGS_XPU -scene_var pixel_samples 1 -texture_cache_size 8192
        RENDER_ARGS_XPU     # |
    )

    # parse and validate arguments
    cmake_parse_arguments(ARG "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})


    message("options: ${options}")
    message("oneValueArgs: ${oneValueArgs}")
    message("multiValueArgs: ${multiValueArgs}")

    message("ARG_DIFF_HEADERS: ${ARG_DIFF_HEADERS}")
    message("ARG_DISABLED: ${ARG_DISABLED}")
    message("ARG_DISABLED_SCALAR: ${ARG_DISABLED_SCALAR}")
    message("ARG_DISABLED_VECTOR: ${ARG_DISABLED_VECTOR}")
    message("ARG_DISABLED_XPU: ${ARG_DISABLED_XPU}")
    message("ARG_NO_SCALAR: ${ARG_NO_SCALAR}")
    message("ARG_NO_VECTOR: ${ARG_NO_VECTOR}")
    message("ARG_NO_XPU: ${ARG_NO_XPU}")
	message("ARG_NO_IMAGE_DIFF: ${ARG_NO_IMAGE_DIFF}")
    message("ARG_NAME_SUFFIX: ${ARG_NAME_SUFFIX}")
    message("ARG_OUTPUT: ${ARG_OUTPUT}")
    message("ARG_RENDERER: ${ARG_RENDERER}")
    message("ARG_CANONICALS: ${ARG_CANONICALS}")
    message("ARG_DEPENDS: ${ARG_DEPENDS}")	
    message("ARG_INPUTS: ${ARG_INPUTS}")
    message("ARG_DELTAS: ${ARG_DELTAS}")
    message("ARG_ENVIRONMENT: ${ARG_ENVIRONMENT}")
    message("ARG_RENDER_ARGS: ${ARG_RENDER_ARGS}")
    message("ARG_RENDER_ARGS_SCALAR: ${ARG_RENDER_ARGS_SCALAR}")
    message("ARG_RENDER_ARGS_VECTOR: ${ARG_RENDER_ARGS_VECTOR}")
    message("ARG_RENDER_ARGS_XPU: ${ARG_RENDER_ARGS_XPU}")

endfunction()

# Add a new PaTS test.
# ---------------------
#
# Each call to this function will produce a series of labeled CTests for each of MoonRay's execution modes.
# A typical PaTS test will comprise 9 or more individual CTests, which can later be run in stages; see below.
#
# ---------------------
#
# TEST NAMES:
# Each test will be named according to the following convention:
#   <stage>_<exec_mode>_<basename>[-output]
#
#   * the <stage> token will be update|render|diff|header
#   * the <exec_mode> token will be one of sca|vec|xpu
#   * the [_output] token appears on diff & header stages and will be the name of the image, eg. _scene.exr
#
# ---------------------
#
# LABELS:
# See https://cmake.org/cmake/help/latest/prop_test/LABELS.html
# Each test will have its LABELS property set according to the CTest's stage, with the following convention:
# 'update' labeled CTests will:
#       * Render each test's RDLA scene file multiple times to produce candidate canonical images into a temp directory
#       * Perform a large number of image comparisons between the resulting candidates for each test (using the openimageio idiff tool), gathering and analyzing statistics.
#       * Choose a set of ideal images for each test to serve as canonicals for future runs of the test suite.
#       * This set of canonicals are copied to a subdirectory of the directory specified by the ${RATS_CANONICAL_DIR} cache variable,
#         as well as a file (diff.json) containing tolerances for future comparisons.
#
# 'render' labeled CTests will:
#       * Render the scene to produce images into the build directory under the <execution_mode>/ dir.
#
# 'diff' labeled CTests will:
#       * Execute the 'idiff' command an output image comparing it with previously rendered canonical image of the same name.
#       * Or... compare the header of an output image with previously rendered canonical image of the same name.
#
# ---------------------
function(add_pats_test)

    # The following KEYWORD arguments are supported:
    set(options
        DIFF_HEADERS        # Adds an extra CTest with the 'diff' label to compare the canonical
                            # and result image headers.

        DISABLED            # Disables this test for all execution modes
        DISABLED_SCALAR     # Disables this test for scalar execution mode
        DISABLED_VECTOR     # Disables this test for vector execution mode
        DISABLED_XPU        # Disables this test for xpu execution mode

        NO_SCALAR           # | Execution modes to skip for this test. For example, path guiding is
        NO_VECTOR           # | currently only supported in scalar mode, so tests using path guiding may want
        NO_XPU              # | to pass: NO_VECTOR NO_XPU.

        NO_IMAGE_DIFF       # Do not generate update/diff/header stages for this test.
    )

    set(oneValueArgs
        NAME_SUFFIX         # Suffix to be appended to test base name. This allows adding multiple tests from the same CMakeLists.txt
        OUTPUT              # Name of output image file, will be added to render args as -out <OUTPUT>
        RENDERER            # moonray|hd_render (defaults to moonray)
		SCRIPT              # Path to the usd generation python script (required)
    )

    set(multiValueArgs
        CANONICALS          # List of output files the test produces.
                            # If empty, no canonical/diff/header stages are created for this test.
                            # example: CANONICALS scene.exr aovs.exr more_aovs.exr

        DEPENDS             # List of tests that should be run before this test (for the update and
                            # render stages) when running ctest with multiple jobs (eg. -j N). For example,
                            # for a test that uses checkpoint/resume rendering the resume test should run _after_
                            # the checkpoint test, and should therefore specify the checkpoint test's basename
                            # in its DEPENDS list.
                            # (Note that CTests are always run in the order they are added when -j is omitted,
                            # but specifying an explicit dependency here allows such tests to run in the correct
                            # order when multiple jobs are used via the -J option to the ctest command).

        INPUTS              # Additional rdl files to be passed to the render (probably rarely used)
                            # example: INPUTS scene.rdla scene.rdlb

        DELTAS              # Ordered list of optional delta files for the test.
                            # example: DELTAS deltas.rdla

        ENVIRONMENT         # List of definitions to be available as env vars during test runtime, for example:
                            # ENVIRONMENT TEST_ASSETS_DIR=/some/path ANOTHER_VAR="another value"

        RENDER_ARGS         # List of renderer args to set/override.
        RENDER_ARGS_SCALAR  # | List of renderer args to set/override per execution mode.
        RENDER_ARGS_VECTOR  # | Example: RENDER_ARGS_XPU -scene_var pixel_samples 1 -texture_cache_size 8192
        RENDER_ARGS_XPU     # |
    )

    # parse and validate arguments
    cmake_parse_arguments(ARG "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})

    if(DEFINED ARG_KEYWORDS_MISSING_VALUES)
        message(FATAL_ERROR "Keywords missing values: ${ARG_KEYWORDS_MISSING_VALUES}")
    endif()
    if(DEFINED ARG_UNPARSED_ARGUMENTS)
        message(FATAL_ERROR "Unrecognized arguments: ${ARG_UNPARSED_ARGUMENTS}")
    endif()
	if(NOT DEFINED ARG_SCRIPT)
			message(FATAL_ERROR "add_pats_test() requires a SCRIPT argument")
    endif()

    #
    # configure some paths
    #
	# the following line will give us the relative path from the project source
	# dir to the current source dir, which we can use to generate a unique test name for this test
    file(RELATIVE_PATH test_rel_path ${PROJECT_SOURCE_DIR}/test/ ${CMAKE_CURRENT_SOURCE_DIR})
    set(test_basename ${test_rel_path})
    if(DEFINED ARG_NAME_SUFFIX)
        set(test_basename ${test_rel_path}${ARG_NAME_SUFFIX})
    endif()

    # add CTests
	set(generate_usd_test_name "generate-usd-${test_basename}")
	set(convert_usd_test_name "convert-usd-${test_basename}")
    add_test(NAME ${generate_usd_test_name}
             COMMAND ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/${ARG_SCRIPT} -o scene.usda
             WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
    add_test(NAME ${convert_usd_test_name}
             COMMAND hd_usd2rdl -in scene.usda -out scene.rdla
             WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
	set_tests_properties(${convert_usd_test_name} PROPERTIES DEPENDS ${generate_usd_test_name})

	message("PROJECT_SOURCE_DIR: ${PROJECT_SOURCE_DIR}")
	message("CMAKE_CURRENT_SOURCE_DIR: ${CMAKE_CURRENT_SOURCE_DIR}")
	message("WORKING_DIRECTORY: ${CMAKE_CURRENT_BINARY_DIR}")
	message("NAME: ${generate_usd_test_name}")
	message("COMMAND: ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/${ARG_SCRIPT} scene.rdla")
        
    set(ARG_INPUTS ${CMAKE_CURRENT_BINARY_DIR}/scene.rdla)

	# override the INPUTS argument to be "foo.rdla"
	add_rats_test(
        # options
		#DIFF_HEADERS ${ARG_DIFF_HEADERS}
		#DISABLED ${ARG_DISABLED}
		#DISABLED_SCALAR ${ARG_DISABLED_SCALAR}
		#DISABLED_VECTOR ${ARG_DISABLED_VECTOR}
		#DISABLED_XPU ${ARG_DISABLED_XPU}
		#NO_SCALAR ${ARG_NO_SCALAR}
		#NO_VECTOR ${ARG_NO_VECTOR}
		#NO_XPU ${ARG_NO_XPU}
		#NO_IMAGE_DIFF ${ARG_NO_IMAGE_DIFF}

        # oneValueArgs
		#NAME_SUFFIX ${ARG_NAME_SUFFIX}
		#OUTPUT ${ARG_OUTPUT}
		#RENDERER ${ARG_RENDERER}

        # multiValueArgs
        CANONICALS ${ARG_CANONICALS}
		#DEPENDS "${ARG_DEPENDS}"
        INPUTS ${ARG_INPUTS}
		#DELTAS "${ARG_DELTAS}"
		#ENVIRONMENT "${ARG_ENVIRONMENT}"
		#RENDER_ARGS ${ARG_RENDER_ARGS}
		#RENDER_ARGS_SCALAR ${ARG_RENDER_ARGS_SCALAR}
		#RENDER_ARGS_VECTOR ${ARG_RENDER_ARGS_VECTOR}
		#RENDER_ARGS_XPU ${ARG_RENDER_ARGS_XPU}
    )

endfunction()

message("PatsTest.cmake loaded")
