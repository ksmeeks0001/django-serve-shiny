from django.apps import AppConfig


class ServeShinyConfig(AppConfig):
    name = 'serve_shiny'

    def ready(self):
        from . import signals