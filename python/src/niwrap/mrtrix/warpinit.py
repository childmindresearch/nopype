# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


WARPINIT_METADATA = Metadata(
    id="89b6a74cefdfe9ff35d5f636ecfe36bce0e39b5d",
    name="warpinit",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


class WarpinitConfigOutputs(typing.NamedTuple):
    """
    Output object returned when calling `WarpinitConfig.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class WarpinitConfig:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value: str
    """temporarily set the value of an MRtrix config file entry."""
    
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
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> WarpinitConfigOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `WarpinitConfigOutputs`).
        """
        ret = WarpinitConfigOutputs(
            root=execution.output_file("."),
        )
        return ret


class WarpinitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `warpinit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    warp: OutputPathType
    """the output warp image."""
    config: typing.List[WarpinitConfigOutputs]
    """Subcommand outputs"""


def warpinit(
    template: InputPathType,
    warp: InputPathType,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[WarpinitConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> WarpinitOutputs:
    """
    warpinit by J-Donald Tournier (jdtournier@gmail.com).
    
    Create an initial warp image, representing an identity transformation.
    
    This is useful to obtain the warp fields from other normalisation
    applications, by applying the transformation of interest to the warp field
    generated by this program.
    
    The image generated is a 4D image with the same spatial characteristics as
    the input template image. It contains 3 volumes, with each voxel containing
    its own x,y,z coordinates.
    
    Note that this command can be used to create 3 separate X,Y,Z images
    directly (which may be useful to create images suitable for use in the
    registration program) using the following syntax:
    
    $ warpinit template.mif warp-'[]'.nii
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/warpinit.html
    
    Args:
        template: the input template image.
        warp: the output warp image.
        info: display information messages.
        quiet: do not display information messages or progress status;
            alternatively, this can be achieved by setting the MRTRIX_QUIET
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications (set
            to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `WarpinitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WARPINIT_METADATA)
    cargs = []
    cargs.append("warpinit")
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend(["-nthreads", str(nthreads)])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(template))
    cargs.append(execution.input_file(warp))
    ret = WarpinitOutputs(
        root=execution.output_file("."),
        warp=execution.output_file(f"{pathlib.Path(warp).name}"),
        config=[config.outputs(execution) for config in config],
    )
    execution.run(cargs)
    return ret


__all__ = [
    "WARPINIT_METADATA",
    "WarpinitConfig",
    "WarpinitConfigOutputs",
    "WarpinitOutputs",
    "warpinit",
]
