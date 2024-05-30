# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


CIFTI_CREATE_LABEL_METADATA = Metadata(
    id="0afb731c477ef6b2e637638972fd28d69d2ce20f",
    name="cifti-create-label",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class CiftiCreateLabelVolumeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `CiftiCreateLabelVolume.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class CiftiCreateLabelVolume:
    """
    volume component
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
    ) -> CiftiCreateLabelVolumeOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `CiftiCreateLabelVolumeOutputs`).
        """
        ret = CiftiCreateLabelVolumeOutputs(
            root=execution.output_file("."),
        )
        return ret


class CiftiCreateLabelLeftLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `CiftiCreateLabelLeftLabel.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class CiftiCreateLabelLeftLabel:
    """
    label file for left surface
    """
    opt_roi_left_roi_metric: InputPathType | None = None
    """roi of vertices to use from left surface: the ROI as a metric file"""
    
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
        if self.opt_roi_left_roi_metric is not None:
            cargs.extend(["-roi-left", execution.input_file(self.opt_roi_left_roi_metric)])
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> CiftiCreateLabelLeftLabelOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `CiftiCreateLabelLeftLabelOutputs`).
        """
        ret = CiftiCreateLabelLeftLabelOutputs(
            root=execution.output_file("."),
        )
        return ret


class CiftiCreateLabelRightLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `CiftiCreateLabelRightLabel.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class CiftiCreateLabelRightLabel:
    """
    label for left surface
    """
    opt_roi_right_roi_metric: InputPathType | None = None
    """roi of vertices to use from right surface: the ROI as a metric file"""
    
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
        if self.opt_roi_right_roi_metric is not None:
            cargs.extend(["-roi-right", execution.input_file(self.opt_roi_right_roi_metric)])
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> CiftiCreateLabelRightLabelOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `CiftiCreateLabelRightLabelOutputs`).
        """
        ret = CiftiCreateLabelRightLabelOutputs(
            root=execution.output_file("."),
        )
        return ret


class CiftiCreateLabelCerebellumLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `CiftiCreateLabelCerebellumLabel.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class CiftiCreateLabelCerebellumLabel:
    """
    label for the cerebellum
    """
    opt_roi_cerebellum_roi_metric: InputPathType | None = None
    """roi of vertices to use from right surface: the ROI as a metric file"""
    
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
        if self.opt_roi_cerebellum_roi_metric is not None:
            cargs.extend(["-roi-cerebellum", execution.input_file(self.opt_roi_cerebellum_roi_metric)])
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> CiftiCreateLabelCerebellumLabelOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `CiftiCreateLabelCerebellumLabelOutputs`).
        """
        ret = CiftiCreateLabelCerebellumLabelOutputs(
            root=execution.output_file("."),
        )
        return ret


class CiftiCreateLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_create_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""
    volume: CiftiCreateLabelVolumeOutputs
    """Subcommand outputs"""
    left_label: CiftiCreateLabelLeftLabelOutputs
    """Subcommand outputs"""
    right_label: CiftiCreateLabelRightLabelOutputs
    """Subcommand outputs"""
    cerebellum_label: CiftiCreateLabelCerebellumLabelOutputs
    """Subcommand outputs"""


def cifti_create_label(
    cifti_out: InputPathType,
    volume: CiftiCreateLabelVolume | None = None,
    left_label: CiftiCreateLabelLeftLabel | None = None,
    right_label: CiftiCreateLabelRightLabel | None = None,
    cerebellum_label: CiftiCreateLabelCerebellumLabel | None = None,
    runner: Runner = None,
) -> CiftiCreateLabelOutputs:
    """
    cifti-create-label by Washington University School of Medicin.
    
    Create a cifti label file.
    
    All input files must have the same number of columns/subvolumes. Only the
    specified components will be in the output cifti. At least one component
    must be specified.
    
    The -volume option requires two volume arguments, the label-volume argument
    contains all labels you want to display (e.g. nuclei of the thalamus),
    whereas the structure-label-volume argument contains all CIFTI voxel-based
    structures you want to include data within (e.g. THALAMUS_LEFT,
    THALAMUS_RIGHT, etc). See -volume-label-import and -volume-help for format
    details of label volume files. If you just want the labels in voxels to be
    the structure names, you may use the same file for both arguments. The
    structure-label-volume must use some of the label names from this list, all
    other label names in the structure-label-volume will be ignored:
    
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
        cifti_out: the output cifti file
        volume: volume component
        left_label: label file for left surface
        right_label: label for left surface
        cerebellum_label: label for the cerebellum
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiCreateLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CREATE_LABEL_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-create-label")
    cargs.append(execution.input_file(cifti_out))
    if volume is not None:
        cargs.extend(["-volume", *volume.run(execution)])
    if left_label is not None:
        cargs.extend(["-left-label", *left_label.run(execution)])
    if right_label is not None:
        cargs.extend(["-right-label", *right_label.run(execution)])
    if cerebellum_label is not None:
        cargs.extend(["-cerebellum-label", *cerebellum_label.run(execution)])
    ret = CiftiCreateLabelOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).name}"),
        volume=volume.outputs(execution),
        left_label=left_label.outputs(execution),
        right_label=right_label.outputs(execution),
        cerebellum_label=cerebellum_label.outputs(execution),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_CREATE_LABEL_METADATA",
    "CiftiCreateLabelCerebellumLabel",
    "CiftiCreateLabelCerebellumLabelOutputs",
    "CiftiCreateLabelLeftLabel",
    "CiftiCreateLabelLeftLabelOutputs",
    "CiftiCreateLabelOutputs",
    "CiftiCreateLabelRightLabel",
    "CiftiCreateLabelRightLabelOutputs",
    "CiftiCreateLabelVolume",
    "CiftiCreateLabelVolumeOutputs",
    "cifti_create_label",
]
