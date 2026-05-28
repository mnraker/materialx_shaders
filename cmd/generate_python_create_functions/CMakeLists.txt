# Copyright 2023-2026 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

set(target generate_python_create_functions)

add_executable(${target}
    generate_python_create_functions
)

install (TARGETS ${target}
    RUNTIME DESTINATION bin)
