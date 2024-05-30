# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


FSLMATHS_METADATA = Metadata(
    id="9df99322110fade52cf95cfd6bb59da632a223ef",
    name="fslmaths",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class FslmathsOperationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `FslmathsOperation.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class FslmathsOperation:
    """
    Operation to perform on input images
    """
    add: float | int | None = None
    """Add following input to current image"""
    sub: float | int | None = None
    """Subtract following input from current image"""
    mul: float | int | None = None
    """Multiply current image by following input"""
    div: float | int | None = None
    """Divide current image by following input"""
    rem: float | int | None = None
    """Modulus remainder - divide current image by following input and take
    remainder"""
    mas: InputPathType | None = None
    """Use (following image>0) to mask current image"""
    thr: float | int | None = None
    """Use following number to threshold current image (zero anything below the
    number)"""
    thrp: float | int | None = None
    """Use following percentage (0-100) of ROBUST RANGE to threshold current
    image (zero anything below the number)"""
    thr_p: float | int | None = None
    """Use following percentage (0-100) of ROBUST RANGE of non-zero voxels and
    threshold below"""
    uthr: float | int | None = None
    """Use following number to upper-threshold current image (zero anything
    above the number)"""
    uthrp: float | int | None = None
    """Use following percentage (0-100) of ROBUST RANGE to upper-threshold
    current image (zero anything above the number)"""
    uthr_p: float | int | None = None
    """Use following percentage (0-100) of ROBUST RANGE of non-zero voxels and
    threshold above"""
    max_: float | int | None = None
    """Take maximum of following input and current image"""
    min_: float | int | None = None
    """Take minimum of following input and current image"""
    seed: float | int | None = None
    """Seed random number generator with following number"""
    restart: InputPathType | None = None
    """Replace the current image with input for future processing operations"""
    save: bool = False
    """Save the current working image to the input filename"""
    exp: bool = False
    """Exponential"""
    log: bool = False
    """Natural logarithm"""
    sin: bool = False
    """Sine function"""
    cos: bool = False
    """Cosine function"""
    tan: bool = False
    """Tangent function"""
    asin: bool = False
    """Arc sine function"""
    acos: bool = False
    """Arc cosine function"""
    atan: bool = False
    """Arc tangent function"""
    sqr: bool = False
    """Square"""
    sqrt: bool = False
    """Square root"""
    recip: bool = False
    """Reciprocal (1/current image)"""
    abs_: bool = False
    """Absolute value"""
    bin_: bool = False
    """Use (current image>0) to binarise"""
    binv: bool = False
    """Binarise and invert (binarisation and logical inversion)"""
    fillh: bool = False
    """Fill holes in a binary mask (holes are internal - i.e. do not touch the
    edge of the FOV)"""
    fillh26: bool = False
    """Fill holes using 26 connectivity"""
    index: bool = False
    """Replace each nonzero voxel with a unique (subject to wrapping) index
    number"""
    grid: list[float | int] = None
    """Add a 3D grid of intensity <value> with grid spacing <spacing>"""
    edge: bool = False
    """Edge strength"""
    tfce: list[float | int] = None
    """Enhance with TFCE, e.g. -tfce 2 0.5 6 (maybe change 6 to 26 for
    skeletons)"""
    tfce_s: list[float | int] = None
    """Show support area for voxel (X,Y,Z)"""
    nan: bool = False
    """Replace NaNs (improper numbers) with 0"""
    nanm: bool = False
    """Make NaN (improper number) mask with 1 for NaN voxels, 0 otherwise"""
    rand: bool = False
    """Add uniform noise (range 0:1)"""
    randn: bool = False
    """Add Gaussian noise (mean=0 sigma=1)"""
    inm: float | int | None = None
    """Intensity normalisation (per 3D volume mean)"""
    ing: float | int | None = None
    """Intensity normalisation, global 4D mean"""
    range_: bool = False
    """Set the output calmin/max to full data range"""
    tensor_decomp: bool = False
    """Convert a 4D (6-timepoint) tensor image into L1,2,3,FA,MD,MO,V1,2,3
    (remaining image in pipeline is FA)"""
    kernel_3_d: bool = False
    """3x3x3 box centered on target voxel (set as default kernel)"""
    kernel_2_d: bool = False
    """3x3x1 box centered on target voxel"""
    kernel_box: float | int | None = None
    """All voxels in a cube of width <size> mm centered on target voxel"""
    kernel_boxv: float | int | None = None
    """All voxels in a cube of width <size> voxels centered on target voxel"""
    kernel_boxv3: list[float | int] = None
    """All voxels in a cuboid of dimensions X x Y x Z centered on target
    voxel"""
    kernel_gauss: float | int | None = None
    """Gaussian kernel (sigma in mm, not voxels)"""
    kernel_sphere: float | int | None = None
    """All voxels in a sphere of radius <size> mm centered on target voxel"""
    kernel_file: InputPathType | None = None
    """Use external file as kernel"""
    dil_m: bool = False
    """Mean Dilation of non-zero voxels"""
    dil_d: bool = False
    """Modal Dilation of non-zero voxels"""
    dil_f: bool = False
    """Maximum filtering of all voxels"""
    dilall: bool = False
    """Apply -dilM repeatedly until the entire FOV is covered"""
    ero: bool = False
    """Erode by zeroing non-zero voxels when zero voxels found in kernel"""
    ero_f: bool = False
    """Minimum filtering of all voxels"""
    fmedian: bool = False
    """Median Filtering"""
    fmean: bool = False
    """Mean filtering, kernel weighted (conventionally used with gauss
    kernel)"""
    fmeanu: bool = False
    """Mean filtering, kernel weighted, un-normalised (gives edge effects)"""
    s: float | int | None = None
    """Create a gauss kernel of sigma mm and perform mean filtering"""
    subsamp2: bool = False
    """Downsamples image by a factor of 2 (keeping new voxels centred on old)"""
    subsamp2offc: bool = False
    """Downsamples image by a factor of 2 (non-centred)"""
    tmean: bool = False
    """Mean across time"""
    xmean: bool = False
    """Mean across X axis"""
    ymean: bool = False
    """Mean across Y axis"""
    zmean: bool = False
    """Mean across Z axis"""
    tstd: bool = False
    """Standard deviation across time"""
    xstd: bool = False
    """Standard deviation across X axis"""
    ystd: bool = False
    """Standard deviation across Y axis"""
    zstd: bool = False
    """Standard deviation across Z axis"""
    tmax: bool = False
    """Max across time"""
    xmax: bool = False
    """Max across X axis"""
    ymax: bool = False
    """Max across Y axis"""
    zmax: bool = False
    """Max across Z axis"""
    tmaxn: bool = False
    """Time index of max across time"""
    xmaxn: bool = False
    """X index of max across X axis"""
    ymaxn: bool = False
    """Y index of max across Y axis"""
    zmaxn: bool = False
    """Z index of max across Z axis"""
    tmin: bool = False
    """Min across time"""
    xmin: bool = False
    """Min across X axis"""
    ymin: bool = False
    """Min across Y axis"""
    zmin: bool = False
    """Min across Z axis"""
    tmedian: bool = False
    """Median across time"""
    xmedian: bool = False
    """Median across X axis"""
    ymedian: bool = False
    """Median across Y axis"""
    zmedian: bool = False
    """Median across Z axis"""
    tperc: float | int | None = None
    """Nth percentile (0-100) of FULL RANGE across time"""
    xperc: float | int | None = None
    """Nth percentile (0-100) of FULL RANGE across X axis"""
    yperc: float | int | None = None
    """Nth percentile (0-100) of FULL RANGE across Y axis"""
    zperc: float | int | None = None
    """Nth percentile (0-100) of FULL RANGE across Z axis"""
    tar1: bool = False
    """Temporal AR(1) coefficient (use -odt float and probably demean first)"""
    roi: list[float | int] = None
    """<xmin> <xsize> <ymin> <ysize> <zmin> <zsize> <tmin> <tsize>. Zero outside
    roi (using voxel coordinates). Inputting -1 for a size will set it to the
    full image extent for that dimension."""
    bptf: list[float | int] = None
    """<lowpass> <highpass>. Bandpass temporal filtering (use -odt float and
    probably demean first)"""
    roc: list[float | int] = None
    """<threshold> <output>. ROC analysis"""
    
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
        if self.thrp is not None and not (0 <= self.thrp <= 100): 
            raise ValueError(f"'self.thrp' must be between 0 <= x <= 100 but was {self.thrp}")
        if self.thr_p is not None and not (0 <= self.thr_p <= 100): 
            raise ValueError(f"'self.thr_p' must be between 0 <= x <= 100 but was {self.thr_p}")
        if self.uthrp is not None and not (0 <= self.uthrp <= 100): 
            raise ValueError(f"'self.uthrp' must be between 0 <= x <= 100 but was {self.uthrp}")
        if self.uthr_p is not None and not (0 <= self.uthr_p <= 100): 
            raise ValueError(f"'self.uthr_p' must be between 0 <= x <= 100 but was {self.uthr_p}")
        if self.kernel_boxv3 is not None and (len(self.kernel_boxv3) != 3): 
            raise ValueError(f"Length of 'self.kernel_boxv3' must be 3 but was {len(self.kernel_boxv3)}")
        if self.tperc is not None and not (0 <= self.tperc <= 100): 
            raise ValueError(f"'self.tperc' must be between 0 <= x <= 100 but was {self.tperc}")
        if self.xperc is not None and not (0 <= self.xperc <= 100): 
            raise ValueError(f"'self.xperc' must be between 0 <= x <= 100 but was {self.xperc}")
        if self.yperc is not None and not (0 <= self.yperc <= 100): 
            raise ValueError(f"'self.yperc' must be between 0 <= x <= 100 but was {self.yperc}")
        if self.zperc is not None and not (0 <= self.zperc <= 100): 
            raise ValueError(f"'self.zperc' must be between 0 <= x <= 100 but was {self.zperc}")
        if self.roi is not None and (len(self.roi) != 6): 
            raise ValueError(f"Length of 'self.roi' must be 6 but was {len(self.roi)}")
        if self.bptf is not None and (len(self.bptf) != 2): 
            raise ValueError(f"Length of 'self.bptf' must be 2 but was {len(self.bptf)}")
        if (
            (self.add is not None) +
            (self.sub is not None) +
            (self.mul is not None) +
            (self.div is not None) +
            (self.rem is not None) +
            (self.mas is not None) +
            (self.thr is not None) +
            (self.thrp is not None) +
            (self.thr_p is not None) +
            (self.uthr is not None) +
            (self.uthrp is not None) +
            (self.uthr_p is not None) +
            (self.max_ is not None) +
            (self.min_ is not None)
        ) > 1:
            raise ValueError(
                "Only one of the following arguments can be specified:\n"
                "add,\n"
                "sub,\n"
                "mul,\n"
                "div,\n"
                "rem,\n"
                "mas,\n"
                "thr,\n"
                "thrp,\n"
                "thrP,\n"
                "uthr,\n"
                "uthrp,\n"
                "uthrP,\n"
                "max,\n"
                "min"
            )
        if (
            self.exp +
            self.log +
            self.sin +
            self.cos +
            self.tan +
            self.asin +
            self.acos +
            self.atan +
            self.sqr +
            self.sqrt +
            self.recip +
            self.abs_ +
            self.bin_ +
            self.binv +
            self.fillh
        ) > 1:
            raise ValueError(
                "Only one of the following arguments can be specified:\n"
                "exp,\n"
                "log,\n"
                "sin,\n"
                "cos,\n"
                "tan,\n"
                "asin,\n"
                "acos,\n"
                "atan,\n"
                "sqr,\n"
                "sqrt,\n"
                "recip,\n"
                "abs,\n"
                "bin,\n"
                "binv,\n"
                "fillh"
            )
        if (
            self.tmean +
            self.xmean +
            self.ymean +
            self.zmean +
            self.tstd +
            self.xstd +
            self.ystd +
            self.zstd +
            self.tmax +
            self.xmax +
            self.ymax +
            self.zmax +
            self.tmaxn +
            self.xmaxn +
            self.ymaxn +
            self.zmaxn +
            self.tmin +
            self.xmin +
            self.ymin +
            self.zmin +
            self.tmedian +
            self.xmedian +
            self.ymedian +
            self.zmedian +
            (self.tperc is not None) +
            (self.xperc is not None) +
            (self.yperc is not None) +
            (self.zperc is not None) +
            self.tar1
        ) > 1:
            raise ValueError(
                "Only one of the following arguments can be specified:\n"
                "Tmean,\n"
                "Xmean,\n"
                "Ymean,\n"
                "Zmean,\n"
                "Tstd,\n"
                "Xstd,\n"
                "Ystd,\n"
                "Zstd,\n"
                "Tmax,\n"
                "Xmax,\n"
                "Ymax,\n"
                "Zmax,\n"
                "Tmaxn,\n"
                "Xmaxn,\n"
                "Ymaxn,\n"
                "Zmaxn,\n"
                "Tmin,\n"
                "Xmin,\n"
                "Ymin,\n"
                "Zmin,\n"
                "Tmedian,\n"
                "Xmedian,\n"
                "Ymedian,\n"
                "Zmedian,\n"
                "Tperc,\n"
                "Xperc,\n"
                "Yperc,\n"
                "Zperc,\n"
                "Tar1"
            )
        if (
            self.dil_m +
            self.dil_d +
            self.dil_f +
            self.dilall +
            self.ero +
            self.ero_f +
            self.fmedian +
            self.fmean +
            self.fmeanu +
            (self.s is not None) +
            self.subsamp2 +
            self.subsamp2offc
        ) > 1:
            raise ValueError(
                "Only one of the following arguments can be specified:\n"
                "dilM,\n"
                "dilD,\n"
                "dilF,\n"
                "dilall,\n"
                "ero,\n"
                "eroF,\n"
                "fmedian,\n"
                "fmean,\n"
                "fmeanu,\n"
                "s,\n"
                "subsamp2,\n"
                "subsamp2offc"
            )
        if (
            self.kernel_3_d +
            self.kernel_2_d +
            (self.kernel_box is not None) +
            (self.kernel_boxv is not None) +
            (self.kernel_boxv3 is not None) +
            (self.kernel_gauss is not None) +
            (self.kernel_sphere is not None) +
            (self.kernel_file is not None)
        ) > 1:
            raise ValueError(
                "Only one of the following arguments can be specified:\n"
                "kernel_3D,\n"
                "kernel_2D,\n"
                "kernel_box,\n"
                "kernel_boxv,\n"
                "kernel_boxv3,\n"
                "kernel_gauss,\n"
                "kernel_sphere,\n"
                "kernel_file"
            )
        if (
            self.nan +
            self.nanm +
            self.rand +
            self.randn +
            (self.inm is not None) +
            (self.ing is not None) +
            self.range_ +
            self.tensor_decomp +
            self.edge +
            (self.tfce is not None) +
            (self.tfce_s is not None) +
            (self.roc is not None)
        ) > 1:
            raise ValueError(
                "Only one of the following arguments can be specified:\n"
                "nan,\n"
                "nanm,\n"
                "rand,\n"
                "randn,\n"
                "inm,\n"
                "ing,\n"
                "range,\n"
                "tensor_decomp,\n"
                "edge,\n"
                "tfce,\n"
                "tfceS,\n"
                "roc"
            )
        if self.add is not None:
            cargs.extend(["-add", str(self.add)])
        if self.sub is not None:
            cargs.extend(["-sub", str(self.sub)])
        if self.mul is not None:
            cargs.extend(["-mul", str(self.mul)])
        if self.div is not None:
            cargs.extend(["-div", str(self.div)])
        if self.rem is not None:
            cargs.extend(["-rem", str(self.rem)])
        if self.mas is not None:
            cargs.extend(["-mas", execution.input_file(self.mas)])
        if self.thr is not None:
            cargs.extend(["-thr", str(self.thr)])
        if self.thrp is not None:
            cargs.extend(["-thrp", str(self.thrp)])
        if self.thr_p is not None:
            cargs.extend(["-thrP", str(self.thr_p)])
        if self.uthr is not None:
            cargs.extend(["-uthr", str(self.uthr)])
        if self.uthrp is not None:
            cargs.extend(["-uthrp", str(self.uthrp)])
        if self.uthr_p is not None:
            cargs.extend(["-uthrP", str(self.uthr_p)])
        if self.max_ is not None:
            cargs.extend(["-max", str(self.max_)])
        if self.min_ is not None:
            cargs.extend(["-min", str(self.min_)])
        if self.seed is not None:
            cargs.extend(["-seed", str(self.seed)])
        if self.restart is not None:
            cargs.extend(["-restart", execution.input_file(self.restart)])
        if self.save:
            cargs.append("-save")
        if self.exp:
            cargs.append("-exp")
        if self.log:
            cargs.append("-log")
        if self.sin:
            cargs.append("-sin")
        if self.cos:
            cargs.append("-cos")
        if self.tan:
            cargs.append("-tan")
        if self.asin:
            cargs.append("-asin")
        if self.acos:
            cargs.append("-acos")
        if self.atan:
            cargs.append("-atan")
        if self.sqr:
            cargs.append("-sqr")
        if self.sqrt:
            cargs.append("-sqrt")
        if self.recip:
            cargs.append("-recip")
        if self.abs_:
            cargs.append("-abs")
        if self.bin_:
            cargs.append("-bin")
        if self.binv:
            cargs.append("-binv")
        if self.fillh:
            cargs.append("-fillh")
        if self.fillh26:
            cargs.append("-fillh26")
        if self.index:
            cargs.append("-index")
        if self.grid is not None:
            cargs.extend(["-grid", *map(str, self.grid)])
        if self.edge:
            cargs.append("-edge")
        if self.tfce is not None:
            cargs.extend(["-tfce", *map(str, self.tfce)])
        if self.tfce_s is not None:
            cargs.extend(["-tfceS", *map(str, self.tfce_s)])
        if self.nan:
            cargs.append("-nan")
        if self.nanm:
            cargs.append("-nanm")
        if self.rand:
            cargs.append("-rand")
        if self.randn:
            cargs.append("-randn")
        if self.inm is not None:
            cargs.extend(["-inm", str(self.inm)])
        if self.ing is not None:
            cargs.extend(["-ing", str(self.ing)])
        if self.range_:
            cargs.append("-range")
        if self.tensor_decomp:
            cargs.append("-tensor_decomp")
        if self.kernel_3_d:
            cargs.append("-kernel 3D")
        if self.kernel_2_d:
            cargs.append("-kernel 2D")
        if self.kernel_box is not None:
            cargs.extend(["-kernel box", str(self.kernel_box)])
        if self.kernel_boxv is not None:
            cargs.extend(["-kernel boxv", str(self.kernel_boxv)])
        if self.kernel_boxv3 is not None:
            cargs.extend(["-kernel boxv3", *map(str, self.kernel_boxv3)])
        if self.kernel_gauss is not None:
            cargs.extend(["-kernel gauss", str(self.kernel_gauss)])
        if self.kernel_sphere is not None:
            cargs.extend(["-kernel sphere", str(self.kernel_sphere)])
        if self.kernel_file is not None:
            cargs.extend(["-kernel file", execution.input_file(self.kernel_file)])
        if self.dil_m:
            cargs.append("-dilM")
        if self.dil_d:
            cargs.append("-dilD")
        if self.dil_f:
            cargs.append("-dilF")
        if self.dilall:
            cargs.append("-dilall")
        if self.ero:
            cargs.append("-ero")
        if self.ero_f:
            cargs.append("-eroF")
        if self.fmedian:
            cargs.append("-fmedian")
        if self.fmean:
            cargs.append("-fmean")
        if self.fmeanu:
            cargs.append("-fmeanu")
        if self.s is not None:
            cargs.extend(["-s", str(self.s)])
        if self.subsamp2:
            cargs.append("-subsamp2")
        if self.subsamp2offc:
            cargs.append("-subsamp2offc")
        if self.tmean:
            cargs.append("-Tmean")
        if self.xmean:
            cargs.append("-Xmean")
        if self.ymean:
            cargs.append("-Ymean")
        if self.zmean:
            cargs.append("-Zmean")
        if self.tstd:
            cargs.append("-Tstd")
        if self.xstd:
            cargs.append("-Xstd")
        if self.ystd:
            cargs.append("-Ystd")
        if self.zstd:
            cargs.append("-Zstd")
        if self.tmax:
            cargs.append("-Tmax")
        if self.xmax:
            cargs.append("-Xmax")
        if self.ymax:
            cargs.append("-Ymax")
        if self.zmax:
            cargs.append("-Zmax")
        if self.tmaxn:
            cargs.append("-Tmaxn")
        if self.xmaxn:
            cargs.append("-Xmaxn")
        if self.ymaxn:
            cargs.append("-Ymaxn")
        if self.zmaxn:
            cargs.append("-Zmaxn")
        if self.tmin:
            cargs.append("-Tmin")
        if self.xmin:
            cargs.append("-Xmin")
        if self.ymin:
            cargs.append("-Ymin")
        if self.zmin:
            cargs.append("-Zmin")
        if self.tmedian:
            cargs.append("-Tmedian")
        if self.xmedian:
            cargs.append("-Xmedian")
        if self.ymedian:
            cargs.append("-Ymedian")
        if self.zmedian:
            cargs.append("-Zmedian")
        if self.tperc is not None:
            cargs.extend(["-Tperc", str(self.tperc)])
        if self.xperc is not None:
            cargs.extend(["-Xperc", str(self.xperc)])
        if self.yperc is not None:
            cargs.extend(["-Yperc", str(self.yperc)])
        if self.zperc is not None:
            cargs.extend(["-Zperc", str(self.zperc)])
        if self.tar1:
            cargs.append("-Tar1")
        if self.roi is not None:
            cargs.extend(["-roi", *map(str, self.roi)])
        if self.bptf is not None:
            cargs.extend(["-bptf", *map(str, self.bptf)])
        if self.roc is not None:
            cargs.extend(["-roc", *map(str, self.roc)])
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> FslmathsOperationOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `FslmathsOperationOutputs`).
        """
        ret = FslmathsOperationOutputs(
            root=execution.output_file("."),
        )
        return ret


class FslmathsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslmaths(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """The main output file produced by fslmaths"""
    operations: typing.List[FslmathsOperationOutputs]
    """Subcommand outputs"""


def fslmaths(
    input_files: list[InputPathType],
    operations: list[FslmathsOperation],
    output: str,
    datatype_internal: typing.Literal["char", "short", "int", "float", "double", "input"] | None = "float",
    output_datatype: typing.Literal["char", "short", "int", "float", "double", "input"] | None = None,
    runner: Runner = None,
) -> FslmathsOutputs:
    """
    fslmaths by FSL Team.
    
    FSL utility for image arithmetic, statistics, and mathematical operations.
    
    Args:
        input_files: Input images for processing
        operations: Operations to perform on input images
        output: Output image file
        datatype_internal: Datatype used internally for calculations
        output_datatype: Datatype used for the output image
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `FslmathsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLMATHS_METADATA)
    cargs = []
    cargs.append("fslmaths")
    if datatype_internal is not None:
        cargs.extend(["-dt", datatype_internal])
    cargs.extend([execution.input_file(f) for f in input_files])
    cargs.extend([a for c in [s.run(execution) for s in operations] for a in c])
    cargs.append(output)
    if output_datatype is not None:
        cargs.extend(["-odt", output_datatype])
    ret = FslmathsOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{output}"),
        operations=[operations.outputs(execution) for operations in operations],
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLMATHS_METADATA",
    "FslmathsOperation",
    "FslmathsOperationOutputs",
    "FslmathsOutputs",
    "fslmaths",
]
