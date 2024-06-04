# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLSWAPDIM_EXE_METADATA = Metadata(
    id="7c7f270b7196a36d87fcce43ef191d96ce3395d8",
    name="fslswapdim_exe",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FslswapdimExeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslswapdim_exe(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """Output image file with swapped dimensions"""


def fslswapdim_exe(
    input_file: InputPathType,
    axis_a: str,
    axis_b: str,
    axis_c: str,
    output_file: InputPathType | None = None,
    check_lr_flag: bool = False,
    runner: Runner = None,
) -> FslswapdimExeOutputs:
    """
    fslswapdim_exe by FMRIB Centre, Oxford University.
    
    Tool to swap the x, y, z axes dimensions of an image.
    
    Args:
        input_file: Input image file (e.g., input.nii.gz)
        axis_a: New x-axis in terms of old axes (-x, x, y, -y, z, -z)
        axis_b: New y-axis in terms of old axes (-x, x, y, -y, z, -z)
        axis_c: New z-axis in terms of old axes (-x, x, y, -y, z, -z)
        output_file: Output image file (optional, cannot be used with --checkLR
            flag)
        check_lr_flag: Option to check if the specified arguments lead to a
            Left-Right swap or not, cannot be used with an output name
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `FslswapdimExeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLSWAPDIM_EXE_METADATA)
    cargs = []
    cargs.append("fslswapdim_exe")
    cargs.append(execution.input_file(input_file))
    cargs.append(axis_a)
    cargs.append(axis_b)
    cargs.append(axis_c)
    if output_file is not None:
        cargs.append(execution.input_file(output_file))
    if check_lr_flag:
        cargs.append("--checkLR")
    ret = FslswapdimExeOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"{pathlib.Path(output_file).name}", optional=True) if output_file is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLSWAPDIM_EXE_METADATA",
    "FslswapdimExeOutputs",
    "fslswapdim_exe",
]
