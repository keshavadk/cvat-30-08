# Copyright (C) 2020 Intel Corporation
#
# SPDX-License-Identifier: MIT

from tempfile import TemporaryDirectory

from datumaro.components.dataset import Dataset
from pyunpack import Archive

from cvat_adas_demo.dataset_manager.bindings import (CvatTaskDataExtractor,
    import_dm_annotations)
from cvat_adas_demo.dataset_manager.util import make_zip_archive

from .registry import dm_env, exporter, importer
from .utils import make_colormap


@exporter(name='CamVid', ext='ZIP', version='1.0')
def _export(dst_file, task_data, save_images=False):
    dataset = Dataset.from_extractors(CvatTaskDataExtractor(
        task_data, include_images=save_images), env=dm_env)
    dataset.transform('polygons_to_masks')
    dataset.transform('boxes_to_masks')
    dataset.transform('merge_instance_segments')
    label_map = make_colormap(task_data)
    with TemporaryDirectory() as temp_dir:
        dataset.export(temp_dir, 'camvid',
            save_images=save_images, apply_colormap=True,
            label_map={label: label_map[label][0] for label in label_map})

        make_zip_archive(temp_dir, dst_file)

@importer(name='CamVid', ext='ZIP', version='1.0')
def _import(src_file, task_data):
    with TemporaryDirectory() as tmp_dir:
        Archive(src_file.name).extractall(tmp_dir)

        dataset = Dataset.import_from(tmp_dir, 'camvid', env=dm_env)
        dataset.transform('masks_to_polygons')
        import_dm_annotations(dataset, task_data)
