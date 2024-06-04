# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLSIZE_METADATA = Metadata(
    id="ff3e20689fe951d053ef5d2fb601d5c64f066339",
    name="fslsize",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FslsizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslsize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslsize(
    input_file: InputPathType,
    short_format_flag: bool = False,
    runner: Runner = None,
) -> FslsizeOutputs:
    """
    fslsize by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Tool to output the size of an image file in FSL.
    
    Args:
        input_file: Input image file
        short_format_flag: Output using short format (one line)
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `FslsizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLSIZE_METADATA)
    cargs = []
    cargs.append("fslsize")
    cargs.append(execution.input_file(input_file))
    if short_format_flag:
        cargs.append("-s")
    ret = FslsizeOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLSIZE_METADATA",
    "FslsizeOutputs",
    "fslsize",
]
