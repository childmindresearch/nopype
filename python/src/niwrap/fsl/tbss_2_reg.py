# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

TBSS_2_REG_METADATA = Metadata(
    id="bab2e71d0f1ac94e9bf20a5d8f8a70d5e2bfe6fd",
    name="tbss_2_reg",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class Tbss2RegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tbss_2_reg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tbss_2_reg(
    use_fmrib58_fa_1mm: bool = False,
    target_image: InputPathType | None = None,
    find_best_target: bool = False,
    runner: Runner = None,
) -> Tbss2RegOutputs:
    """
    tbss_2_reg by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    TBSS utility for target selection and registration for Tract-Based Spatial
    Statistics (TBSS) analysis.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/TBSS/UserGuide
    
    Args:
        use_fmrib58_fa_1mm: Use FMRIB58_FA_1mm as the target for nonlinear
            registrations (recommended)
        target_image: Use the specified image as the target for nonlinear
            registrations
        find_best_target: Find the best target from all images in the FA
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `Tbss2RegOutputs`).
    """
    runner = runner or get_global_runner()
    if (
        use_fmrib58_fa_1mm +
        (target_image is not None) +
        find_best_target
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "use_fmrib58_fa_1mm,\n"
            "target_image,\n"
            "find_best_target"
        )
    execution = runner.start_execution(TBSS_2_REG_METADATA)
    cargs = []
    cargs.append("tbss_2_reg")
    cargs.append("[TARGET_SELECTION_OPTION]")
    ret = Tbss2RegOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TBSS_2_REG_METADATA",
    "Tbss2RegOutputs",
    "tbss_2_reg",
]
