# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

EDDY_SQUAD_METADATA = Metadata(
    id="1a0358224e0d08712229ec6f87648df2db3df771",
    name="eddy_squad",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class EddySquadOutputs(typing.NamedTuple):
    """
    Output object returned when calling `eddy_squad(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    qc_results: OutputPathType | None
    """QC results in JSON format"""


def eddy_squad(
    subject_list: str,
    grouping: str | None = None,
    group_db: InputPathType | None = None,
    update_: bool = False,
    output_dir: str | None = None,
    runner: Runner = None,
) -> EddySquadOutputs:
    """
    eddy_squad by FMRIB Software Library (FSL).
    
    Study-wise QC for dMRI data.
    
    More information:
    https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/eddy/UsersGuide#EDDY_QC
    
    Args:
        subject_list: List of subject IDs for the QC.
        grouping: Specifies the grouping of studies.
        group_db: Path to the group database.
        update_: Option to update the QC results.
        output_dir: Output directory for the QC results.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `EddySquadOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EDDY_SQUAD_METADATA)
    cargs = []
    cargs.append("eddy_squad")
    if grouping is not None:
        cargs.extend(["-g", grouping])
    if group_db is not None:
        cargs.extend(["-gdb", execution.input_file(group_db)])
    if update_:
        cargs.append("-u")
    if output_dir is not None:
        cargs.extend(["-o", output_dir])
    cargs.append(subject_list)
    ret = EddySquadOutputs(
        root=execution.output_file("."),
        qc_results=execution.output_file(f"{output_dir}/qc_results.json", optional=True) if output_dir is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "EDDY_SQUAD_METADATA",
    "EddySquadOutputs",
    "eddy_squad",
]
