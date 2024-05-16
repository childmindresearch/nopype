# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


EPI_REG_METADATA = Metadata(
    id="37cb7269b8203daa1607d21f01257d8871072881",
    name="epi_reg",
    container_image_type="docker",
    container_image_tag="fcp-indi/c-pac:nightly",
)


class EpiRegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `epi_reg(...)`.
    """
    epi2str_inv: OutputPathType
    """Rigid structural-to-epi transform."""
    epi2str_mat: OutputPathType
    """Rigid epi-to-structural transform."""
    fmap2epi_mat: OutputPathType
    """Rigid fieldmap-to-epi transform."""
    fmap2str_mat: OutputPathType
    """Rigid fieldmap-to-structural transform."""
    fmap_epi: OutputPathType
    """Fieldmap in epi space."""
    fmap_str: OutputPathType
    """Fieldmap in structural space."""
    fmapmag_str: OutputPathType
    """Fieldmap magnitude image in structural space."""
    fullwarp: OutputPathType
    """Warpfield to unwarp epi and transform into structural space."""
    out_1vol: OutputPathType
    """Unwarped and coregistered single volume."""
    out_file: OutputPathType
    """Unwarped and coregistered epi input."""
    seg: OutputPathType
    """White matter, gray matter, csf segmentation."""
    shiftmap: OutputPathType
    """Shiftmap in epi space."""
    wmedge: OutputPathType
    """White matter edges for visualization."""
    wmseg_outfile: OutputPathType
    """White matter segmentation used in flirt bbr."""


def epi_reg(
    runner: Runner,
    epi: InputPathType,
    out_base_name: str,
    t1_brain: InputPathType,
    t1_head: InputPathType,
    echospacing: float | int | None = None,
    fmap: InputPathType | None = None,
    fmapmag: InputPathType | None = None,
    fmapmagbrain: InputPathType | None = None,
    no_clean: bool = False,
    no_fmapreg: bool = False,
    pedir: typing.Literal["x", "y", "z", "-x", "-y", "-z"] | None = None,
    weight_image: InputPathType | None = None,
    wmseg: InputPathType | None = None,
) -> EpiRegOutputs:
    """
    epi_reg, as implemented in Nipype (module: nipype.interfaces.fsl, interface:
    EpiReg). Runs FSL epi_reg script for simultaneous coregistration and fieldmap
    unwarping.
    
    Args:
        runner: Command runner
        epi: EPI Nifti image.
        out_base_name: Output base name.
        t1_brain: Brain-extracted T1 image.
        t1_head: Wholehead T1 image.
        echospacing: Effective epi echo spacing (sometimes called dwell time) -
            in seconds.
        fmap: Fieldmap image (in rad/s).
        fmapmag: Fieldmap magnitude image - wholehead.
        fmapmagbrain: Fieldmap magnitude image - brain extracted.
        no_clean: Do not clean up intermediate files.
        no_fmapreg: Do not perform registration of fmap to t1 (use if fmap
            already registered).
        pedir: 'x' or 'y' or 'z' or '-x' or '-y' or '-z'. Phase encoding
            direction, dir = x/y/z/-x/-y/-z.
        weight_image: Weighting image (in t1 space).
        wmseg: White matter segmentation of t1 image, has to be named like the
            t1brain and end on _wmseg.
    Returns:
        NamedTuple of outputs (described in `EpiRegOutputs`).
    """
    execution = runner.start_execution(EPI_REG_METADATA)
    cargs = []
    cargs.append("epi_reg")
    cargs.append(("--epi=" + execution.input_file(epi)))
    cargs.append(("--t1=" + execution.input_file(t1_head)))
    cargs.append(("--t1brain=" + execution.input_file(t1_brain)))
    cargs.append(("--out=" + out_base_name))
    if echospacing is not None:
        cargs.append(("--echospacing=" + str(echospacing)))
    if fmap is not None:
        cargs.append(("--fmap=" + execution.input_file(fmap)))
    if fmapmag is not None:
        cargs.append(("--fmapmag=" + execution.input_file(fmapmag)))
    if fmapmagbrain is not None:
        cargs.append(("--fmapmagbrain=" + execution.input_file(fmapmagbrain)))
    if no_clean:
        cargs.append("--noclean")
    if no_fmapreg:
        cargs.append("--nofmapreg")
    if pedir is not None:
        cargs.append(("--pedir=" + pedir))
    if weight_image is not None:
        cargs.append(("--weight=" + execution.input_file(weight_image)))
    if wmseg is not None:
        cargs.append(("--wmseg=" + execution.input_file(wmseg)))
    ret = EpiRegOutputs(
        epi2str_inv=execution.output_file(f"epi2str_inv.mat", optional=True),
        epi2str_mat=execution.output_file(f"epi2struct.mat", optional=True),
        fmap2epi_mat=execution.output_file(f"fmap2epi.mat", optional=True),
        fmap2str_mat=execution.output_file(f"fmap2str.mat", optional=True),
        fmap_epi=execution.output_file(f"fmap_epi.nii.gz", optional=True),
        fmap_str=execution.output_file(f"fmap_str.nii.gz", optional=True),
        fmapmag_str=execution.output_file(f"fmapmag_str.nii.gz", optional=True),
        fullwarp=execution.output_file(f"fullwarp.nii.gz", optional=True),
        out_1vol=execution.output_file(f"out_1vol.nii.gz", optional=True),
        out_file=execution.output_file(f"{out_base_name}.nii.gz", optional=True),
        seg=execution.output_file(f"{out_base_name}_fast_seg.nii.gz", optional=True),
        shiftmap=execution.output_file(f"shiftmap.nii.gz", optional=True),
        wmedge=execution.output_file(f"{out_base_name}_fast_wmedge.nii.gz", optional=True),
        wmseg_outfile=execution.output_file(f"{out_base_name}_fast_wmseg.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret
