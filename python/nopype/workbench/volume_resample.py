# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


VOLUME_RESAMPLE_METADATA = Metadata(
    id="e0cf1b4dcb6f4c5eb2afc4fdf77142917613c127",
    name="volume-resample",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_resample(...)`.
    """
    volume_out: OutputPathType
    """the output volume"""


def volume_resample(
    runner: Runner,
    volume_in: InputPathType,
    volume_space: str,
    method: str,
    volume_out: InputPathType,
    opt_affine_affine: str | None = None,
    opt_affine_series_affine_series: str | None = None,
    opt_warp_warpfield: str | None = None,
) -> VolumeResampleOutputs:
    """
    TRANSFORM AND RESAMPLE A VOLUME FILE.
    
    Resample a volume file with an arbitrary list of transformations. You may
    specify -affine, -warp, and -affine-series multiple times each, and they
    will be used in the order specified. For instance, for rigid motion
    correction followed by nonlinear atlas registration, specify -affine-series
    first, then -warp. The recommended methods are CUBIC (cubic spline) for most
    data, and ENCLOSING_VOXEL for label data. The parameter <method> must be one
    of:
    
    CUBIC
    ENCLOSING_VOXEL
    TRILINEAR
    
    Args:
        runner: Command runner
        volume_in: volume to resample
        volume_space: a volume file in the volume space you want for the output
        method: the resampling method
        volume_out: the output volume
        opt_affine_affine: add an affine transform: the affine file to use
        opt_affine_series_affine_series: add an independent affine per-frame:
            text file containing 12 or 16 numbers per line, each being a row-major
            flattened affine
        opt_warp_warpfield: add a nonlinear warpfield transform: the warpfield
            file
    Returns:
        NamedTuple of outputs (described in `VolumeResampleOutputs`).
    """
    execution = runner.start_execution(VOLUME_RESAMPLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-resample")
    cargs.append(execution.input_file(volume_in))
    cargs.append(volume_space)
    cargs.append(method)
    cargs.append(execution.input_file(volume_out))
    if opt_affine_affine is not None:
        cargs.extend(["-affine", opt_affine_affine])
    if opt_affine_series_affine_series is not None:
        cargs.extend(["-affine-series", opt_affine_series_affine_series])
    if opt_warp_warpfield is not None:
        cargs.extend(["-warp", opt_warp_warpfield])
    ret = VolumeResampleOutputs(
        volume_out=execution.output_file(f"{volume_out}"),
    )
    execution.run(cargs)
    return ret