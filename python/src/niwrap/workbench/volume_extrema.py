# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


VOLUME_EXTREMA_METADATA = Metadata(
    id="e38cc856aefe646a1058c83142367371227ac117",
    name="volume-extrema",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VolumeExtremaPresmoothOutputs(typing.NamedTuple):
    """
    Output object returned when calling `VolumeExtremaPresmooth.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class VolumeExtremaPresmooth:
    """
    smooth the volume before finding extrema
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
    ) -> VolumeExtremaPresmoothOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `VolumeExtremaPresmoothOutputs`).
        """
        ret = VolumeExtremaPresmoothOutputs(
            root=execution.output_file("."),
        )
        return ret


class VolumeExtremaThresholdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `VolumeExtremaThreshold.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class VolumeExtremaThreshold:
    """
    ignore small extrema
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
    ) -> VolumeExtremaThresholdOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `VolumeExtremaThresholdOutputs`).
        """
        ret = VolumeExtremaThresholdOutputs(
            root=execution.output_file("."),
        )
        return ret


class VolumeExtremaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_extrema(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output extrema volume"""
    presmooth: VolumeExtremaPresmoothOutputs
    """Subcommand outputs"""
    threshold: VolumeExtremaThresholdOutputs
    """Subcommand outputs"""


def volume_extrema(
    volume_in: InputPathType,
    distance: float | int,
    volume_out: InputPathType,
    presmooth: VolumeExtremaPresmooth | None = None,
    opt_roi_roi_volume: InputPathType | None = None,
    threshold: VolumeExtremaThreshold | None = None,
    opt_sum_subvols: bool = False,
    opt_consolidate_mode: bool = False,
    opt_only_maxima: bool = False,
    opt_only_minima: bool = False,
    opt_subvolume_subvolume: str | None = None,
    runner: Runner = None,
) -> VolumeExtremaOutputs:
    """
    volume-extrema by Washington University School of Medicin.
    
    Find extrema in a volume file.
    
    Finds extrema in a volume file, such that no two extrema of the same type
    are within <distance> of each other. The extrema are labeled as -1 for
    minima, 1 for maxima, 0 otherwise. If -only-maxima or -only-minima is
    specified, then it will ignore extrema not of the specified type. These
    options are mutually exclusive.
    
    If -sum-subvols is specified, these extrema subvolumes are summed, and the
    output has a single subvolume with this result.
    
    By default, a datapoint is an extrema only if it is more extreme than every
    other datapoint that is within <distance> from it. If -consolidate-mode is
    used, it instead starts by finding all datapoints that are more extreme than
    their immediate neighbors, then while there are any extrema within
    <distance> of each other, take the two extrema closest to each other and
    merge them into one by a weighted average based on how many original extrema
    have been merged into each.
    
    By default, all input subvolumes are used with no smoothing, use -subvolume
    to specify a single subvolume to use, and -presmooth to smooth the input
    before finding the extrema.
    
    Args:
        volume_in: volume file to find the extrema of
        distance: the minimum distance between identified extrema of the same
            type
        volume_out: the output extrema volume
        presmooth: smooth the volume before finding extrema
        opt_roi_roi_volume: ignore values outside the selected area: the area to
            find extrema in
        threshold: ignore small extrema
        opt_sum_subvols: output the sum of the extrema subvolumes instead of
            each subvolume separately
        opt_consolidate_mode: use consolidation of local minima instead of a
            large neighborhood
        opt_only_maxima: only find the maxima
        opt_only_minima: only find the minima
        opt_subvolume_subvolume: select a single subvolume to find extrema in:
            the subvolume number or name
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeExtremaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_EXTREMA_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-extrema")
    cargs.append(execution.input_file(volume_in))
    cargs.append(str(distance))
    cargs.append(execution.input_file(volume_out))
    if presmooth is not None:
        cargs.extend(["-presmooth", *presmooth.run(execution)])
    if opt_roi_roi_volume is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_volume)])
    if threshold is not None:
        cargs.extend(["-threshold", *threshold.run(execution)])
    if opt_sum_subvols:
        cargs.append("-sum-subvols")
    if opt_consolidate_mode:
        cargs.append("-consolidate-mode")
    if opt_only_maxima:
        cargs.append("-only-maxima")
    if opt_only_minima:
        cargs.append("-only-minima")
    if opt_subvolume_subvolume is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvolume])
    ret = VolumeExtremaOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).name}"),
        presmooth=presmooth.outputs(execution),
        threshold=threshold.outputs(execution),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_EXTREMA_METADATA",
    "VolumeExtremaOutputs",
    "VolumeExtremaPresmooth",
    "VolumeExtremaPresmoothOutputs",
    "VolumeExtremaThreshold",
    "VolumeExtremaThresholdOutputs",
    "volume_extrema",
]
