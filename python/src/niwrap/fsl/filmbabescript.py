# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FILMBABESCRIPT_METADATA = Metadata(
    id="7bcf9aaf7d7295f4282ba52a6958b4181d8fede6",
    name="filmbabescript",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="image-not-provided",
)


class FilmbabescriptOutputs(typing.NamedTuple):
    """
    Output object returned when calling `filmbabescript(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def filmbabescript(
    feat_dir: str,
    flobs_dir: str,
    runner: Runner = None,
) -> FilmbabescriptOutputs:
    """
    filmbabescript by Author Unknown.
    
    A tool/script for processing FEAT directories and FLOBs directories.
    
    More information: URL not provided
    
    Args:
        feat_dir: Input FEAT directory
        flobs_dir: Input FLOBs directory
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `FilmbabescriptOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FILMBABESCRIPT_METADATA)
    cargs = []
    cargs.append("filmbabescript")
    cargs.append(feat_dir)
    cargs.append(flobs_dir)
    ret = FilmbabescriptOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FILMBABESCRIPT_METADATA",
    "FilmbabescriptOutputs",
    "filmbabescript",
]
