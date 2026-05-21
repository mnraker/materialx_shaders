# Copyright 2023-2025 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

moonray_ispc_dso(ND_multiply_color4FA
DEPENDENCIES
    MaterialxShaders::moonray_mtlx_map
    Moonray::common_mcrt_macros
    Moonray::rendering_shading
    Moonray::shading_ispc
    SceneRdl2::render_util)
