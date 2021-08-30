from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cvat_adas_demo.authentication'

    def ready(self):
        from .auth import register_signals
        register_signals()
