# SPDX-License-Identifier: Apache-2.0
# Copyright Contributors to the Moonray Project

function(${PROJECT_NAME}_cxx_compile_options target)
    if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
        target_compile_options(${target}
            PRIVATE
                $<$<BOOL:${ABI_SET_VERSION}>:
                    -fabi-version=${ABI_VERSION} # corrects the promotion behavior of C++11 scoped enums and the mangling of template argument packs.
                >
                -fexceptions                    # Enable exception handling.
                -fno-omit-frame-pointer         # TODO: add a note
                -fno-strict-aliasing            # TODO: add a note
                -fno-var-tracking-assignments   # Turn off variable tracking
                -fpermissive                    # Downgrade some diagnostics about nonconformant code from errors to warnings.
                -march=core-avx2                # Specify the name of the target architecture
                -mavx                           # x86 options
                -pipe                           # Use pipes rather than intermediate files.
                -pthread                        # Define additional macros required for using the POSIX threads library.
                -w                              # Inhibit all warning messages.
                -Wall                           # Enable most warning messages.
                -Wcast-align                    # Warn about pointer casts which increase alignment.
                -Wcast-qual                     # Warn about casts which discard qualifiers.
                -Wdisabled-optimization         # Warn when an optimization pass is disabled.
                -Wextra                         # This enables some extra warning flags that are not enabled by -Wall
                -Woverloaded-virtual            # Warn about overloaded virtual function names.
                -Wno-conversion                 # Disable certain warnings that are enabled by -Wall
                -Wno-sign-compare               # Disable certain warnings that are enabled by -Wall
                -Wno-switch                     # Disable certain warnings that are enabled by -Wall
                -Wno-system-headers             # Disable certain warnings that are enabled by -Wall
                -Wno-unused-parameter           # Disable certain warnings that are enabled by -Wall

                $<$<CONFIG:RELWITHDEBINFO>:
                    -O3                         # the default is -O2 for RELWITHDEBINFO
                >
        )
    elseif (CMAKE_CXX_COMPILER_ID STREQUAL Clang)
        target_compile_options(${target}
            # TODO: Some if not all of these should probably be PUBLIC
            PRIVATE
                -march=core-avx2                # Specify the name of the target architecture
                -fdelayed-template-parsing      # Shader.h has a template method that uses a moonray class which is no available to scene_rdl2 and is only used in moonray+
                -Wno-deprecated-declarations    # disable auto_ptr deprecated warnings from log4cplus-1.
                -Wno-unused-value               # caused by opt-debug build and MNRY_VERIFY.
                -Wno-switch                     # Disable certain warnings that are enabled by -Wall
                -Wno-uninitialized              # Disable warning for Interpolater
                -Wno-register                   # Flex uses deprecated register keyword
        )
    elseif (CMAKE_CXX_COMPILER_ID STREQUAL Intel)
        target_compile_options(${target}
            # TODO: Some if not all of these should probably be PUBLIC
            PRIVATE
                -march=core-avx2                # Specify the name of the target architecture
                -mavx
                -Qoption,cpp,--print_include_stack
                -fmerge-debug-strings
                -fexceptions                    # Enable exception handling.
                -fno-strict-aliasing            # TODO: add a note
                -pthread
                -restrict
        )
    endif()
endfunction()

