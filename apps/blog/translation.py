from modeltranslation.translator import translator, TranslationOptions

from apps.blog.models import Blog


class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description')


translator.register(Blog, BlogTranslationOptions)
