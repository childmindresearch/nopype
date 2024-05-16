# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.877458

import typing

from ..styxdefs import *


SURFACE_CLOSEST_VERTEX_METADATA = Metadata(
    id="464fdcd54c3d5f63c79bdb5ebe8a0b3efb447891",
    name="surface-closest-vertex",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceClosestVertexOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_closest_vertex(...)`.
    """


def surface_closest_vertex(
    runner: Runner,
    surface: InputPathType,
    coord_list_file: str,
    vertex_list_out: str,
) -> SurfaceClosestVertexOutputs:
    """
    FIND CLOSEST SURFACE VERTEX TO COORDINATES.
    
    For each coordinate XYZ triple, find the closest vertex in the surface, and
    output its vertex number into a text file. The input file should only use
    whitespace to separate coordinates (spaces, newlines, tabs), for instance:
    
    20 30 25
    30 -20 10
    
    Args:
        runner: Command runner
        surface: the surface to use
        coord_list_file: text file with coordinates
        vertex_list_out: output - the output text file with vertex numbers
    Returns:
        NamedTuple of outputs (described in `SurfaceClosestVertexOutputs`).
    """
    execution = runner.start_execution(SURFACE_CLOSEST_VERTEX_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-closest-vertex")
    cargs.append(execution.input_file(surface))
    cargs.append(coord_list_file)
    cargs.append(vertex_list_out)
    ret = SurfaceClosestVertexOutputs(
    )
    execution.run(cargs)
    return ret