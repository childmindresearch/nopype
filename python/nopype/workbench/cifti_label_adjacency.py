# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


CIFTI_LABEL_ADJACENCY_METADATA = Metadata(
    id="56efde38de95f4b8adc1fb8f95f69d9cfafe9b24",
    name="cifti-label-adjacency",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiLabelAdjacencyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_label_adjacency(...)`.
    """
    adjacency_out: OutputPathType
    """the output cifti pconn adjacency matrix"""


def cifti_label_adjacency(
    runner: Runner,
    label_in: InputPathType,
    adjacency_out: InputPathType,
    opt_left_surface_surface: InputPathType | None = None,
    opt_right_surface_surface: InputPathType | None = None,
    opt_cerebellum_surface_surface: InputPathType | None = None,
) -> CiftiLabelAdjacencyOutputs:
    """
    MAKE ADJACENCY MATRIX OF A CIFTI LABEL FILE.
    
    Find face-adjacent voxels and connected vertices that have different label
    values, and count them for each pair. Put the resulting counts into a
    parcellated connectivity file, with the diagonal being zero. This gives a
    rough estimate of how long or expansive the border between two labels is.
    
    Args:
        runner: Command runner
        label_in: the input cifti label file
        adjacency_out: the output cifti pconn adjacency matrix
        opt_left_surface_surface: specify the left surface to use: the left
            surface file
        opt_right_surface_surface: specify the right surface to use: the right
            surface file
        opt_cerebellum_surface_surface: specify the cerebellum surface to use:
            the cerebellum surface file
    Returns:
        NamedTuple of outputs (described in `CiftiLabelAdjacencyOutputs`).
    """
    execution = runner.start_execution(CIFTI_LABEL_ADJACENCY_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-label-adjacency")
    cargs.append(execution.input_file(label_in))
    cargs.append(execution.input_file(adjacency_out))
    if opt_left_surface_surface is not None:
        cargs.extend(["-left-surface", execution.input_file(opt_left_surface_surface)])
    if opt_right_surface_surface is not None:
        cargs.extend(["-right-surface", execution.input_file(opt_right_surface_surface)])
    if opt_cerebellum_surface_surface is not None:
        cargs.extend(["-cerebellum-surface", execution.input_file(opt_cerebellum_surface_surface)])
    ret = CiftiLabelAdjacencyOutputs(
        adjacency_out=execution.output_file(f"{adjacency_out}"),
    )
    execution.run(cargs)
    return ret
