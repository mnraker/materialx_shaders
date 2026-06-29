# Copyright 2025 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

add_pats_test(
    SCRIPT Test_distance.py
    CANONICALS scene.exr
    RENDER_ARGS -size 800 800
)
