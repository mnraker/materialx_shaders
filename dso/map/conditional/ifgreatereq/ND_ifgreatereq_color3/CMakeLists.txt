# Copyright 2025 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

moonray_ispc_dso(ND_ifgreatereq_color3
DEPENDENCIES
    MaterialxShaders::moonray_mtlx_map
    Moonray::common_mcrt_macros
    Moonray::rendering_shading
    Moonray::shading_ispc
    SceneRdl2::render_util)
