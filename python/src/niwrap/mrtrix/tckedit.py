# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


TCKEDIT_METADATA = Metadata(
    id="9826cd8bcf7139e530a5747a922b1421f5bdb5c4",
    name="tckedit",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


class TckeditIncludeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `TckeditInclude.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class TckeditInclude:
    """
    specify an inclusion region of interest, as either a binary mask image, or as a sphere using 4 comma-separared values (x,y,z,radius). Streamlines must traverse ALL inclusion regions to be accepted.
    """
    spec: str
    """specify an inclusion region of interest, as either a binary mask image,
    or as a sphere using 4 comma-separared values (x,y,z,radius). Streamlines
    must traverse ALL inclusion regions to be accepted."""
    
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
        cargs.append("-include")
        cargs.append(self.spec)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> TckeditIncludeOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `TckeditIncludeOutputs`).
        """
        ret = TckeditIncludeOutputs(
            root=execution.output_file("."),
        )
        return ret


class TckeditIncludeOrderedOutputs(typing.NamedTuple):
    """
    Output object returned when calling `TckeditIncludeOrdered.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class TckeditIncludeOrdered:
    """
    specify an inclusion region of interest, as either a binary mask image, or as a sphere using 4 comma-separared values (x,y,z,radius). Streamlines must traverse ALL inclusion_ordered regions in the order they are specified in order to be accepted.
    """
    image: str
    """specify an inclusion region of interest, as either a binary mask image,
    or as a sphere using 4 comma-separared values (x,y,z,radius). Streamlines
    must traverse ALL inclusion_ordered regions in the order they are specified
    in order to be accepted."""
    
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
        cargs.append("-include_ordered")
        cargs.append(self.image)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> TckeditIncludeOrderedOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `TckeditIncludeOrderedOutputs`).
        """
        ret = TckeditIncludeOrderedOutputs(
            root=execution.output_file("."),
        )
        return ret


class TckeditExcludeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `TckeditExclude.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class TckeditExclude:
    """
    specify an exclusion region of interest, as either a binary mask image, or as a sphere using 4 comma-separared values (x,y,z,radius). Streamlines that enter ANY exclude region will be discarded.
    """
    spec: str
    """specify an exclusion region of interest, as either a binary mask image,
    or as a sphere using 4 comma-separared values (x,y,z,radius). Streamlines
    that enter ANY exclude region will be discarded."""
    
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
        cargs.append("-exclude")
        cargs.append(self.spec)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> TckeditExcludeOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `TckeditExcludeOutputs`).
        """
        ret = TckeditExcludeOutputs(
            root=execution.output_file("."),
        )
        return ret


class TckeditMaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `TckeditMask.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class TckeditMask:
    """
    specify a masking region of interest, as either a binary mask image, or as a sphere using 4 comma-separared values (x,y,z,radius). If defined, streamlines exiting the mask will be truncated.
    """
    spec: str
    """specify a masking region of interest, as either a binary mask image, or
    as a sphere using 4 comma-separared values (x,y,z,radius). If defined,
    streamlines exiting the mask will be truncated."""
    
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
        cargs.append("-mask")
        cargs.append(self.spec)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> TckeditMaskOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `TckeditMaskOutputs`).
        """
        ret = TckeditMaskOutputs(
            root=execution.output_file("."),
        )
        return ret


class TckeditConfigOutputs(typing.NamedTuple):
    """
    Output object returned when calling `TckeditConfig.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class TckeditConfig:
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
    ) -> TckeditConfigOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `TckeditConfigOutputs`).
        """
        ret = TckeditConfigOutputs(
            root=execution.output_file("."),
        )
        return ret


class TckeditOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tckedit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    tracks_out: OutputPathType
    """the output track file"""
    tck_weights_out: OutputPathType | None
    """specify the path for an output text scalar file containing streamline weights """
    include: typing.List[TckeditIncludeOutputs]
    """Subcommand outputs"""
    include_ordered: typing.List[TckeditIncludeOrderedOutputs]
    """Subcommand outputs"""
    exclude: typing.List[TckeditExcludeOutputs]
    """Subcommand outputs"""
    mask: typing.List[TckeditMaskOutputs]
    """Subcommand outputs"""
    config: typing.List[TckeditConfigOutputs]
    """Subcommand outputs"""


def tckedit(
    tracks_in: list[InputPathType],
    tracks_out: InputPathType,
    include: list[TckeditInclude] = None,
    include_ordered: list[TckeditIncludeOrdered] = None,
    exclude: list[TckeditExclude] = None,
    mask: list[TckeditMask] = None,
    maxlength: float | int | None = None,
    minlength: float | int | None = None,
    number: int | None = None,
    skip: int | None = None,
    maxweight: float | int | None = None,
    minweight: float | int | None = None,
    inverse: bool = False,
    ends_only: bool = False,
    tck_weights_in: InputPathType | None = None,
    tck_weights_out: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TckeditConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> TckeditOutputs:
    """
    tckedit by Robert E. Smith (robert.smith@florey.edu.au).
    
    Perform various editing operations on track files.
    
    This command can be used to perform various types of manipulations on track
    data. A range of such manipulations are demonstrated in the examples
    provided below.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/tckedit.html
    
    Args:
        tracks_in: the input track file(s)
        tracks_out: the output track file
        include: specify an inclusion region of interest, as either a binary
            mask image, or as a sphere using 4 comma-separared values
            (x,y,z,radius). Streamlines must traverse ALL inclusion regions to be
            accepted.
        include_ordered: specify an inclusion region of interest, as either a
            binary mask image, or as a sphere using 4 comma-separared values
            (x,y,z,radius). Streamlines must traverse ALL inclusion_ordered regions
            in the order they are specified in order to be accepted.
        exclude: specify an exclusion region of interest, as either a binary
            mask image, or as a sphere using 4 comma-separared values
            (x,y,z,radius). Streamlines that enter ANY exclude region will be
            discarded.
        mask: specify a masking region of interest, as either a binary mask
            image, or as a sphere using 4 comma-separared values (x,y,z,radius). If
            defined, streamlines exiting the mask will be truncated.
        maxlength: set the maximum length of any streamline in mm
        minlength: set the minimum length of any streamline in mm
        number: set the desired number of selected streamlines to be propagated
            to the output file
        skip: omit this number of selected streamlines before commencing writing
            to the output file
        maxweight: set the maximum weight of any streamline
        minweight: set the minimum weight of any streamline
        inverse: output the inverse selection of streamlines based on the
            criteria provided; i.e. only those streamlines that fail at least one
            selection criterion, and/or vertices that are outside masks if provided,
            will be written to file
        ends_only: only test the ends of each streamline against the provided
            include/exclude ROIs
        tck_weights_in: specify a text scalar file containing the streamline
            weights
        tck_weights_out: specify the path for an output text scalar file
            containing streamline weights
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
        NamedTuple of outputs (described in `TckeditOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCKEDIT_METADATA)
    cargs = []
    cargs.append("tckedit")
    if include is not None:
        cargs.extend([a for c in [s.run(execution) for s in include] for a in c])
    if include_ordered is not None:
        cargs.extend([a for c in [s.run(execution) for s in include_ordered] for a in c])
    if exclude is not None:
        cargs.extend([a for c in [s.run(execution) for s in exclude] for a in c])
    if mask is not None:
        cargs.extend([a for c in [s.run(execution) for s in mask] for a in c])
    if maxlength is not None:
        cargs.extend(["-maxlength", str(maxlength)])
    if minlength is not None:
        cargs.extend(["-minlength", str(minlength)])
    if number is not None:
        cargs.extend(["-number", str(number)])
    if skip is not None:
        cargs.extend(["-skip", str(skip)])
    if maxweight is not None:
        cargs.extend(["-maxweight", str(maxweight)])
    if minweight is not None:
        cargs.extend(["-minweight", str(minweight)])
    if inverse:
        cargs.append("-inverse")
    if ends_only:
        cargs.append("-ends_only")
    if tck_weights_in is not None:
        cargs.extend(["-tck_weights_in", execution.input_file(tck_weights_in)])
    if tck_weights_out is not None:
        cargs.extend(["-tck_weights_out", execution.input_file(tck_weights_out)])
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
    cargs.extend([execution.input_file(f) for f in tracks_in])
    cargs.append(execution.input_file(tracks_out))
    ret = TckeditOutputs(
        root=execution.output_file("."),
        tracks_out=execution.output_file(f"{pathlib.Path(tracks_out).name}"),
        tck_weights_out=execution.output_file(f"{pathlib.Path(tck_weights_out).name}") if tck_weights_out is not None else None,
        include=[include.outputs(execution) for include in include],
        include_ordered=[include_ordered.outputs(execution) for include_ordered in include_ordered],
        exclude=[exclude.outputs(execution) for exclude in exclude],
        mask=[mask.outputs(execution) for mask in mask],
        config=[config.outputs(execution) for config in config],
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TCKEDIT_METADATA",
    "TckeditConfig",
    "TckeditConfigOutputs",
    "TckeditExclude",
    "TckeditExcludeOutputs",
    "TckeditInclude",
    "TckeditIncludeOrdered",
    "TckeditIncludeOrderedOutputs",
    "TckeditIncludeOutputs",
    "TckeditMask",
    "TckeditMaskOutputs",
    "TckeditOutputs",
    "tckedit",
]
