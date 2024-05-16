# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


VOLUME_ROIS_FROM_EXTREMA_METADATA = Metadata(
    id="91346dec57449cc125d00145a10d3e6aa9f4d27e",
    name="volume-rois-from-extrema",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeRoisFromExtremaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_rois_from_extrema(...)`.
    """
    volume_out: OutputPathType
    """the output volume"""


def volume_rois_from_extrema(
    runner: Runner,
    volume_in: InputPathType,
    limit: float | int,
    volume_out: InputPathType,
    opt_gaussian_sigma: float | int | None = None,
    opt_roi_roi_volume: InputPathType | None = None,
    opt_overlap_logic_method: str | None = None,
    opt_subvolume_subvol: str | None = None,
) -> VolumeRoisFromExtremaOutputs:
    """
    CREATE VOLUME ROI MAPS FROM EXTREMA MAPS.
    
    For each nonzero value in each map, make a map with an ROI around that
    location. If the -gaussian option is specified, then normalized gaussian
    kernels are output instead of ROIs. The <method> argument to -overlap-logic
    must be one of ALLOW, CLOSEST, or EXCLUDE. ALLOW is the default, and means
    that ROIs are treated independently and may overlap. CLOSEST means that ROIs
    may not overlap, and that no ROI contains vertices that are closer to a
    different seed vertex. EXCLUDE means that ROIs may not overlap, and that any
    vertex within range of more than one ROI does not belong to any ROI.
    
    Args:
        runner: Command runner
        volume_in: the input volume
        limit: distance limit from voxel center, in mm
        volume_out: the output volume
        opt_gaussian_sigma: generate a gaussian kernel instead of a flat ROI:
            the sigma for the gaussian kernel, in mm
        opt_roi_roi_volume: select a region of interest to use: the region to
            use
        opt_overlap_logic_method: how to handle overlapping ROIs, default ALLOW:
            the method of resolving overlaps
        opt_subvolume_subvol: select a single subvolume to take the gradient of:
            the subvolume number or name
    Returns:
        NamedTuple of outputs (described in `VolumeRoisFromExtremaOutputs`).
    """
    execution = runner.start_execution(VOLUME_ROIS_FROM_EXTREMA_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-rois-from-extrema")
    cargs.append(execution.input_file(volume_in))
    cargs.append(str(limit))
    cargs.append(execution.input_file(volume_out))
    if opt_gaussian_sigma is not None:
        cargs.extend(["-gaussian", str(opt_gaussian_sigma)])
    if opt_roi_roi_volume is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_volume)])
    if opt_overlap_logic_method is not None:
        cargs.extend(["-overlap-logic", opt_overlap_logic_method])
    if opt_subvolume_subvol is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvol])
    ret = VolumeRoisFromExtremaOutputs(
        volume_out=execution.output_file(f"{volume_out}"),
    )
    execution.run(cargs)
    return ret
