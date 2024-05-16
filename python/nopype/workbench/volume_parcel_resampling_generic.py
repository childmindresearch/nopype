# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


VOLUME_PARCEL_RESAMPLING_GENERIC_METADATA = Metadata(
    id="6efe201ba5945feedc9ac05541d9912189c179e7",
    name="volume-parcel-resampling-generic",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeParcelResamplingGenericOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_parcel_resampling_generic(...)`.
    """
    volume_out: OutputPathType
    """output volume"""


def volume_parcel_resampling_generic(
    runner: Runner,
    volume_in: InputPathType,
    cur_parcels: InputPathType,
    new_parcels: InputPathType,
    kernel: float | int,
    volume_out: InputPathType,
    opt_fwhm: bool = False,
    opt_fix_zeros: bool = False,
    opt_subvolume_subvol: str | None = None,
) -> VolumeParcelResamplingGenericOutputs:
    """
    SMOOTH AND RESAMPLE VOLUME PARCELS FROM DIFFERENT VOLUME SPACE.
    
    Smooths and resamples the region inside each label in cur-parcels to the
    region of the same label name in new-parcels. Any voxels in the output label
    region but outside the input label region will be extrapolated from nearby
    data. The -fix-zeros option causes the smoothing to not use an input value
    if it is zero, but still write a smoothed value to the voxel, and after
    smoothing is complete, it will check for any remaining values of zero, and
    fill them in with extrapolated values. The output volume will use the volume
    space of new-parcels, which does not need to be in the same volume space as
    the input.
    
    Args:
        runner: Command runner
        volume_in: the input data volume
        cur_parcels: label volume of where the parcels currently are
        new_parcels: label volume of where the parcels should be
        kernel: gaussian kernel size in mm to smooth by during resampling, as
            sigma by default
        volume_out: output volume
        opt_fwhm: smoothing kernel size is FWHM, not sigma
        opt_fix_zeros: treat zero values as not being data
        opt_subvolume_subvol: select a single subvolume as input: the subvolume
            number or name
    Returns:
        NamedTuple of outputs (described in `VolumeParcelResamplingGenericOutputs`).
    """
    execution = runner.start_execution(VOLUME_PARCEL_RESAMPLING_GENERIC_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-parcel-resampling-generic")
    cargs.append(execution.input_file(volume_in))
    cargs.append(execution.input_file(cur_parcels))
    cargs.append(execution.input_file(new_parcels))
    cargs.append(str(kernel))
    cargs.append(execution.input_file(volume_out))
    if opt_fwhm:
        cargs.append("-fwhm")
    if opt_fix_zeros:
        cargs.append("-fix-zeros")
    if opt_subvolume_subvol is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvol])
    ret = VolumeParcelResamplingGenericOutputs(
        volume_out=execution.output_file(f"{volume_out}"),
    )
    execution.run(cargs)
    return ret
