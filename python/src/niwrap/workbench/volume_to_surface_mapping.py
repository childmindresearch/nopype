# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


VOLUME_TO_SURFACE_MAPPING_METADATA = Metadata(
    id="cb01faa679067e09945f8830eccc7c74db53e5b3",
    name="volume-to-surface-mapping",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VolumeToSurfaceMappingVolumeRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `VolumeToSurfaceMappingVolumeRoi.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class VolumeToSurfaceMappingVolumeRoi:
    """
    use a volume roi
    """
    opt_weighted: bool = False
    """treat the roi values as weightings rather than binary"""
    
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
        if self.opt_weighted:
            cargs.append("-weighted")
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> VolumeToSurfaceMappingVolumeRoiOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `VolumeToSurfaceMappingVolumeRoiOutputs`).
        """
        ret = VolumeToSurfaceMappingVolumeRoiOutputs(
            root=execution.output_file("."),
        )
        return ret


class VolumeToSurfaceMappingOutputWeightsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `VolumeToSurfaceMappingOutputWeights.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    weights_out: OutputPathType
    """volume to write the weights to"""


@dataclasses.dataclass
class VolumeToSurfaceMappingOutputWeights:
    """
    write the voxel weights for a vertex to a volume file
    """
    weights_out: InputPathType
    """volume to write the weights to"""
    
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
        cargs.append(execution.input_file(self.weights_out))
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> VolumeToSurfaceMappingOutputWeightsOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `VolumeToSurfaceMappingOutputWeightsOutputs`).
        """
        ret = VolumeToSurfaceMappingOutputWeightsOutputs(
            root=execution.output_file("."),
            weights_out=execution.output_file(f"{pathlib.Path(self.weights_out).name}"),
        )
        return ret


class VolumeToSurfaceMappingRibbonConstrainedOutputs(typing.NamedTuple):
    """
    Output object returned when calling `VolumeToSurfaceMappingRibbonConstrained.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    self.volume_roi: VolumeToSurfaceMappingVolumeRoiOutputs
    """Subcommand outputs"""
    self.output_weights: VolumeToSurfaceMappingOutputWeightsOutputs
    """Subcommand outputs"""


@dataclasses.dataclass
class VolumeToSurfaceMappingRibbonConstrained:
    """
    use ribbon constrained mapping algorithm
    """
    volume_roi: VolumeToSurfaceMappingVolumeRoi | None = None
    """use a volume roi"""
    opt_voxel_subdiv_subdiv_num: int | None = None
    """voxel divisions while estimating voxel weights: number of subdivisions,
    default 3"""
    opt_thin_columns: bool = False
    """use non-overlapping polyhedra"""
    opt_gaussian_scale: float | int | None = None
    """reduce weight to voxels that aren't near <surface>: value to multiply the
    local thickness by, to get the gaussian sigma"""
    opt_interpolate_method: str | None = None
    """instead of a weighted average of voxels, interpolate at subpoints inside
    the ribbon: interpolation method, must be CUBIC, ENCLOSING_VOXEL, or
    TRILINEAR"""
    opt_bad_vertices_out: bool = False
    """output an ROI of which vertices didn't intersect any valid voxels"""
    roi_out: InputPathType
    """the output metric file of vertices that have no data"""
    output_weights: VolumeToSurfaceMappingOutputWeights | None = None
    """write the voxel weights for a vertex to a volume file"""
    opt_output_weights_text_text_out: str | None = None
    """write the voxel weights for all vertices to a text file: output - the
    output text filename"""
    
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
        if self.volume_roi is not None:
            cargs.extend(["-volume-roi", *self.volume_roi.run(execution)])
        if self.opt_voxel_subdiv_subdiv_num is not None:
            cargs.extend(["-voxel-subdiv", str(self.opt_voxel_subdiv_subdiv_num)])
        if self.opt_thin_columns:
            cargs.append("-thin-columns")
        if self.opt_gaussian_scale is not None:
            cargs.extend(["-gaussian", str(self.opt_gaussian_scale)])
        if self.opt_interpolate_method is not None:
            cargs.extend(["-interpolate", self.opt_interpolate_method])
        if self.opt_bad_vertices_out:
            cargs.append("-bad-vertices-out")
        cargs.append(execution.input_file(self.roi_out))
        if self.output_weights is not None:
            cargs.extend(["-output-weights", *self.output_weights.run(execution)])
        if self.opt_output_weights_text_text_out is not None:
            cargs.extend(["-output-weights-text", self.opt_output_weights_text_text_out])
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> VolumeToSurfaceMappingRibbonConstrainedOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `VolumeToSurfaceMappingRibbonConstrainedOutputs`).
        """
        ret = VolumeToSurfaceMappingRibbonConstrainedOutputs(
            root=execution.output_file("."),
            self.volume_roi=self.volume_roi.outputs(execution),
            self.output_weights=self.output_weights.outputs(execution),
        )
        return ret


class VolumeToSurfaceMappingMyelinStyleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `VolumeToSurfaceMappingMyelinStyle.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class VolumeToSurfaceMappingMyelinStyle:
    """
    use the method from myelin mapping
    """
    opt_legacy_bug: bool = False
    """emulate old v1.2.3 and earlier code that didn't follow a cylinder
    cutoff"""
    
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
        if self.opt_legacy_bug:
            cargs.append("-legacy-bug")
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> VolumeToSurfaceMappingMyelinStyleOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `VolumeToSurfaceMappingMyelinStyleOutputs`).
        """
        ret = VolumeToSurfaceMappingMyelinStyleOutputs(
            root=execution.output_file("."),
        )
        return ret


class VolumeToSurfaceMappingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_to_surface_mapping(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric file"""
    ribbon_constrained: VolumeToSurfaceMappingRibbonConstrainedOutputs
    """Subcommand outputs"""
    myelin_style: VolumeToSurfaceMappingMyelinStyleOutputs
    """Subcommand outputs"""


