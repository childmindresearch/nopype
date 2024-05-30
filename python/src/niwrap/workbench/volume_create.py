# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


VOLUME_CREATE_METADATA = Metadata(
    id="2efc737c1b4ef92da53e59ceaab4e071268a7c77",
    name="volume-create",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VolumeCreatePlumbOutputs(typing.NamedTuple):
    """
    Output object returned when calling `VolumeCreatePlumb.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class VolumeCreatePlumb:
    """
    set via axis order and spacing/offset
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
    ) -> VolumeCreatePlumbOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `VolumeCreatePlumbOutputs`).
        """
        ret = VolumeCreatePlumbOutputs(
            root=execution.output_file("."),
        )
        return ret


class VolumeCreateSformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `VolumeCreateSform.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class VolumeCreateSform:
    """
    set via a nifti sform
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
    ) -> VolumeCreateSformOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `VolumeCreateSformOutputs`).
        """
        ret = VolumeCreateSformOutputs(
            root=execution.output_file("."),
        )
        return ret


class VolumeCreateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_create(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""
    plumb: VolumeCreatePlumbOutputs
    """Subcommand outputs"""
    sform: VolumeCreateSformOutputs
    """Subcommand outputs"""


def volume_create(
    i_dim: int,
    j_dim: int,
    k_dim: int,
    volume_out: InputPathType,
    plumb: VolumeCreatePlumb | None = None,
    sform: VolumeCreateSform | None = None,
    runner: Runner = None,
) -> VolumeCreateOutputs:
    """
    volume-create by Washington University School of Medicin.
    
    Create a blank volume file.
    
    Creates a volume file full of zeros. Exactly one of -plumb or -sform must be
    specified.
    
    Args:
        i_dim: length of first dimension
        j_dim: length of second dimension
        k_dim: length of third dimension
        volume_out: the output volume
        plumb: set via axis order and spacing/offset
        sform: set via a nifti sform
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeCreateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_CREATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-create")
    cargs.append(str(i_dim))
    cargs.append(str(j_dim))
    cargs.append(str(k_dim))
    cargs.append(execution.input_file(volume_out))
    if plumb is not None:
        cargs.extend(["-plumb", *plumb.run(execution)])
    if sform is not None:
        cargs.extend(["-sform", *sform.run(execution)])
    ret = VolumeCreateOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).name}"),
        plumb=plumb.outputs(execution),
        sform=sform.outputs(execution),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_CREATE_METADATA",
    "VolumeCreateOutputs",
    "VolumeCreatePlumb",
    "VolumeCreatePlumbOutputs",
    "VolumeCreateSform",
    "VolumeCreateSformOutputs",
    "volume_create",
]
