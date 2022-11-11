from django.apps import AppConfig
from django.db.utils import ProgrammingError


class PortfolioAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio_app'

    def ready(self):
        try:
            site_language_model = self.get_model("SiteLanguage")
            try:
                site_language_model.objects.get(code='gb')
            except site_language_model.DoesNotExist:
                en_language = site_language_model.objects.create(code='gb', language='English')
                translations = self.get_model('Translation')
                translations.objects.create(language=en_language)
        except ProgrammingError:
            print("You need to run migrations!")
            return None