def volume_to_surface_mapping(
    volume: InputPathType,
    surface: InputPathType,
    metric_out: InputPathType,
    opt_trilinear: bool = False,
    opt_enclosing: bool = False,
    opt_cubic: bool = False,
    ribbon_constrained: VolumeToSurfaceMappingRibbonConstrained | None = None,
    myelin_style: VolumeToSurfaceMappingMyelinStyle | None = None,
    opt_subvol_select_subvol: str | None = None,
    runner: Runner = None,
) -> VolumeToSurfaceMappingOutputs:
    """
    volume-to-surface-mapping by Washington University School of Medicin.
    
    Map volume to surface.
    
    You must specify exactly one mapping method. Enclosing voxel uses the value
    from the voxel the vertex lies inside, while trilinear does a 3D linear
    interpolation based on the voxels immediately on each side of the vertex's
    position.
    
    The ribbon mapping method constructs a polyhedron from the vertex's
    neighbors on each surface, and estimates the amount of this polyhedron's
    volume that falls inside any nearby voxels, to use as the weights for
    sampling. If -thin-columns is specified, the polyhedron uses the edge
    midpoints and triangle centroids, so that neighboring vertices do not have
    overlapping polyhedra. This may require increasing -voxel-subdiv to get
    enough samples in each voxel to reliably land inside these smaller
    polyhedra. The volume ROI is useful to exclude partial volume effects of
    voxels the surfaces pass through, and will cause the mapping to ignore
    voxels that don't have a positive value in the mask. The subdivision number
    specifies how it approximates the amount of the volume the polyhedron
    intersects, by splitting each voxel into NxNxN pieces, and checking whether
    the center of each piece is inside the polyhedron. If you have very large
    voxels, consider increasing this if you get zeros in your output. The
    -gaussian option makes it act more like the myelin method, where the
    distance of a voxel from <surface> is used to downweight the voxel. The
    -interpolate suboption, instead of doing a weighted average of voxels,
    interpolates from the volume at the subdivided points inside the ribbon. If
    using both -interpolate and the -weighted suboption to -volume-roi, the roi
    volume weights are linearly interpolated, unless the -interpolate method is
    ENCLOSING_VOXEL, in which case ENCLOSING_VOXEL is also used for sampling the
    roi volume weights.
    
    The myelin style method uses part of the caret5 myelin mapping command to do
    the mapping: for each surface vertex, take all voxels that are in a cylinder
    with radius and height equal to cortical thickness, centered on the vertex
    and aligned with the surface normal, and that are also within the ribbon
    ROI, and apply a gaussian kernel with the specified sigma to them to get the
    weights to use. The -legacy-bug flag reverts to the unintended behavior
    present from the initial implementation up to and including v1.2.3, which
    had only the tangential cutoff and a bounding box intended to be larger than
    where the cylinder cutoff should have been.
    
    Args:
        volume: the volume to map data from
        surface: the surface to map the data onto
        metric_out: the output metric file
        opt_trilinear: use trilinear volume interpolation
        opt_enclosing: use value of the enclosing voxel
        opt_cubic: use cubic splines
        ribbon_constrained: use ribbon constrained mapping algorithm
        myelin_style: use the method from myelin mapping
        opt_subvol_select_subvol: select a single subvolume to map: the
            subvolume number or name
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeToSurfaceMappingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_TO_SURFACE_MAPPING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-to-surface-mapping")
    cargs.append(execution.input_file(volume))
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_out))
    if opt_trilinear:
        cargs.append("-trilinear")
    if opt_enclosing:
        cargs.append("-enclosing")
    if opt_cubic:
        cargs.append("-cubic")
    if ribbon_constrained is not None:
        cargs.extend(["-ribbon-constrained", *ribbon_constrained.run(execution)])
    if myelin_style is not None:
        cargs.extend(["-myelin-style", *myelin_style.run(execution)])
    if opt_subvol_select_subvol is not None:
        cargs.extend(["-subvol-select", opt_subvol_select_subvol])
    ret = VolumeToSurfaceMappingOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{pathlib.Path(metric_out).name}"),
        ribbon_constrained=ribbon_constrained.outputs(execution),
        myelin_style=myelin_style.outputs(execution),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_TO_SURFACE_MAPPING_METADATA",
    "VolumeToSurfaceMappingMyelinStyle",
    "VolumeToSurfaceMappingMyelinStyleOutputs",
    "VolumeToSurfaceMappingOutputWeights",
    "VolumeToSurfaceMappingOutputWeightsOutputs",
    "VolumeToSurfaceMappingOutputs",
    "VolumeToSurfaceMappingRibbonConstrained",
    "VolumeToSurfaceMappingRibbonConstrainedOutputs",
    "VolumeToSurfaceMappingVolumeRoi",
    "VolumeToSurfaceMappingVolumeRoiOutputs",
    "volume_to_surface_mapping",
]