# ISPC compiler
function(${PROJECT_NAME}_ispc_compile_options target)
    set(commonOptions
	${GLOBAL_ISPC_FLAGS}
        --opt=force-aligned-memory          # always issue "aligned" vector load and store instructions
        --pic                               # Generate position-independent code.  Ignored for Windows target
        #--werror                            # Treat warnings as errors
        --wno-perf                          # Don't issue warnings related to performance-related issues
    )
    set_property(TARGET ${target}
                 PROPERTY TARGET_OBJECTS $<TARGET_OBJECTS:${target}>)
    set_property(TARGET ${target}
                 PROPERTY DEPENDENCY "")
    check_language(ISPC)
    if(NOT CMAKE_ISPC_COMPILER OR IsWindowsPlatform)
        get_target_property(SOURCES ${target} SOURCES)
        get_target_property(ISPC_HEADER_SUFFIX ${target} ISPC_HEADER_SUFFIX)
        get_target_property(ISPC_HEADER_DIRECTORY ${target} ISPC_HEADER_DIRECTORY)
        get_target_property(ISPC_INSTRUCTION_SETS ${target} ISPC_INSTRUCTION_SETS)
        get_target_property(ISPC_ARCH ${target} ISPC_ARCH)
        get_target_property(ISPC_TARGET_OS ${target} ISPC_TARGET_OS)

        set(configDepFlags "")
        if (CMAKE_BUILD_TYPE STREQUAL "Debug")
            set(configDepFlags
                    -g                              # emit debug info
                    --dwarf-version=2               # use DWARF version 2 for debug symbols
                )
        elseif (CMAKE_BUILD_TYPE STREQUAL "RelWithDebInfo")
            set(configDepFlags
                    -g                              # emit debug info
                    -O3                             # the default is -O2 for RELWITHDEBINFO
                    --dwarf-version=2               # use DWARF version 2 for debug symbols
                    --opt=disable-assertions        # disable all of the assertions
                )
        elseif (CMAKE_BUILD_TYPE STREQUAL "Release")
            set(configDepFlags
                    --opt=disable-assertions        # disable all of the assertions
                )
        endif()

        foreach(src ${SOURCES})
            get_filename_component(srcExt ${src} LAST_EXT)

            if (NOT srcExt STREQUAL ".ispc")
                continue()
            endif()

            get_filename_component(srcName ${src} NAME_WE)
            
        set(objOut "${CMAKE_CURRENT_BINARY_DIR}/${srcName}.o")
        set(depFile "${CMAKE_CURRENT_BINARY_DIR}/${srcName}.dep")

        if(IsWindowsPlatform)
            set(depArgs "")
            set(depFileArg "")
            set(ispcArch ${ISPC_ARCH})
            set(ispcTargetOs ${ISPC_TARGET_OS})
        else()
            set(depArgs -M -MF ${depFile})
            set(depFileArg DEPFILE ${depFile})
            set(ispcArch aarch64)
            set(ispcTargetOs macos)
        endif()

        set(headerOut "${ISPC_HEADER_DIRECTORY}/${srcName}${ISPC_HEADER_SUFFIX}")
        if(IS_ABSOLUTE "${headerOut}")
            set(headerArg "${headerOut}")
        else()
            set(headerArg "./${headerOut}")
        endif()

        add_custom_command(
            OUTPUT ${objOut}
            COMMAND ${ISPC_COMPILER} ${CMAKE_CURRENT_SOURCE_DIR}/${src}
                -o ${objOut}
                -h ${headerArg}
                ${depArgs}
                --arch=${ispcArch}
                --target=${ISPC_INSTRUCTION_SETS}
                --target-os=${ispcTargetOs}
                ${commonOptions}
                ${configDepFlags}
                "-I$<JOIN:$<TARGET_PROPERTY:${target},INCLUDE_DIRECTORIES>,;-I>"
            WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
            COMMAND_EXPAND_LISTS
            VERBATIM
            ${depFileArg}
            DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/${src})
        list(APPEND ISPC_TARGET_OBJECTS ${objOut})
        endforeach()
        target_link_libraries(${target}
                PRIVATE ${ISPC_TARGET_OBJECTS})
    if(IsWindowsPlatform)
        target_sources(${target}
            PRIVATE ${ISPC_TARGET_OBJECTS})
    endif()
        add_custom_target(${target}_ispc_dep DEPENDS ${ISPC_TARGET_OBJECTS})
        add_dependencies(${target} ${target}_ispc_dep)
        set_property(TARGET ${target}
                 PROPERTY DEPENDENCY ${target}_ispc_dep)
        set_property(
                TARGET ${target}
                PROPERTY
                    TARGET_OBJECTS ${ISPC_TARGET_OBJECTS})
    else ()
        target_compile_options(${target}
            PRIVATE
                ${commonOptions}    
                $<$<CONFIG:DEBUG>:
                    --dwarf-version=2               # use DWARF version 2 for debug symbols
                >
    
                $<$<CONFIG:RELWITHDEBINFO>:
                    -O3                             # the default is -O2 for RELWITHDEBINFO
                    --dwarf-version=2               # use DWARF version 2 for debug symbols
                    --opt=disable-assertions        # disable all of the assertions
                >
    
                $<$<CONFIG:RELEASE>:
                    --opt=disable-assertions        # disable all of the assertions
                >
        )
    endif()
endfunction()
