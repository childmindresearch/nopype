# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FIRST_FLIRT_METADATA = Metadata(
    id="ac2f20ea9a7f965574ece6b5d5933c46688276f3",
    name="first_flirt",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FirstFlirtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `first_flirt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    registered_output_image: OutputPathType
    """Output image registered to standard space"""
    log_file: OutputPathType
    """Log file containing details of the registration process"""
    transformation_matrix: OutputPathType
    """Transformation matrix file"""


def first_flirt(
    input_image: InputPathType,
    output_basename: str,
    already_brain_extracted_flag: bool = False,
    debug_flag: bool = False,
    inweight_flag: bool = False,
    strucweight_mask: InputPathType | None = None,
    cort_flag: bool = False,
    cost_function: str | None = None,
    runner: Runner = None,
) -> FirstFlirtOutputs:
    """
    first_flirt by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    FLIRT-based image registration tool with additional options for brain
    extraction and weighting masks.
    
    Args:
        input_image: Input image (e.g. subject10rawT1.nii.gz)
        output_basename: Output basename for the results (e.g.
            subject10rawT1_to_std_sub)
        already_brain_extracted_flag: Input is already brain extracted
        debug_flag: Debug mode: don't delete intermediate files
        inweight_flag: Use a weighting mask on the first registration
        strucweight_mask: Use a specific structure weighting mask (in standard
            space) for an optional third-stage registration step (e.g.
            maskimage.nii.gz)
        cort_flag: Use a weighting mask of the whole brain on the first
            registration for specific models
        cost_function: Specify the cost function to be used by all FLIRT calls
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `FirstFlirtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIRST_FLIRT_METADATA)
    cargs = []
    cargs.append("first_flirt")
    cargs.append(execution.input_file(input_image))
    cargs.append(output_basename)
    if already_brain_extracted_flag:
        cargs.append("-b")
    if debug_flag:
        cargs.append("-d")
    if inweight_flag:
        cargs.append("-inweight")
    if strucweight_mask is not None:
        cargs.extend(["-strucweight", execution.input_file(strucweight_mask)])
    if cort_flag:
        cargs.append("-cort")
    if cost_function is not None:
        cargs.extend(["-cost", cost_function])
    ret = FirstFlirtOutputs(
        root=execution.output_file("."),
        registered_output_image=execution.output_file(f"{output_basename}_result.nii.gz", optional=True),
        log_file=execution.output_file(f"{output_basename}_log.txt", optional=True),
        transformation_matrix=execution.output_file(f"{output_basename}_matrix.mat", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIRST_FLIRT_METADATA",
    "FirstFlirtOutputs",
    "first_flirt",
]
