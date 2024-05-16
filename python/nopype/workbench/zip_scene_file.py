# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


ZIP_SCENE_FILE_METADATA = Metadata(
    id="82547db09c2958f5df5064ed3a0f4d79af8b7f31",
    name="zip-scene-file",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class ZipSceneFileOutputs(typing.NamedTuple):
    """
    Output object returned when calling `zip_scene_file(...)`.
    """


def zip_scene_file(
    runner: Runner,
    scene_file: str,
    extract_folder: str,
    zip_file: str,
    opt_base_dir_directory: str | None = None,
    opt_skip_missing: bool = False,
    opt_write_scene_file: bool = False,
) -> ZipSceneFileOutputs:
    """
    ZIP A SCENE FILE AND ITS DATA FILES.
    
    If zip-file already exists, it will be overwritten. If -base-dir is not
    specified, the base directory will be automatically set to the lowest level
    directory containing all files. The scene file must contain only relative
    paths, and no data files may be outside the base directory.
    
    Args:
        runner: Command runner
        scene_file: the scene file to make the zip file from
        extract_folder: the name of the folder created when the zip file is
            unzipped
        zip_file: out - the zip file that will be created
        opt_base_dir_directory: specify a directory that all data files are
            somewhere within, this will become the root of the zipfile's directory
            structure: the directory
        opt_skip_missing: any missing files will generate only warnings, and the
            zip file will be created anyway
        opt_write_scene_file: rewrite the scene file before zipping, to store a
            new base path or fix extra '..'s in paths that might break
    Returns:
        NamedTuple of outputs (described in `ZipSceneFileOutputs`).
    """
    execution = runner.start_execution(ZIP_SCENE_FILE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-zip-scene-file")
    cargs.append(scene_file)
    cargs.append(extract_folder)
    cargs.append(zip_file)
    if opt_base_dir_directory is not None:
        cargs.extend(["-base-dir", opt_base_dir_directory])
    if opt_skip_missing:
        cargs.append("-skip-missing")
    if opt_write_scene_file:
        cargs.append("-write-scene-file")
    ret = ZipSceneFileOutputs(
    )
    execution.run(cargs)
    return ret
