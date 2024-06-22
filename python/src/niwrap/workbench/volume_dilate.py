# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

VOLUME_DILATE_METADATA = Metadata(
    id="e512d11a4fe60b0e9589139cea8a9f67f23cde02",
    name="volume-dilate",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class VolumeDilatePresmooth:
    """
    apply presmoothing before computing gradient vectors, not recommended
    """
    kernel: float | int
    """the size of gaussian smoothing kernel in mm, as sigma by default"""
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
        cargs.append("-presmooth")
        cargs.append(str(self.kernel))
        if self.opt_fwhm:
            cargs.append("-fwhm")
        return cargs


class VolumeDilateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_dilate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_dilate(
    volume: InputPathType,
    distance: float | int,
    method: str,
    volume_out: InputPathType,
    opt_exponent_exponent: float | int | None = None,
    opt_bad_voxel_roi_roi_volume: InputPathType | None = None,
    opt_data_roi_roi_volume: InputPathType | None = None,
    opt_subvolume_subvol: str | None = None,
    opt_legacy_cutoff: bool = False,
    opt_grad_extrapolate: bool = False,
    presmooth: VolumeDilatePresmooth | None = None,
    runner: Runner = None,
) -> VolumeDilateOutputs:
    """
    volume-dilate by Washington University School of Medicin.
    
    Dilate a volume file.
    
    For all voxels that are designated as bad, if they neighbor a non-bad voxel
    with data or are within the specified distance of such a voxel, replace the
    value in the bad voxel with a value calculated from nearby non-bad voxels
    that have data, otherwise set the value to zero. No matter how small
    <distance> is, dilation will always use at least the face neighbor voxels.
    
    By default, voxels that have data with the value 0 are bad, specify
    -bad-voxel-roi to only count voxels as bad if they are selected by the roi.
    If -data-roi is not specified, all voxels are assumed to have data.
    
    To get the behavior of version 1.3.2 or earlier, use '-legacy-cutoff
    -exponent 2'.
    
    Valid values for <method> are:
    
    NEAREST - use the value from the nearest good voxel
    WEIGHTED - use a weighted average based on distance.
    
    Args:
        volume: the volume to dilate.
        distance: distance in mm to dilate.
        method: dilation method to use.
        volume_out: the output volume.
        opt_exponent_exponent: use a different exponent in the weighting\
            function: exponent 'n' to use in (1 / (distance ^ n)) as the weighting\
            function (default 7).
        opt_bad_voxel_roi_roi_volume: specify an roi of voxels to overwrite,\
            rather than voxels with value zero: volume file, positive values denote\
            voxels to have their values replaced.
        opt_data_roi_roi_volume: specify an roi of where there is data: volume\
            file, positive values denote voxels that have data.
        opt_subvolume_subvol: select a single subvolume to dilate: the\
            subvolume number or name.
        opt_legacy_cutoff: use the v1.3.2 method of excluding voxels further\
            than the dilation distance when calculating the dilated value.
        opt_grad_extrapolate: additionally use the gradient to extrapolate,\
            intended to be used with WEIGHTED.
        presmooth: apply presmoothing before computing gradient vectors, not\
            recommended.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeDilateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_DILATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-dilate")
    cargs.append(execution.input_file(volume))
    cargs.append(str(distance))
    cargs.append(method)
    cargs.append(execution.input_file(volume_out))
    if opt_exponent_exponent is not None:
        cargs.extend(["-exponent", str(opt_exponent_exponent)])
    if opt_bad_voxel_roi_roi_volume is not None:
        cargs.extend(["-bad-voxel-roi", execution.input_file(opt_bad_voxel_roi_roi_volume)])
    if opt_data_roi_roi_volume is not None:
        cargs.extend(["-data-roi", execution.input_file(opt_data_roi_roi_volume)])
    if opt_subvolume_subvol is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvol])
    if opt_legacy_cutoff:
        cargs.append("-legacy-cutoff")
    if opt_grad_extrapolate:
        cargs.append("-grad-extrapolate")
    if presmooth is not None:
        cargs.extend(presmooth.run(execution))
    ret = VolumeDilateOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_DILATE_METADATA",
    "VolumeDilateOutputs",
    "VolumeDilatePresmooth",
    "volume_dilate",
]
