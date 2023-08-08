from modeltranslation.translator import TranslationOptions, translator

from apps.main.models import HomePage


class HomePageTranslationOptions(TranslationOptions):
    fields = ("title", 'description')


translator.register(HomePage, HomePageTranslationOptions)