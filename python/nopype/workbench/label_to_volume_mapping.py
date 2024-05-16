# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


LABEL_TO_VOLUME_MAPPING_METADATA = Metadata(
    id="de1743a3cb37fd1cfbf7d407339dda1f78786770",
    name="label-to-volume-mapping",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class LabelToVolumeMappingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_to_volume_mapping(...)`.
    """
    volume_out: OutputPathType
    """the output volume file"""


def label_to_volume_mapping(
    runner: Runner,
    label: InputPathType,
    surface: InputPathType,
    volume_space: InputPathType,
    volume_out: InputPathType,
    opt_nearest_vertex_distance: float | int | None = None,
) -> LabelToVolumeMappingOutputs:
    """
    MAP LABEL FILE TO VOLUME.
    
    Maps labels from a gifti label file into a volume file. You must specify
    exactly one mapping method option. The -nearest-vertex method uses the label
    from the vertex closest to the voxel center. The -ribbon-constrained method
    uses the same method as in -volume-to-surface-mapping, then uses the weights
    in reverse, with popularity logic to decide on a label to use.
    
    Args:
        runner: Command runner
        label: the input label file
        surface: the surface to use coordinates from
        volume_space: a volume file in the desired output volume space
        volume_out: the output volume file
        opt_nearest_vertex_distance: use the label from the vertex closest to
            the voxel center: how far from the surface to map labels to voxels, in
            mm
    Returns:
        NamedTuple of outputs (described in `LabelToVolumeMappingOutputs`).
    """
    execution = runner.start_execution(LABEL_TO_VOLUME_MAPPING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-label-to-volume-mapping")
    cargs.append(execution.input_file(label))
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(volume_space))
    cargs.append(execution.input_file(volume_out))
    if opt_nearest_vertex_distance is not None:
        cargs.extend(["-nearest-vertex", str(opt_nearest_vertex_distance)])
    ret = LabelToVolumeMappingOutputs(
        volume_out=execution.output_file(f"{volume_out}"),
    )
    execution.run(cargs)
    return ret
