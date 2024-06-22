# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

VOLUME_MERGE_METADATA = Metadata(
    id="19d5788f8e36ff96123e1149b833db7a03da4fdd",
    name="volume-merge",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class VolumeMergeUpTo:
    """
    use an inclusive range of subvolumes
    """
    last_subvol: str
    """the number or name of the last subvolume to include"""
    opt_reverse: bool = False
    """use the range in reverse order"""
    
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
        cargs.append("-up-to")
        cargs.append(self.last_subvol)
        if self.opt_reverse:
            cargs.append("-reverse")
        return cargs


@dataclasses.dataclass
class VolumeMergeSubvolume:
    """
    select a single subvolume to use
    """
    subvol: str
    """the subvolume number or name"""
    up_to: VolumeMergeUpTo | None = None
    """use an inclusive range of subvolumes"""
    
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
        cargs.append("-subvolume")
        cargs.append(self.subvol)
        if self.up_to is not None:
            cargs.extend(self.up_to.run(execution))
        return cargs


@dataclasses.dataclass
class VolumeMergeVolume:
    """
    specify an input volume file
    """
    volume_in: InputPathType
    """a volume file to use subvolumes from"""
    subvolume: list[VolumeMergeSubvolume] = None
    """select a single subvolume to use"""
    
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
        cargs.append(execution.input_file(self.volume_in))
        if self.subvolume is not None:
            cargs.extend([a for c in [s.run(execution) for s in self.subvolume] for a in c])
        return cargs


class VolumeMergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_merge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume file"""


def volume_merge(
    volume_out: InputPathType,
    volume: list[VolumeMergeVolume] = None,
    runner: Runner = None,
) -> VolumeMergeOutputs:
    """
    volume-merge by Washington University School of Medicin.
    
    Merge volume files into a new file.
    
    Takes one or more volume files and constructs a new volume file by
    concatenating subvolumes from them. The input volume files must have the
    same volume space.
    
    Example: wb_command -volume-merge out.nii -volume first.nii -subvolume 1
    -volume second.nii
    
    This example would take the first subvolume from first.nii, followed by all
    subvolumes from second.nii, and write these to out.nii.
    
    Args:
        volume_out: the output volume file.
        volume: specify an input volume file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeMergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_MERGE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-merge")
    cargs.append(execution.input_file(volume_out))
    if volume is not None:
        cargs.extend([a for c in [s.run(execution) for s in volume] for a in c])
    ret = VolumeMergeOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_MERGE_METADATA",
    "VolumeMergeOutputs",
    "VolumeMergeSubvolume",
    "VolumeMergeUpTo",
    "VolumeMergeVolume",
    "volume_merge",
]
