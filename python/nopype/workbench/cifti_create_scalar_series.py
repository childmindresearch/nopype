# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


CIFTI_CREATE_SCALAR_SERIES_METADATA = Metadata(
    id="f4640c44e7a1ad32cf8297ee3384ab37787d11c3",
    name="cifti-create-scalar-series",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiCreateScalarSeriesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_create_scalar_series(...)`.
    """
    cifti_out: OutputPathType
    """output cifti file"""


def cifti_create_scalar_series(
    runner: Runner,
    input_: str,
    cifti_out: InputPathType,
    opt_transpose: bool = False,
    opt_name_file_file: str | None = None,
) -> CiftiCreateScalarSeriesOutputs:
    """
    IMPORT SERIES DATA INTO CIFTI.
    
    Convert a text file containing series of equal length into a cifti file. The
    text file should have lines made up of numbers separated by whitespace, with
    no extra newlines between lines.
    
    The <unit> argument must be one of the following:
    
    SECOND
    HERTZ
    METER
    RADIAN
    
    Args:
        runner: Command runner
        input_: input file
        cifti_out: output cifti file
        opt_transpose: use if the rows of the text file are along the scalar
            dimension
        opt_name_file_file: use a text file to set names on scalar dimension:
            text file containing names, one per line
    Returns:
        NamedTuple of outputs (described in `CiftiCreateScalarSeriesOutputs`).
    """
    execution = runner.start_execution(CIFTI_CREATE_SCALAR_SERIES_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-create-scalar-series")
    cargs.append(input_)
    cargs.append(execution.input_file(cifti_out))
    if opt_transpose:
        cargs.append("-transpose")
    if opt_name_file_file is not None:
        cargs.extend(["-name-file", opt_name_file_file])
    ret = CiftiCreateScalarSeriesOutputs(
        cifti_out=execution.output_file(f"{cifti_out}"),
    )
    execution.run(cargs)
    return ret