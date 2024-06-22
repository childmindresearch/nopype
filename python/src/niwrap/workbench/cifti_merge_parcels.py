# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_MERGE_PARCELS_METADATA = Metadata(
    id="8a405856cf70836460d08946786378f72f650d6b",
    name="cifti-merge-parcels",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiMergeParcelsCifti:
    """
    specify an input cifti file
    """
    cifti_in: InputPathType
    """a cifti file to merge"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-cifti")
        cargs.append(execution.input_file(self.cifti_in))
        return cargs


class CiftiMergeParcelsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_merge_parcels(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_merge_parcels(
    direction: str,
    cifti_out: InputPathType,
    cifti: list[CiftiMergeParcelsCifti] = None,
    runner: Runner = None,
) -> CiftiMergeParcelsOutputs:
    """
    cifti-merge-parcels by Washington University School of Medicin.
    
    Merge cifti files along parcels dimension.
    
    The input cifti files must have matching mappings along the direction not
    specified, and the mapping along the specified direction must be parcels.
    The direction can be either an integer starting from 1, or the strings 'ROW'
    or 'COLUMN'.
    
    Args:
        direction: which dimension to merge along (integer, 'ROW', or 'COLUMN').
        cifti_out: the output cifti file.
        cifti: specify an input cifti file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiMergeParcelsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_MERGE_PARCELS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-merge-parcels")
    cargs.append(direction)
    cargs.append(execution.input_file(cifti_out))
    if cifti is not None:
        cargs.extend([a for c in [s.run(execution) for s in cifti] for a in c])
    ret = CiftiMergeParcelsOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_MERGE_PARCELS_METADATA",
    "CiftiMergeParcelsCifti",
    "CiftiMergeParcelsOutputs",
    "cifti_merge_parcels",
]
