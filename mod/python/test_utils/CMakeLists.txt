# Copyright 2026 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

set(python_install_dir python/lib/python${Python_VERSION_MAJOR}.${Python_VERSION_MINOR}/${PACKAGE_NAME})

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/test_utils.py DESTINATION ${python_install_dir})
