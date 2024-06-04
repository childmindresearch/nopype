# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLCPGEOM_METADATA = Metadata(
    id="1994a0b404d8a4e67b02aeddc1322f37f2e05b08",
    name="fslcpgeom",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FslcpgeomOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslcpgeom(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslcpgeom(
    source_file: InputPathType,
    destination_file: InputPathType,
    dimensions_flag: bool = False,
    runner: Runner = None,
) -> FslcpgeomOutputs:
    """
    fslcpgeom by FMRIB Centre.
    
    FSL tool to copy image geometry from one file to another.
    
    More information:
    https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils#FSL-Extended-Utilities
    
    Args:
        source_file: Source image file (e.g. img1.nii.gz)
        destination_file: Destination image file (e.g. img2.nii.gz)
        dimensions_flag: Don't copy image dimensions
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `FslcpgeomOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLCPGEOM_METADATA)
    cargs = []
    cargs.append("fslcpgeom")
    cargs.append(execution.input_file(source_file))
    cargs.append(execution.input_file(destination_file))
    if dimensions_flag:
        cargs.append("-d")
    ret = FslcpgeomOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLCPGEOM_METADATA",
    "FslcpgeomOutputs",
    "fslcpgeom",
]
