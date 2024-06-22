# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_ERODE_METADATA = Metadata(
    id="8c37d80eed4e28581f0a93bc7798d680591a6441",
    name="cifti-erode",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiErodeLeftSurface:
    """
    specify the left surface to use
    """
    surface: InputPathType
    """the left surface file"""
    opt_left_corrected_areas_area_metric: InputPathType | None = None
    """vertex areas to use instead of computing them from the left surface: the
    corrected vertex areas, as a metric"""
    
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
        cargs.append("-left-surface")
        cargs.append(execution.input_file(self.surface))
        if self.opt_left_corrected_areas_area_metric is not None:
            cargs.extend(["-left-corrected-areas", execution.input_file(self.opt_left_corrected_areas_area_metric)])
        return cargs


@dataclasses.dataclass
class CiftiErodeRightSurface:
    """
    specify the right surface to use
    """
    surface: InputPathType
    """the right surface file"""
    opt_right_corrected_areas_area_metric: InputPathType | None = None
    """vertex areas to use instead of computing them from the right surface: the
    corrected vertex areas, as a metric"""
    
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
        cargs.append("-right-surface")
        cargs.append(execution.input_file(self.surface))
        if self.opt_right_corrected_areas_area_metric is not None:
            cargs.extend(["-right-corrected-areas", execution.input_file(self.opt_right_corrected_areas_area_metric)])
        return cargs


@dataclasses.dataclass
class CiftiErodeCerebellumSurface:
    """
    specify the cerebellum surface to use
    """
    surface: InputPathType
    """the cerebellum surface file"""
    opt_cerebellum_corrected_areas_area_metric: InputPathType | None = None
    """vertex areas to use instead of computing them from the cerebellum
    surface: the corrected vertex areas, as a metric"""
    
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
        cargs.append("-cerebellum-surface")
        cargs.append(execution.input_file(self.surface))
        if self.opt_cerebellum_corrected_areas_area_metric is not None:
            cargs.extend(["-cerebellum-corrected-areas", execution.input_file(self.opt_cerebellum_corrected_areas_area_metric)])
        return cargs


class CiftiErodeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_erode(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_erode(
    cifti_in: InputPathType,
    direction: str,
    surface_distance: float | int,
    volume_distance: float | int,
    cifti_out: InputPathType,
    left_surface: CiftiErodeLeftSurface | None = None,
    right_surface: CiftiErodeRightSurface | None = None,
    cerebellum_surface: CiftiErodeCerebellumSurface | None = None,
    opt_merged_volume: bool = False,
    runner: Runner = None,
) -> CiftiErodeOutputs:
    """
    cifti-erode by Washington University School of Medicin.
    
    Erode a cifti file.
    
    For all data values that are empty (for label data, unlabeled, for other
    data, zero), set the surrounding values to empty. The surrounding values are
    defined as the immediate neighbors and all values in the same structure
    within the specified distance (-merged-volume treats all voxels as one
    structure).
    
    The -*-corrected-areas options are intended for eroding on group average
    surfaces, but it is only an approximate correction.
    
    Args:
        cifti_in: the input cifti file.
        direction: which dimension to dilate along, ROW or COLUMN.
        surface_distance: the distance to dilate on surfaces, in mm.
        volume_distance: the distance to dilate in the volume, in mm.
        cifti_out: the output cifti file.
        left_surface: specify the left surface to use.
        right_surface: specify the right surface to use.
        cerebellum_surface: specify the cerebellum surface to use.
        opt_merged_volume: treat volume components as if they were a single\
            component.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiErodeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_ERODE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-erode")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(direction)
    cargs.append(str(surface_distance))
    cargs.append(str(volume_distance))
    cargs.append(execution.input_file(cifti_out))
    if left_surface is not None:
        cargs.extend(left_surface.run(execution))
    if right_surface is not None:
        cargs.extend(right_surface.run(execution))
    if cerebellum_surface is not None:
        cargs.extend(cerebellum_surface.run(execution))
    if opt_merged_volume:
        cargs.append("-merged-volume")
    ret = CiftiErodeOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_ERODE_METADATA",
    "CiftiErodeCerebellumSurface",
    "CiftiErodeLeftSurface",
    "CiftiErodeOutputs",
    "CiftiErodeRightSurface",
    "cifti_erode",
]
