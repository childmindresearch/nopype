# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


METRIC_GRADIENT_METADATA = Metadata(
    id="7f36ae411093e7ed8b4e554a111987e6a03a0358",
    name="metric-gradient",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class MetricGradientPresmoothOutputs(typing.NamedTuple):
    """
    Output object returned when calling `MetricGradientPresmooth.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class MetricGradientPresmooth:
    """
    smooth the metric before computing the gradient
    """
    opt_fwhm: bool = False
    """kernel size is FWHM, not sigma"""
    
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
        if self.opt_fwhm:
            cargs.append("-fwhm")
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> MetricGradientPresmoothOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `MetricGradientPresmoothOutputs`).
        """
        ret = MetricGradientPresmoothOutputs(
            root=execution.output_file("."),
        )
        return ret


class MetricGradientRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `MetricGradientRoi.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class MetricGradientRoi:
    """
    select a region of interest to take the gradient of
    """
    opt_match_columns: bool = False
    """for each input column, use the corresponding column from the roi"""
    
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
        if self.opt_match_columns:
            cargs.append("-match-columns")
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> MetricGradientRoiOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `MetricGradientRoiOutputs`).
        """
        ret = MetricGradientRoiOutputs(
            root=execution.output_file("."),
        )
        return ret


class MetricGradientOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_gradient(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the magnitude of the gradient"""
    vector_metric_out: OutputPathType
    """the vectors as a metric file"""
    presmooth: MetricGradientPresmoothOutputs
    """Subcommand outputs"""
    roi: MetricGradientRoiOutputs
    """Subcommand outputs"""


def metric_gradient(
    surface: InputPathType,
    metric_in: InputPathType,
    metric_out: InputPathType,
    vector_metric_out: InputPathType,
    presmooth: MetricGradientPresmooth | None = None,
    roi: MetricGradientRoi | None = None,
    opt_vectors: bool = False,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    opt_average_normals: bool = False,
    runner: Runner = None,
) -> MetricGradientOutputs:
    """
    metric-gradient by Washington University School of Medicin.
    
    Surface gradient of a metric file.
    
    At each vertex, the immediate neighbors are unfolded onto a plane tangent to
    the surface at the vertex (specifically, perpendicular to the normal). The
    gradient is computed using a regression between the unfolded positions of
    the vertices and their values. The gradient is then given by the slopes of
    the regression, and reconstructed as a 3D gradient vector. By default, takes
    the gradient of all columns, with no presmoothing, across the whole surface,
    without averaging the normals of the surface among neighbors.
    
    When using -corrected-areas, note that it is an approximate correction.
    Doing smoothing on individual surfaces before averaging/gradient is
    preferred, when possible, in order to make use of the original surface
    structure.
    
    Specifying an ROI will restrict the gradient to only use data from where the
    ROI metric is positive, and output zeros anywhere the ROI metric is not
    positive.
    
    By default, the first column of the roi metric is used for all input
    columns. When -match-columns is specified to the -roi option, the input and
    roi metrics must have the same number of columns, and for each input
    column's index, the same column index is used in the roi metric. If the
    -match-columns option to -roi is used while the -column option is also used,
    the number of columns of the roi metric must match the input metric, and it
    will use the roi column with the index of the selected input column.
    
    The vector output metric is organized such that the X, Y, and Z components
    from a single input column are consecutive columns.
    
    Args:
        surface: the surface to compute the gradient on
        metric_in: the metric to compute the gradient of
        metric_out: the magnitude of the gradient
        vector_metric_out: the vectors as a metric file
        presmooth: smooth the metric before computing the gradient
        roi: select a region of interest to take the gradient of
        opt_vectors: output gradient vectors
        opt_column_column: select a single column to compute the gradient of:
            the column number or name
        opt_corrected_areas_area_metric: vertex areas to use instead of
            computing them from the surface: the corrected vertex areas, as a metric
        opt_average_normals: average the normals of each vertex with its
            neighbors before using them to compute the gradient
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MetricGradientOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_GRADIENT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-gradient")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_in))
    cargs.append(execution.input_file(metric_out))
    if presmooth is not None:
        cargs.extend(["-presmooth", *presmooth.run(execution)])
    if roi is not None:
        cargs.extend(["-roi", *roi.run(execution)])
    if opt_vectors:
        cargs.append("-vectors")
    cargs.append(execution.input_file(vector_metric_out))
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    if opt_average_normals:
        cargs.append("-average-normals")
    ret = MetricGradientOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{pathlib.Path(metric_out).name}"),
        vector_metric_out=execution.output_file(f"{pathlib.Path(vector_metric_out).name}"),
        presmooth=presmooth.outputs(execution),
        roi=roi.outputs(execution),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_GRADIENT_METADATA",
    "MetricGradientOutputs",
    "MetricGradientPresmooth",
    "MetricGradientPresmoothOutputs",
    "MetricGradientRoi",
    "MetricGradientRoiOutputs",
    "metric_gradient",
]
