# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


METADATA_STRING_REPLACE_METADATA = Metadata(
    id="c401ec18f64003879449685a4bbdee7858260fc3",
    name="metadata-string-replace",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class MetadataStringReplaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metadata_string_replace(...)`.
    """


def metadata_string_replace(
    runner: Runner,
    input_file: str,
    find_string: str,
    replace_string: str,
    output_file: str,
    opt_case_insensitive: bool = False,
) -> MetadataStringReplaceOutputs:
    """
    REPLACE A STRING IN ALL METADATA OF A FILE.
    
    Replaces all occurrences of <find-string> in the metadata and map names of
    <input-file> with <replace-string>.
    
    Args:
        runner: Command runner
        input_file: the file to replace metadata in
        find_string: the string to find
        replace_string: the string to replace <find-string> with
        output_file: output - the name to save the modified file as
        opt_case_insensitive: match with case variation also
    Returns:
        NamedTuple of outputs (described in `MetadataStringReplaceOutputs`).
    """
    execution = runner.start_execution(METADATA_STRING_REPLACE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metadata-string-replace")
    cargs.append(input_file)
    cargs.append(find_string)
    cargs.append(replace_string)
    cargs.append(output_file)
    if opt_case_insensitive:
        cargs.append("-case-insensitive")
    ret = MetadataStringReplaceOutputs(
    )
    execution.run(cargs)
    return ret
