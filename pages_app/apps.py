from django.apps import AppConfig


class PagesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages_app'

    def ready(self):
        import pages_app.signals
