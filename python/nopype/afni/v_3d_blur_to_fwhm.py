# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


V_3D_BLUR_TO_FWHM_METADATA = Metadata(
    id="a9aac6f0866e30f5e7ed62748e0098f57fd2faf5",
    name="3dBlurToFWHM",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dBlurToFwhmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_blur_to_fwhm(...)`.
    """
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Output file."""


def v_3d_blur_to_fwhm(
    runner: Runner,
    in_file: InputPathType,
    automask: bool = False,
    blurmaster: InputPathType | None = None,
    fwhm: float | int | None = None,
    fwhmxy: float | int | None = None,
    mask: InputPathType | None = None,
    num_threads: int | None = 1,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
) -> V3dBlurToFwhmOutputs:
    """
    BlurToFWHM, as implemented in Nipype (module: nipype.interfaces.afni.preprocess,
    interface: BlurToFWHM).
    Blurs a 'master' dataset until it reaches a specified FWHM smoothness
    (approximately).
    For complete details, see the `3dBlurToFWHM Documentation
    <https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dBlurToFWHM.html>`_
    
    Args:
        runner: Command runner
        in_file: The dataset that will be smoothed.
        automask: Create an automask from the input dataset.
        blurmaster: The dataset whose smoothness controls the process.
        fwhm: Blur until the 3d fwhm reaches this value (in mm).
        fwhmxy: Blur until the 2d (x,y)-plane fwhm reaches this value (in mm).
        mask: Mask dataset, if desired. voxels not in mask will be set to zero
            in output.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
    Returns:
        NamedTuple of outputs (described in `V3dBlurToFwhmOutputs`).
    """
    execution = runner.start_execution(V_3D_BLUR_TO_FWHM_METADATA)
    cargs = []
    cargs.append("3dBlurToFWHM")
    cargs.append("[ARGS]")
    if automask:
        cargs.append("-automask")
    if blurmaster is not None:
        cargs.extend(["-blurmaster", execution.input_file(blurmaster)])
    cargs.append("[ENVIRON]")
    if fwhm is not None:
        cargs.extend(["-FWHM", str(fwhm)])
    if fwhmxy is not None:
        cargs.extend(["-FWHMxy", str(fwhmxy)])
    cargs.extend(["-input", execution.input_file(in_file)])
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if num_threads is not None:
        cargs.append(str(num_threads))
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    ret = V3dBlurToFwhmOutputs(
        out_file=execution.output_file(f"{in_file}_afni", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret
