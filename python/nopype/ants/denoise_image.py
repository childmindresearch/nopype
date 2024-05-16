# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


DENOISE_IMAGE_METADATA = Metadata(
    id="de8e9758a56524d9e370be3d8b0536aae5a932b5",
    name="DenoiseImage",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class DenoiseImageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `denoise_image(...)`.
    """
    corrected_image: OutputPathType
    """The noise corrected version of the input image."""
    noise_image: OutputPathType
    """Estimated noise image."""


def denoise_image(
    runner: Runner,
    input_image: InputPathType,
    corrected_image_path: str,
    noise_image_path: str,
    image_dimensionality: typing.Literal[2, 3, 4] | None = None,
    noise_model: typing.Literal["Gaussian", "Rician"] | None = None,
    shrink_factor: int | None = None,
    mask_image: InputPathType | None = None,
    patch_radius: str | None = None,
    search_radius: str | None = None,
    verbose: typing.Literal[0, 1] | None = None,
) -> DenoiseImageOutputs:
    """
    Denoise an image using a spatially adaptive filter originally described in J. V.
    Manjon, P. Coupe, Luis Marti-Bonmati, D. L. Collins, and M. Robles. Adaptive
    Non-Local Means Denoising of MR Images With Spatially Varying Noise Levels,
    Journal of Magnetic Resonance Imaging, 31:192-203, June 2010.
    
    Args:
        runner: Command runner
        input_image: -i, --input-image inputImageFilename. A scalar image is
            expected as input for noise correction.
        corrected_image_path: The noise corrected version of the input image.
        noise_image_path: Estimated noise image.
        image_dimensionality: -d, --image-dimensionality 2/3/4. This option
            forces the image to be treated as a specified-dimensional image. If not
            specified, the program tries to infer the dimensionality from the input
            image.
        noise_model: -n, --noise-model Rician/(Gaussian). Employ a Rician or
            Gaussian noise model.
        shrink_factor: -s, --shrink-factor (1)/2/3/... Running noise correction
            on large images can be time consuming. To lessen computation time, the
            input image can be resampled. The shrink factor, specified as a single
            integer, describes this resampling. Shrink factor = 1 is the default.
        mask_image: -x, --mask-image maskImageFilename. If a mask image is
            specified, denoising is only performed in the mask region.
        patch_radius: -p, --patch-radius 1x1x1. Patch radius. Default is 1x1x1.
        search_radius: -r, --search-radius 2x2x2. Search radius. Default is
            2x2x2.
        verbose: Verbose output.
    Returns:
        NamedTuple of outputs (described in `DenoiseImageOutputs`).
    """
    execution = runner.start_execution(DENOISE_IMAGE_METADATA)
    cargs = []
    cargs.append("DenoiseImage")
    if image_dimensionality is not None:
        cargs.extend(["--image-dimensionality", str(image_dimensionality)])
    if noise_model is not None:
        cargs.extend(["--noise-model", noise_model])
    if shrink_factor is not None:
        cargs.extend(["--shrink-factor", str(shrink_factor)])
    if mask_image is not None:
        cargs.extend(["--mask-image", execution.input_file(mask_image)])
    if patch_radius is not None:
        cargs.extend(["--patch-radius", patch_radius])
    if search_radius is not None:
        cargs.extend(["--search-radius", search_radius])
    if verbose is not None:
        cargs.extend(["--verbose", str(verbose)])
    cargs.extend(["--input-image", execution.input_file(input_image)])
    cargs.append("--output")
    cargs.append(
        "[" +
        corrected_image_path +
        "," +
        noise_image_path +
        "]"
    )
    ret = DenoiseImageOutputs(
        corrected_image=execution.output_file(f"{corrected_image_path}"),
        noise_image=execution.output_file(f"{noise_image_path}"),
    )
    execution.run(cargs)
    return ret
