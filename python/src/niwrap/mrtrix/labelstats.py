# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


LABELSTATS_METADATA = Metadata(
    id="286c9fb1bf7805b495acc538d6c090d1834865ce",
    name="labelstats",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


class LabelstatsConfigOutputs(typing.NamedTuple):
    """
    Output object returned when calling `LabelstatsConfig.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class LabelstatsConfig:
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
    ) -> LabelstatsConfigOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `LabelstatsConfigOutputs`).
        """
        ret = LabelstatsConfigOutputs(
            root=execution.output_file("."),
        )
        return ret


class LabelstatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `labelstats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    config: typing.List[LabelstatsConfigOutputs]
    """Subcommand outputs"""


def labelstats(
    input_: InputPathType,
    output: typing.Literal["choice"] | None = None,
    voxelspace: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[LabelstatsConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> LabelstatsOutputs:
    """
    labelstats by Robert E. Smith (robert.smith@florey.edu.au).
    
    Compute statistics of parcels within a label image.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/labelstats.html
    
    Args:
        input_: the input label image
        output: output only the field specified; options are: mass,centre
        voxelspace: report parcel centres of mass in voxel space rather than
            scanner space
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
        NamedTuple of outputs (described in `LabelstatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABELSTATS_METADATA)
    cargs = []
    cargs.append("labelstats")
    if output is not None:
        cargs.extend(["-output", output])
    if voxelspace:
        cargs.append("-voxelspace")
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
    cargs.append(execution.input_file(input_))
    ret = LabelstatsOutputs(
        root=execution.output_file("."),
        config=[config.outputs(execution) for config in config],
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LABELSTATS_METADATA",
    "LabelstatsConfig",
    "LabelstatsConfigOutputs",
    "LabelstatsOutputs",
    "labelstats",
]
