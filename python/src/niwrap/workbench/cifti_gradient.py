# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


CIFTI_GRADIENT_METADATA = Metadata(
    id="a9239854842b00d4fe0dc93f4ae227d407c95995",
    name="cifti-gradient",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class CiftiGradientLeftSurfaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `CiftiGradientLeftSurface.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class CiftiGradientLeftSurface:
    """
    specify the left surface to use
    """
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
        if self.opt_left_corrected_areas_area_metric is not None:
            cargs.extend(["-left-corrected-areas", execution.input_file(self.opt_left_corrected_areas_area_metric)])
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> CiftiGradientLeftSurfaceOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `CiftiGradientLeftSurfaceOutputs`).
        """
        ret = CiftiGradientLeftSurfaceOutputs(
            root=execution.output_file("."),
        )
        return ret


class CiftiGradientRightSurfaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `CiftiGradientRightSurface.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class CiftiGradientRightSurface:
    """
    specify the right surface to use
    """
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
        if self.opt_right_corrected_areas_area_metric is not None:
            cargs.extend(["-right-corrected-areas", execution.input_file(self.opt_right_corrected_areas_area_metric)])
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> CiftiGradientRightSurfaceOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `CiftiGradientRightSurfaceOutputs`).
        """
        ret = CiftiGradientRightSurfaceOutputs(
            root=execution.output_file("."),
        )
        return ret


class CiftiGradientCerebellumSurfaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `CiftiGradientCerebellumSurface.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class CiftiGradientCerebellumSurface:
    """
    specify the cerebellum surface to use
    """
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
        if self.opt_cerebellum_corrected_areas_area_metric is not None:
            cargs.extend(["-cerebellum-corrected-areas", execution.input_file(self.opt_cerebellum_corrected_areas_area_metric)])
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> CiftiGradientCerebellumSurfaceOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `CiftiGradientCerebellumSurfaceOutputs`).
        """
        ret = CiftiGradientCerebellumSurfaceOutputs(
            root=execution.output_file("."),
        )
        return ret


class CiftiGradientOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_gradient(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti"""
    vectors_out: OutputPathType
    """the vectors, as a dscalar file"""
    left_surface: CiftiGradientLeftSurfaceOutputs
    """Subcommand outputs"""
    right_surface: CiftiGradientRightSurfaceOutputs
    """Subcommand outputs"""
    cerebellum_surface: CiftiGradientCerebellumSurfaceOutputs
    """Subcommand outputs"""


def cifti_gradient(
    cifti: InputPathType,
    direction: str,
    cifti_out: InputPathType,
    vectors_out: InputPathType,
    left_surface: CiftiGradientLeftSurface | None = None,
    right_surface: CiftiGradientRightSurface | None = None,
    cerebellum_surface: CiftiGradientCerebellumSurface | None = None,
    opt_surface_presmooth_surface_kernel: float | int | None = None,
    opt_volume_presmooth_volume_kernel: float | int | None = None,
    opt_presmooth_fwhm: bool = False,
    opt_average_output: bool = False,
    opt_vectors: bool = False,
    runner: Runner = None,
) -> CiftiGradientOutputs:
    """
    cifti-gradient by Washington University School of Medicin.
    
    Take gradient of a cifti file.
    
    Performs gradient calculation on each component of the cifti file, and
    optionally averages the resulting gradients. The -vectors and
    -average-output options may not be used together. You must specify a surface
    for each surface structure in the cifti file. The COLUMN direction should be
    faster, and is the direction that works on dtseries. For dconn, you probably
    want ROW, unless you are using -average-output.
    
    Args:
        cifti: the input cifti
        direction: which dimension to take the gradient along, ROW or COLUMN
        cifti_out: the output cifti
        vectors_out: the vectors, as a dscalar file
        left_surface: specify the left surface to use
        right_surface: specify the right surface to use
        cerebellum_surface: specify the cerebellum surface to use
        opt_surface_presmooth_surface_kernel: smooth on the surface before
            computing the gradient: the size of the gaussian surface smoothing
            kernel in mm, as sigma by default
        opt_volume_presmooth_volume_kernel: smooth on the surface before
            computing the gradient: the size of the gaussian volume smoothing kernel
            in mm, as sigma by default
        opt_presmooth_fwhm: smoothing kernel sizes are FWHM, not sigma
        opt_average_output: output the average of the gradient magnitude maps
            instead of each gradient map separately
        opt_vectors: output gradient vectors
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiGradientOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_GRADIENT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-gradient")
    cargs.append(execution.input_file(cifti))
    cargs.append(direction)
    cargs.append(execution.input_file(cifti_out))
    if left_surface is not None:
        cargs.extend(["-left-surface", *left_surface.run(execution)])
    if right_surface is not None:
        cargs.extend(["-right-surface", *right_surface.run(execution)])
    if cerebellum_surface is not None:
        cargs.extend(["-cerebellum-surface", *cerebellum_surface.run(execution)])
    if opt_surface_presmooth_surface_kernel is not None:
        cargs.extend(["-surface-presmooth", str(opt_surface_presmooth_surface_kernel)])
    if opt_volume_presmooth_volume_kernel is not None:
        cargs.extend(["-volume-presmooth", str(opt_volume_presmooth_volume_kernel)])
    if opt_presmooth_fwhm:
        cargs.append("-presmooth-fwhm")
    if opt_average_output:
        cargs.append("-average-output")
    if opt_vectors:
        cargs.append("-vectors")
    cargs.append(execution.input_file(vectors_out))
    ret = CiftiGradientOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).name}"),
        vectors_out=execution.output_file(f"{pathlib.Path(vectors_out).name}"),
        left_surface=left_surface.outputs(execution),
        right_surface=right_surface.outputs(execution),
        cerebellum_surface=cerebellum_surface.outputs(execution),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_GRADIENT_METADATA",
    "CiftiGradientCerebellumSurface",
    "CiftiGradientCerebellumSurfaceOutputs",
    "CiftiGradientLeftSurface",
    "CiftiGradientLeftSurfaceOutputs",
    "CiftiGradientOutputs",
    "CiftiGradientRightSurface",
    "CiftiGradientRightSurfaceOutputs",
    "cifti_gradient",
]
