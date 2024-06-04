# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

TBSS_SKELETON_METADATA = Metadata(
    id="b7cc100b31dab2dc2749169d03876d80618788b8",
    name="tbss_skeleton",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class TbssSkeletonOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tbss_skeleton(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    skeleton_output: OutputPathType
    """Output skeleton image"""


def tbss_skeleton(
    input_image: InputPathType,
    output_image: InputPathType | None = None,
    skeleton_params: list[str] = None,
    alternative_4ddata: InputPathType | None = None,
    alternative_skeleton: InputPathType | None = None,
    help_flag: bool = False,
    debug_flag: bool = False,
    debug2_flag: InputPathType | None = None,
    runner: Runner = None,
) -> TbssSkeletonOutputs:
    """
    tbss_skeleton by University of Oxford (Stephen Smith).
    
    TBSS Skeletonization tool from FSL.
    
    More information:
    https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/TBSS/UserGuide#Step_4:_tbss_skeleton
    
    Args:
        input_image: Input image
        output_image: Output skeleton image
        skeleton_params: Skeleton threshold, distance map, search rule mask, 4D
            data and projected 4D data in that order
        alternative_4ddata: Alternative 4D data (e.g., L1)
        alternative_skeleton: Alternative skeleton
        help_flag: Display help message
        debug_flag: Enable debugging image outputs
        debug2_flag: De-project skelpoints points on skeleton back to all_FA
            space
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `TbssSkeletonOutputs`).
    """
    runner = runner or get_global_runner()
    if skeleton_params is not None and not (len(skeleton_params) <= 5): 
        raise ValueError(f"Length of 'skeleton_params' must be less than 5 but was {len(skeleton_params)}")
    execution = runner.start_execution(TBSS_SKELETON_METADATA)
    cargs = []
    cargs.append("tbss_skeleton")
    cargs.extend(["-i", execution.input_file(input_image)])
    cargs.append("[SKEL_THRESHOLD]")
    cargs.append("[DISTANCE_MAP]")
    cargs.append("[SEARCH_RULE_MASK]")
    cargs.append("[4DDATA]")
    cargs.append("[PROJECTED_4DDATA]")
    if alternative_4ddata is not None:
        cargs.extend(["-a", execution.input_file(alternative_4ddata)])
    if alternative_skeleton is not None:
        cargs.extend(["-s", execution.input_file(alternative_skeleton)])
    if output_image is not None:
        cargs.extend(["-o", execution.input_file(output_image)])
    if help_flag:
        cargs.append("-h")
    if debug_flag:
        cargs.append("-d")
    if debug2_flag is not None:
        cargs.extend(["-D", execution.input_file(debug2_flag)])
    ret = TbssSkeletonOutputs(
        root=execution.output_file("."),
        skeleton_output=execution.output_file(f"skeleton_output.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TBSS_SKELETON_METADATA",
    "TbssSkeletonOutputs",
    "tbss_skeleton",
]
