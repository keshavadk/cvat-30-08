# Copyright (C) 2018 Intel Corporation
#
# SPDX-License-Identifier: MIT

from django.apps import AppConfig


class EngineConfig(AppConfig):
    name = 'cvat_adas_demo.engine'

    def ready(self):
        # Required to define signals in application
        import cvat_adas_demo.engine.signals
        # Required in order to silent "unused-import" in pyflake
        assert cvat_adas_demo.engine.signals
