# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.916421

import typing

from ..styxdefs import *


LABEL_RESAMPLE_METADATA = Metadata(
    id="9cf69c56efa624132b8c5082081675d14da366fa",
    name="label-resample",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class LabelResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_resample(...)`.
    """
    label_out: OutputPathType
    """the output label file"""


def label_resample(
    runner: Runner,
    label_in: InputPathType,
    current_sphere: InputPathType,
    new_sphere: InputPathType,
    method: str,
    label_out: InputPathType,
    opt_current_roi_roi_metric: InputPathType | None = None,
    opt_valid_roi_out: bool = False,
    opt_largest: bool = False,
    opt_bypass_sphere_check: bool = False,
) -> LabelResampleOutputs:
    """
    RESAMPLE A LABEL FILE TO A DIFFERENT MESH.
    
    Resamples a label file, given two spherical surfaces that are in register.
    If ADAP_BARY_AREA is used, exactly one of -area-surfs or -area-metrics must
    be specified.
    
    The ADAP_BARY_AREA method is recommended for label data, because it should
    be better at resolving vertices that are near multiple labels, or in case of
    downsampling. Midthickness surfaces are recommended for the vertex areas for
    most data.
    
    The -largest option results in nearest vertex behavior when used with
    BARYCENTRIC, as it uses the value of the source vertex that has the largest
    weight.
    
    When -largest is not specified, the vertex weights are summed according to
    which label they correspond to, and the label with the largest sum is used.
    
    The <method> argument must be one of the following:
    
    ADAP_BARY_AREA
    BARYCENTRIC
    
    Args:
        runner: Command runner
        label_in: the label file to resample
        current_sphere: a sphere surface with the mesh that the label file is
            currently on
        new_sphere: a sphere surface that is in register with <current-sphere>
            and has the desired output mesh
        method: the method name
        label_out: the output label file
        opt_current_roi_roi_metric: use an input roi on the current mesh to
            exclude non-data vertices: the roi, as a metric file
        opt_valid_roi_out: output the ROI of vertices that got data from valid
            source vertices
        opt_largest: use only the label of the vertex with the largest weight
        opt_bypass_sphere_check: ADVANCED: allow the current and new 'spheres'
            to have arbitrary shape as long as they follow the same contour
    Returns:
        NamedTuple of outputs (described in `LabelResampleOutputs`).
    """
    execution = runner.start_execution(LABEL_RESAMPLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-label-resample")
    cargs.append(execution.input_file(label_in))
    cargs.append(execution.input_file(current_sphere))
    cargs.append(execution.input_file(new_sphere))
    cargs.append(method)
    cargs.append(execution.input_file(label_out))
    if opt_current_roi_roi_metric is not None:
        cargs.extend(["-current-roi", execution.input_file(opt_current_roi_roi_metric)])
    if opt_valid_roi_out:
        cargs.append("-valid-roi-out")
    if opt_largest:
        cargs.append("-largest")
    if opt_bypass_sphere_check:
        cargs.append("-bypass-sphere-check")
    ret = LabelResampleOutputs(
        label_out=execution.output_file(f"{label_out}"),
    )
    execution.run(cargs)
    return ret