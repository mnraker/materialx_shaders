# Copyright 2023-2025 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

moonray_ispc_dso(ND_round_color3
DEPENDENCIES
    MaterialxShaders::moonray_mtlx_map
    Moonray::common_mcrt_macros
    Moonray::rendering_shading
    Moonray::shading_ispc
    SceneRdl2::render_util)
add_dependencies(all_shader_dsos ND_round_color3)
