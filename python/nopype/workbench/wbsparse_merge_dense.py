# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.870526

import typing

from ..styxdefs import *


WBSPARSE_MERGE_DENSE_METADATA = Metadata(
    id="a1111bf6d7704cb0f2a4fbcee31160fa2692b589",
    name="wbsparse-merge-dense",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class WbsparseMergeDenseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `wbsparse_merge_dense(...)`.
    """


def wbsparse_merge_dense(
    runner: Runner,
    direction: str,
    wbsparse_out: str,
    opt_wbsparse_wbsparse_in: str | None = None,
) -> WbsparseMergeDenseOutputs:
    """
    MERGE WBSPARSE FILES ALONG DENSE DIMENSION.
    
    The input wbsparse files must have matching mappings along the direction not
    specified, and the mapping along the specified direction must be brain
    models.
    
    Args:
        runner: Command runner
        direction: which dimension to merge along, ROW or COLUMN
        wbsparse_out: output - the output wbsparse file
        opt_wbsparse_wbsparse_in: specify an input wbsparse file: a wbsparse
            file to merge
    Returns:
        NamedTuple of outputs (described in `WbsparseMergeDenseOutputs`).
    """
    execution = runner.start_execution(WBSPARSE_MERGE_DENSE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-wbsparse-merge-dense")
    cargs.append(direction)
    cargs.append(wbsparse_out)
    if opt_wbsparse_wbsparse_in is not None:
        cargs.extend(["-wbsparse", opt_wbsparse_wbsparse_in])
    ret = WbsparseMergeDenseOutputs(
    )
    execution.run(cargs)
    return ret