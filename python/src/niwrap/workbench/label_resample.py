# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


LABEL_RESAMPLE_METADATA = Metadata(
    id="62135c374b3b1838f951fa32fe0a90d64343e9a8",
    name="label-resample",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class LabelResampleAreaSurfsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `LabelResampleAreaSurfs.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class LabelResampleAreaSurfs:
    """
    specify surfaces to do vertex area correction based on
    """
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> LabelResampleAreaSurfsOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `LabelResampleAreaSurfsOutputs`).
        """
        ret = LabelResampleAreaSurfsOutputs(
            root=execution.output_file("."),
        )
        return ret


class LabelResampleAreaMetricsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `LabelResampleAreaMetrics.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class LabelResampleAreaMetrics:
    """
    specify vertex area metrics to do area correction based on
    """
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> LabelResampleAreaMetricsOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `LabelResampleAreaMetricsOutputs`).
        """
        ret = LabelResampleAreaMetricsOutputs(
            root=execution.output_file("."),
        )
        return ret


class LabelResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """the output label file"""
    roi_out: OutputPathType
    """the output roi as a metric"""
    area_surfs: LabelResampleAreaSurfsOutputs
    """Subcommand outputs"""
    area_metrics: LabelResampleAreaMetricsOutputs
    """Subcommand outputs"""


def label_resample(
    label_in: InputPathType,
    current_sphere: InputPathType,
    new_sphere: InputPathType,
    method: str,
    label_out: InputPathType,
    roi_out: InputPathType,
    area_surfs: LabelResampleAreaSurfs | None = None,
    area_metrics: LabelResampleAreaMetrics | None = None,
    opt_current_roi_roi_metric: InputPathType | None = None,
    opt_valid_roi_out: bool = False,
    opt_largest: bool = False,
    opt_bypass_sphere_check: bool = False,
    runner: Runner = None,
) -> LabelResampleOutputs:
    """
    label-resample by Washington University School of Medicin.
    
    Resample a label file to a different mesh.
    
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
    .
    
    Args:
        label_in: the label file to resample
        current_sphere: a sphere surface with the mesh that the label file is
            currently on
        new_sphere: a sphere surface that is in register with <current-sphere>
            and has the desired output mesh
        method: the method name
        label_out: the output label file
        roi_out: the output roi as a metric
        area_surfs: specify surfaces to do vertex area correction based on
        area_metrics: specify vertex area metrics to do area correction based on
        opt_current_roi_roi_metric: use an input roi on the current mesh to
            exclude non-data vertices: the roi, as a metric file
        opt_valid_roi_out: output the ROI of vertices that got data from valid
            source vertices
        opt_largest: use only the label of the vertex with the largest weight
        opt_bypass_sphere_check: ADVANCED: allow the current and new 'spheres'
            to have arbitrary shape as long as they follow the same contour
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `LabelResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_RESAMPLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-label-resample")
    cargs.append(execution.input_file(label_in))
    cargs.append(execution.input_file(current_sphere))
    cargs.append(execution.input_file(new_sphere))
    cargs.append(method)
    cargs.append(execution.input_file(label_out))
    if area_surfs is not None:
        cargs.extend(["-area-surfs", *area_surfs.run(execution)])
    if area_metrics is not None:
        cargs.extend(["-area-metrics", *area_metrics.run(execution)])
    if opt_current_roi_roi_metric is not None:
        cargs.extend(["-current-roi", execution.input_file(opt_current_roi_roi_metric)])
    if opt_valid_roi_out:
        cargs.append("-valid-roi-out")
    cargs.append(execution.input_file(roi_out))
    if opt_largest:
        cargs.append("-largest")
    if opt_bypass_sphere_check:
        cargs.append("-bypass-sphere-check")
    ret = LabelResampleOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(f"{pathlib.Path(label_out).name}"),
        roi_out=execution.output_file(f"{pathlib.Path(roi_out).name}"),
        area_surfs=area_surfs.outputs(execution),
        area_metrics=area_metrics.outputs(execution),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LABEL_RESAMPLE_METADATA",
    "LabelResampleAreaMetrics",
    "LabelResampleAreaMetricsOutputs",
    "LabelResampleAreaSurfs",
    "LabelResampleAreaSurfsOutputs",
    "LabelResampleOutputs",
    "label_resample",
]
