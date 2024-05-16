# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


SET_MAP_NAMES_METADATA = Metadata(
    id="dcf0688d9bb39ef45912b8210ebd33e788bbd4ae",
    name="set-map-names",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SetMapNamesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `set_map_names(...)`.
    """


def set_map_names(
    runner: Runner,
    data_file: str,
    opt_name_file_file: str | None = None,
    opt_from_data_file_file: str | None = None,
) -> SetMapNamesOutputs:
    """
    SET THE NAME OF ONE OR MORE MAPS IN A FILE.
    
    Sets the name of one or more maps for metric, shape, label, volume, cifti
    scalar or cifti label files. You must specify either -name-file, or
    -from-data-file, or at least one -map option. The three option types are
    mutually exclusive.
    
    Args:
        runner: Command runner
        data_file: the file to set the map names of
        opt_name_file_file: use a text file to replace all map names: text file
            containing map names, one per line
        opt_from_data_file_file: use the map names from another data file: a
            data file with the same number of maps
    Returns:
        NamedTuple of outputs (described in `SetMapNamesOutputs`).
    """
    execution = runner.start_execution(SET_MAP_NAMES_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-set-map-names")
    cargs.append(data_file)
    if opt_name_file_file is not None:
        cargs.extend(["-name-file", opt_name_file_file])
    if opt_from_data_file_file is not None:
        cargs.extend(["-from-data-file", opt_from_data_file_file])
    ret = SetMapNamesOutputs(
    )
    execution.run(cargs)
    return ret
