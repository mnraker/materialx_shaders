# Copyright 2025 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

moonray_ispc_dso(ND_randomcolor_integer
DEPENDENCIES
    MaterialxShaders::moonray_mtlx_map
    Moonray::common_mcrt_macros
    Moonray::common_noise
    Moonray::rendering_shading
    Moonray::shading_ispc
    SceneRdl2::render_util)
