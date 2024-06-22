# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

METRIC_PALETTE_METADATA = Metadata(
    id="8ef21839245d8392415b18db0209c772abc4fd46",
    name="metric-palette",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class MetricPalettePosPercent:
    """
    percentage min/max for positive data coloring
    """
    pos_min__: float | int
    """the percentile for the least positive data"""
    pos_max__: float | int
    """the percentile for the most positive data"""
    
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
        cargs.append("-pos-percent")
        cargs.append(str(self.pos_min__))
        cargs.append(str(self.pos_max__))
        return cargs


@dataclasses.dataclass
class MetricPaletteNegPercent:
    """
    percentage min/max for negative data coloring
    """
    neg_min__: float | int
    """the percentile for the least negative data"""
    neg_max__: float | int
    """the percentile for the most negative data"""
    
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
        cargs.append("-neg-percent")
        cargs.append(str(self.neg_min__))
        cargs.append(str(self.neg_max__))
        return cargs


@dataclasses.dataclass
class MetricPalettePosUser:
    """
    user min/max values for positive data coloring
    """
    pos_min_user: float | int
    """the value for the least positive data"""
    pos_max_user: float | int
    """the value for the most positive data"""
    
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
        cargs.append("-pos-user")
        cargs.append(str(self.pos_min_user))
        cargs.append(str(self.pos_max_user))
        return cargs


@dataclasses.dataclass
class MetricPaletteNegUser:
    """
    user min/max values for negative data coloring
    """
    neg_min_user: float | int
    """the value for the least negative data"""
    neg_max_user: float | int
    """the value for the most negative data"""
    
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
        cargs.append("-neg-user")
        cargs.append(str(self.neg_min_user))
        cargs.append(str(self.neg_max_user))
        return cargs


@dataclasses.dataclass
class MetricPaletteThresholding:
    """
    set the thresholding
    """
    type_: str
    """thresholding setting"""
    test: str
    """show values inside or outside thresholds"""
    min_: float | int
    """lower threshold"""
    max_: float | int
    """upper threshold"""
    
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
        cargs.append("-thresholding")
        cargs.append(self.type_)
        cargs.append(self.test)
        cargs.append(str(self.min_))
        cargs.append(str(self.max_))
        return cargs


class MetricPaletteOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_palette(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def metric_palette(
    metric: str,
    mode: str,
    opt_column_column: str | None = None,
    pos_percent: MetricPalettePosPercent | None = None,
    neg_percent: MetricPaletteNegPercent | None = None,
    pos_user: MetricPalettePosUser | None = None,
    neg_user: MetricPaletteNegUser | None = None,
    opt_interpolate_interpolate: typing.Literal["true", "false"] | None = None,
    opt_disp_pos_display: typing.Literal["true", "false"] | None = None,
    opt_disp_neg_display: typing.Literal["true", "false"] | None = None,
    opt_disp_zero_display: typing.Literal["true", "false"] | None = None,
    opt_palette_name_name: str | None = None,
    thresholding: MetricPaletteThresholding | None = None,
    opt_inversion_type: str | None = None,
    runner: Runner = None,
) -> MetricPaletteOutputs:
    """
    metric-palette by Washington University School of Medicin.
    
    Set the palette of a metric file.
    
    The original metric file is overwritten with the modified version. By
    default, all columns of the metric file are adjusted to the new settings,
    use the -column option to change only one column. Mapping settings not
    specified in options will be taken from the first column. The <mode>
    argument must be one of the following:
    
    MODE_AUTO_SCALE
    MODE_AUTO_SCALE_ABSOLUTE_PERCENTAGE
    MODE_AUTO_SCALE_PERCENTAGE
    MODE_USER_SCALE
    
    The <name> argument to -palette-name must be one of the following:
    
    ROY-BIG-BL
    videen_style
    Gray_Interp_Positive
    Gray_Interp
    PSYCH-FIXED
    RBGYR20
    RBGYR20P
    RYGBR4_positive
    RGRBR_mirror90_pos
    Orange-Yellow
    POS_NEG_ZERO
    red-yellow
    blue-lightblue
    FSL
    power_surf
    black-red
    black-green
    black-blue
    black-red-positive
    black-green-positive
    black-blue-positive
    blue-black-green
    blue-black-red
    red-black-green
    fsl_red
    fsl_green
    fsl_blue
    fsl_yellow
    RedWhiteBlue
    cool-warm
    spectral
    RY-BC-BL
    magma
    JET256
    PSYCH
    PSYCH-NO-NONE
    ROY-BIG
    clear_brain
    fidl
    raich4_clrmid
    raich6_clrmid
    HSB8_clrmid
    POS_NEG
    Special-RGB-Volume
    
    The <type> argument to -thresholding must be one of the following:
    
    THRESHOLD_TYPE_OFF
    THRESHOLD_TYPE_NORMAL
    THRESHOLD_TYPE_FILE
    
    The <test> argument to -thresholding must be one of the following:
    
    THRESHOLD_TEST_SHOW_OUTSIDE
    THRESHOLD_TEST_SHOW_INSIDE
    
    The <type> argument to -inversion must be one of the following:
    
    OFF
    POSITIVE_WITH_NEGATIVE
    POSITIVE_NEGATIVE_SEPARATE
    .
    
    Args:
        metric: the metric to modify.
        mode: the mapping mode.
        opt_column_column: select a single column: the column number or name.
        pos_percent: percentage min/max for positive data coloring.
        neg_percent: percentage min/max for negative data coloring.
        pos_user: user min/max values for positive data coloring.
        neg_user: user min/max values for negative data coloring.
        opt_interpolate_interpolate: interpolate colors: boolean, whether to\
            interpolate.
        opt_disp_pos_display: display positive data: boolean, whether to\
            display.
        opt_disp_neg_display: display positive data: boolean, whether to\
            display.
        opt_disp_zero_display: display data closer to zero than the min cutoff:\
            boolean, whether to display.
        opt_palette_name_name: set the palette used: the name of the palette.
        thresholding: set the thresholding.
        opt_inversion_type: specify palette inversion: the type of inversion.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricPaletteOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_PALETTE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-palette")
    cargs.append(metric)
    cargs.append(mode)
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if pos_percent is not None:
        cargs.extend(pos_percent.run(execution))
    if neg_percent is not None:
        cargs.extend(neg_percent.run(execution))
    if pos_user is not None:
        cargs.extend(pos_user.run(execution))
    if neg_user is not None:
        cargs.extend(neg_user.run(execution))
    if opt_interpolate_interpolate is not None:
        cargs.extend(["-interpolate", opt_interpolate_interpolate])
    if opt_disp_pos_display is not None:
        cargs.extend(["-disp-pos", opt_disp_pos_display])
    if opt_disp_neg_display is not None:
        cargs.extend(["-disp-neg", opt_disp_neg_display])
    if opt_disp_zero_display is not None:
        cargs.extend(["-disp-zero", opt_disp_zero_display])
    if opt_palette_name_name is not None:
        cargs.extend(["-palette-name", opt_palette_name_name])
    if thresholding is not None:
        cargs.extend(thresholding.run(execution))
    if opt_inversion_type is not None:
        cargs.extend(["-inversion", opt_inversion_type])
    ret = MetricPaletteOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_PALETTE_METADATA",
    "MetricPaletteNegPercent",
    "MetricPaletteNegUser",
    "MetricPaletteOutputs",
    "MetricPalettePosPercent",
    "MetricPalettePosUser",
    "MetricPaletteThresholding",
    "metric_palette",
]
