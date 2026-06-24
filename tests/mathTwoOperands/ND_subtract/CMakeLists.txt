# Copyright 2025 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

# Tests camera stereo left view with dof.

add_pats_test(
    SCRIPT Test_ND_subtract.py
    CANONICALS scene.exr
    RENDER_ARGS -size 600 800
)
