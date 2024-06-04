# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

PROJ_THRESH_METADATA = Metadata(
    id="d433b7b38b1bca3728c07db0bfce71d86483f89c",
    name="proj_thresh",
)


class ProjThreshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `proj_thresh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def proj_thresh(
    input_paths: list[InputPathType],
    threshold: float | int,
    runner: Runner = None,
) -> ProjThreshOutputs:
    """
    proj_thresh by Unknown.
    
    A tool to apply a threshold to either volumes or surfaces.
    
    Args:
        input_paths: Paths to volume or surface files. Please use either volumes
            or surfaces but not both.
        threshold: Threshold value to be applied.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `ProjThreshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PROJ_THRESH_METADATA)
    cargs = []
    cargs.append("proj_thresh")
    cargs.extend([execution.input_file(f) for f in input_paths])
    cargs.append(str(threshold))
    ret = ProjThreshOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PROJ_THRESH_METADATA",
    "ProjThreshOutputs",
    "proj_thresh",
]
