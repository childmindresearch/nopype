# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

VOLUME_WARPFIELD_AFFINE_REGRESSION_METADATA = Metadata(
    id="29b48fc5f8ad3eeb89b59fbd5229ca62c3f1cc87",
    name="volume-warpfield-affine-regression",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class VolumeWarpfieldAffineRegressionFlirtOut:
    """
    write output as a flirt matrix rather than a world coordinate transform
    """
    source_volume: str
    """the volume you want to apply the transform to"""
    target_volume: str
    """the target space you want the transformed volume to match"""
    
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
        cargs.append("-flirt-out")
        cargs.append(self.source_volume)
        cargs.append(self.target_volume)
        return cargs


class VolumeWarpfieldAffineRegressionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_warpfield_affine_regression(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def volume_warpfield_affine_regression(
    warpfield: str,
    affine_out: str,
    opt_roi_roi_vol: InputPathType | None = None,
    opt_fnirt_source_volume: str | None = None,
    flirt_out: VolumeWarpfieldAffineRegressionFlirtOut | None = None,
    runner: Runner = None,
) -> VolumeWarpfieldAffineRegressionOutputs:
    """
    volume-warpfield-affine-regression by Washington University School of Medicin.
    
    Regress affine from warpfield.
    
    For all voxels in the warpfield, do a regression that predicts the post-warp
    coordinate from the source coordinate. When -roi is specified, only consider
    voxels with a value greater than 0 in <roi-vol>.
    
    The default is to expect the warpfield to be in relative world coordinates
    (mm space), and to write the output as a world affine (mm space to mm
    space). If you are using FSL-created files and utilities, specify -fnirt and
    -flirt as needed, as their coordinate conventions are different.
    
    Args:
        warpfield: the input warpfield.
        affine_out: output - the output affine file.
        opt_roi_roi_vol: only consider voxels within a mask (e.g., a brain\
            mask): the mask volume.
        opt_fnirt_source_volume: input is a fnirt warpfield: the source volume\
            used when generating the fnirt warpfield.
        flirt_out: write output as a flirt matrix rather than a world\
            coordinate transform.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeWarpfieldAffineRegressionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_WARPFIELD_AFFINE_REGRESSION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-warpfield-affine-regression")
    cargs.append(warpfield)
    cargs.append(affine_out)
    if opt_roi_roi_vol is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_vol)])
    if opt_fnirt_source_volume is not None:
        cargs.extend(["-fnirt", opt_fnirt_source_volume])
    if flirt_out is not None:
        cargs.extend(flirt_out.run(execution))
    ret = VolumeWarpfieldAffineRegressionOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_WARPFIELD_AFFINE_REGRESSION_METADATA",
    "VolumeWarpfieldAffineRegressionFlirtOut",
    "VolumeWarpfieldAffineRegressionOutputs",
    "volume_warpfield_affine_regression",
]
