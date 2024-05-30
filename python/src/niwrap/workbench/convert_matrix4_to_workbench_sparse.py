# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


CONVERT_MATRIX4_TO_WORKBENCH_SPARSE_METADATA = Metadata(
    id="a26864aea637ed2645e8d8c927fa1f82e6fe9142",
    name="convert-matrix4-to-workbench-sparse",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ConvertMatrix4ToWorkbenchSparseVolumeSeedsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ConvertMatrix4ToWorkbenchSparseVolumeSeeds.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class ConvertMatrix4ToWorkbenchSparseVolumeSeeds:
    """
    specify the volume seed space
    """
    
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
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> ConvertMatrix4ToWorkbenchSparseVolumeSeedsOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `ConvertMatrix4ToWorkbenchSparseVolumeSeedsOutputs`).
        """
        ret = ConvertMatrix4ToWorkbenchSparseVolumeSeedsOutputs(
            root=execution.output_file("."),
        )
        return ret


class ConvertMatrix4ToWorkbenchSparseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_matrix4_to_workbench_sparse(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_seeds: ConvertMatrix4ToWorkbenchSparseVolumeSeedsOutputs
    """Subcommand outputs"""


def convert_matrix4_to_workbench_sparse(
    matrix4_1: str,
    matrix4_2: str,
    matrix4_3: str,
    orientation_file: InputPathType,
    voxel_list: str,
    wb_sparse_out: str,
    opt_surface_seeds_seed_roi: InputPathType | None = None,
    volume_seeds: ConvertMatrix4ToWorkbenchSparseVolumeSeeds | None = None,
    runner: Runner = None,
) -> ConvertMatrix4ToWorkbenchSparseOutputs:
    """
    convert-matrix4-to-workbench-sparse by Washington University School of Medicin.
    
    Convert a 3-file matrix4 to a workbench sparse file.
    
    Converts the matrix 4 output of probtrackx to workbench sparse file format.
    Exactly one of -surface-seeds and -volume-seeds must be specified.
    
    Args:
        matrix4_1: the first matrix4 file
        matrix4_2: the second matrix4 file
        matrix4_3: the third matrix4 file
        orientation_file: the .fiberTEMP.nii file this trajectory file applies
            to
        voxel_list: list of white matter voxel index triplets as used in the
            trajectory matrix
        wb_sparse_out: output - the output workbench sparse file
        opt_surface_seeds_seed_roi: specify the surface seed space: metric roi
            file of all vertices used in the seed space
        volume_seeds: specify the volume seed space
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `ConvertMatrix4ToWorkbenchSparseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_MATRIX4_TO_WORKBENCH_SPARSE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-convert-matrix4-to-workbench-sparse")
    cargs.append(matrix4_1)
    cargs.append(matrix4_2)
    cargs.append(matrix4_3)
    cargs.append(execution.input_file(orientation_file))
    cargs.append(voxel_list)
    cargs.append(wb_sparse_out)
    if opt_surface_seeds_seed_roi is not None:
        cargs.extend(["-surface-seeds", execution.input_file(opt_surface_seeds_seed_roi)])
    if volume_seeds is not None:
        cargs.extend(["-volume-seeds", *volume_seeds.run(execution)])
    ret = ConvertMatrix4ToWorkbenchSparseOutputs(
        root=execution.output_file("."),
        volume_seeds=volume_seeds.outputs(execution),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVERT_MATRIX4_TO_WORKBENCH_SPARSE_METADATA",
    "ConvertMatrix4ToWorkbenchSparseOutputs",
    "ConvertMatrix4ToWorkbenchSparseVolumeSeeds",
    "ConvertMatrix4ToWorkbenchSparseVolumeSeedsOutputs",
    "convert_matrix4_to_workbench_sparse",
]
