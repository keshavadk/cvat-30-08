from django.apps import AppConfig


class TrainingConfig(AppConfig):
    name = 'cvat_adas_demo.training'

    def ready(self):
        # Required to define signals in application
        import cvat_adas_demo.training.signals
        # Required in order to silent "unused-import" in pyflake
        assert cvat_adas_demo.training.signals
