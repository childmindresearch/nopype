# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_EXPORT_DENSE_MAPPING_METADATA = Metadata(
    id="ab21dab4c846c0b8fb3eb710a6d3bff8f5ca1b13",
    name="cifti-export-dense-mapping",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiExportDenseMappingVolumeAll:
    """
    export the the mapping of all voxels
    """
    text_out: str
    """output - the output text file"""
    opt_no_cifti_index: bool = False
    """don't write the cifti index in the output file"""
    opt_structure: bool = False
    """write the structure each voxel belongs to in the output file"""
    
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
        cargs.append("-volume-all")
        cargs.append(self.text_out)
        if self.opt_no_cifti_index:
            cargs.append("-no-cifti-index")
        if self.opt_structure:
            cargs.append("-structure")
        return cargs


@dataclasses.dataclass
class CiftiExportDenseMappingSurface:
    """
    export the the mapping of one surface structure
    """
    structure: str
    """the structure to output"""
    text_out: str
    """output - the output text file"""
    opt_no_cifti_index: bool = False
    """don't write the cifti index in the output file"""
    
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
        cargs.append("-surface")
        cargs.append(self.structure)
        cargs.append(self.text_out)
        if self.opt_no_cifti_index:
            cargs.append("-no-cifti-index")
        return cargs


@dataclasses.dataclass
class CiftiExportDenseMappingVolume:
    """
    export the the mapping of one volume structure
    """
    structure: str
    """the structure to output"""
    text_out: str
    """output - the output text file"""
    opt_no_cifti_index: bool = False
    """don't write the cifti index in the output file"""
    
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
        cargs.append("-volume")
        cargs.append(self.structure)
        cargs.append(self.text_out)
        if self.opt_no_cifti_index:
            cargs.append("-no-cifti-index")
        return cargs


class CiftiExportDenseMappingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_export_dense_mapping(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_export_dense_mapping(
    cifti: InputPathType,
    direction: str,
    volume_all: CiftiExportDenseMappingVolumeAll | None = None,
    surface: list[CiftiExportDenseMappingSurface] = None,
    volume: list[CiftiExportDenseMappingVolume] = None,
    runner: Runner = None,
) -> CiftiExportDenseMappingOutputs:
    """
    cifti-export-dense-mapping by Washington University School of Medicin.
    
    Write index to element mapping as text.
    
    This command produces text files that describe the mapping from cifti
    indices to surface vertices or voxels. All indices are zero-based. The
    default format for -surface is lines of the form:
    
    <cifti-index> <vertex>
    
    The default format for -volume and -volume-all is lines of the form:
    
    <cifti-index> <i> <j> <k>
    
    For each <structure> argument, use one of the following strings:
    
    CORTEX_LEFT
    CORTEX_RIGHT
    CEREBELLUM
    ACCUMBENS_LEFT
    ACCUMBENS_RIGHT
    ALL_GREY_MATTER
    ALL_WHITE_MATTER
    AMYGDALA_LEFT
    AMYGDALA_RIGHT
    BRAIN_STEM
    CAUDATE_LEFT
    CAUDATE_RIGHT
    CEREBELLAR_WHITE_MATTER_LEFT
    CEREBELLAR_WHITE_MATTER_RIGHT
    CEREBELLUM_LEFT
    CEREBELLUM_RIGHT
    CEREBRAL_WHITE_MATTER_LEFT
    CEREBRAL_WHITE_MATTER_RIGHT
    CORTEX
    DIENCEPHALON_VENTRAL_LEFT
    DIENCEPHALON_VENTRAL_RIGHT
    HIPPOCAMPUS_LEFT
    HIPPOCAMPUS_RIGHT
    INVALID
    OTHER
    OTHER_GREY_MATTER
    OTHER_WHITE_MATTER
    PALLIDUM_LEFT
    PALLIDUM_RIGHT
    PUTAMEN_LEFT
    PUTAMEN_RIGHT
    THALAMUS_LEFT
    THALAMUS_RIGHT.
    
    Args:
        cifti: the cifti file.
        direction: which direction to export the mapping from, ROW or COLUMN.
        volume_all: export the the mapping of all voxels.
        surface: export the the mapping of one surface structure.
        volume: export the the mapping of one volume structure.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiExportDenseMappingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_EXPORT_DENSE_MAPPING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-export-dense-mapping")
    cargs.append(execution.input_file(cifti))
    cargs.append(direction)
    if volume_all is not None:
        cargs.extend(volume_all.run(execution))
    if surface is not None:
        cargs.extend([a for c in [s.run(execution) for s in surface] for a in c])
    if volume is not None:
        cargs.extend([a for c in [s.run(execution) for s in volume] for a in c])
    ret = CiftiExportDenseMappingOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_EXPORT_DENSE_MAPPING_METADATA",
    "CiftiExportDenseMappingOutputs",
    "CiftiExportDenseMappingSurface",
    "CiftiExportDenseMappingVolume",
    "CiftiExportDenseMappingVolumeAll",
    "cifti_export_dense_mapping",
]
