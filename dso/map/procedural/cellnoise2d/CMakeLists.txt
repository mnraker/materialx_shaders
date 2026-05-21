# Copyright 2025 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

moonray_ispc_dso(ND_cellnoise2d_float
DEPENDENCIES
    Moonray::common_mcrt_macros
    Moonray::common_noise
    Moonray::rendering_shading
    Moonray::shading_ispc
    SceneRdl2::render_util)
