# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


SURFACE_GEODESIC_DISTANCE_ALL_TO_ALL_METADATA = Metadata(
    id="7ce999198356b35719cc8f74450182fa893e69d4",
    name="surface-geodesic-distance-all-to-all",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceGeodesicDistanceAllToAllOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_geodesic_distance_all_to_all(...)`.
    """
    cifti_out: OutputPathType
    """single-hemisphere dconn containing the distances"""


def surface_geodesic_distance_all_to_all(
    runner: Runner,
    surface: InputPathType,
    cifti_out: InputPathType,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_limit_limit_mm: float | int | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    opt_naive: bool = False,
) -> SurfaceGeodesicDistanceAllToAllOutputs:
    """
    COMPUTE GEODESIC DISTANCES FROM ALL VERTICES.
    
    Computes geodesic distance from every vertex to every vertex, outputting a
    single-hemisphere dconn file. If you are only interested in a few vertices,
    see -surface-geodesic-distance. When -limit is specified, any vertex beyond
    the limit is assigned the value -1.
    
    The -roi option makes the output file smaller by not outputting distances to
    or from vertices outside the ROI, but paths are still allowed to go outside
    the ROI when finding distances to other vertices.
    
    The -corrected-areas option should be used when the input is a group average
    surface - group average surfaces have significantly less surface area than
    individual surfaces do, and therefore distances measured on them would be
    smaller than measuring them on individual surfaces. In this case, the input
    to this option should be a group average of the output of
    -surface-vertex-areas for each subject.
    
    If -naive is not specified, the algorithm uses not just immediate neighbors,
    but also neighbors derived from crawling across pairs of triangles that
    share an edge.
    
    Args:
        runner: Command runner
        surface: the surface to compute on
        cifti_out: single-hemisphere dconn containing the distances
        opt_roi_roi_metric: only output distances for vertices inside an ROI:
            the ROI as a metric file
        opt_limit_limit_mm: stop at a specified distance: distance in mm to stop
            at
        opt_corrected_areas_area_metric: vertex areas to use instead of
            computing them from the surface: the corrected vertex areas, as a metric
        opt_naive: use only neighbors, don't crawl triangles (not recommended)
    Returns:
        NamedTuple of outputs (described in `SurfaceGeodesicDistanceAllToAllOutputs`).
    """
    execution = runner.start_execution(SURFACE_GEODESIC_DISTANCE_ALL_TO_ALL_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-geodesic-distance-all-to-all")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(cifti_out))
    if opt_roi_roi_metric is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_metric)])
    if opt_limit_limit_mm is not None:
        cargs.extend(["-limit", str(opt_limit_limit_mm)])
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    if opt_naive:
        cargs.append("-naive")
    ret = SurfaceGeodesicDistanceAllToAllOutputs(
        cifti_out=execution.output_file(f"{cifti_out}"),
    )
    execution.run(cargs)
    return ret
