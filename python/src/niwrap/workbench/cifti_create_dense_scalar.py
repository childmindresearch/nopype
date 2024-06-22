# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_CREATE_DENSE_SCALAR_METADATA = Metadata(
    id="613cf7385396ea60b872f82b84a297d05dcea4c3",
    name="cifti-create-dense-scalar",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiCreateDenseScalarVolume:
    """
    volume component
    """
    volume_data: InputPathType
    """volume file containing all voxel data for all volume structures"""
    structure_label_volume: InputPathType
    """label volume file containing labels for cifti structures"""
    
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
        cargs.append(execution.input_file(self.volume_data))
        cargs.append(execution.input_file(self.structure_label_volume))
        return cargs


@dataclasses.dataclass
class CiftiCreateDenseScalarLeftMetric:
    """
    metric for left surface
    """
    metric: InputPathType
    """the metric file"""
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
        cargs.append("-left-metric")
        cargs.append(execution.input_file(self.metric))
        if self.opt_roi_left_roi_metric is not None:
            cargs.extend(["-roi-left", execution.input_file(self.opt_roi_left_roi_metric)])
        return cargs


@dataclasses.dataclass
class CiftiCreateDenseScalarRightMetric:
    """
    metric for right surface
    """
    metric: InputPathType
    """the metric file"""
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
        cargs.append("-right-metric")
        cargs.append(execution.input_file(self.metric))
        if self.opt_roi_right_roi_metric is not None:
            cargs.extend(["-roi-right", execution.input_file(self.opt_roi_right_roi_metric)])
        return cargs


@dataclasses.dataclass
class CiftiCreateDenseScalarCerebellumMetric:
    """
    metric for the cerebellum
    """
    metric: InputPathType
    """the metric file"""
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
        cargs.append("-cerebellum-metric")
        cargs.append(execution.input_file(self.metric))
        if self.opt_roi_cerebellum_roi_metric is not None:
            cargs.extend(["-roi-cerebellum", execution.input_file(self.opt_roi_cerebellum_roi_metric)])
        return cargs


class CiftiCreateDenseScalarOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_create_dense_scalar(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_create_dense_scalar(
    cifti_out: InputPathType,
    volume: CiftiCreateDenseScalarVolume | None = None,
    left_metric: CiftiCreateDenseScalarLeftMetric | None = None,
    right_metric: CiftiCreateDenseScalarRightMetric | None = None,
    cerebellum_metric: CiftiCreateDenseScalarCerebellumMetric | None = None,
    opt_name_file_file: str | None = None,
    runner: Runner = None,
) -> CiftiCreateDenseScalarOutputs:
    """
    cifti-create-dense-scalar by Washington University School of Medicin.
    
    Create a cifti dense scalar file.
    
    All input files must have the same number of columns/subvolumes. Only the
    specified components will be in the output cifti file. Map names will be
    taken from one of the input files. At least one component must be specified.
    
    See -volume-label-import and -volume-help for format details of label volume
    files. The structure-label-volume should have some of the label names from
    this list, all other label names will be ignored:
    
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
        cifti_out: the output cifti file.
        volume: volume component.
        left_metric: metric for left surface.
        right_metric: metric for right surface.
        cerebellum_metric: metric for the cerebellum.
        opt_name_file_file: use a text file to set all map names: text file\
            containing map names, one per line.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiCreateDenseScalarOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CREATE_DENSE_SCALAR_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-create-dense-scalar")
    cargs.append(execution.input_file(cifti_out))
    if volume is not None:
        cargs.extend(volume.run(execution))
    if left_metric is not None:
        cargs.extend(left_metric.run(execution))
    if right_metric is not None:
        cargs.extend(right_metric.run(execution))
    if cerebellum_metric is not None:
        cargs.extend(cerebellum_metric.run(execution))
    if opt_name_file_file is not None:
        cargs.extend(["-name-file", opt_name_file_file])
    ret = CiftiCreateDenseScalarOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_CREATE_DENSE_SCALAR_METADATA",
    "CiftiCreateDenseScalarCerebellumMetric",
    "CiftiCreateDenseScalarLeftMetric",
    "CiftiCreateDenseScalarOutputs",
    "CiftiCreateDenseScalarRightMetric",
    "CiftiCreateDenseScalarVolume",
    "cifti_create_dense_scalar",
]
