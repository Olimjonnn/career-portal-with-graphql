from apps.vacancy.models import (
    Branch,
    Category,
    Condition,
    Requirement,
    Responsibility,
    Tag,
    Vacancy,
)
from modeltranslation.translator import TranslationOptions, translator


class TagTranslationOptions(TranslationOptions):
    fields = ("name",)


class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


class VacancyTranslationOptions(TranslationOptions):
    fields = ("title", "description")


class RequirementTranslationOptions(TranslationOptions):
    fields = ("description",)


class ResponsibilityTranslationOptions(TranslationOptions):
    fields = ("description",)


class ConditionTranslationOptions(TranslationOptions):
    fields = ("description",)




class BranchTranslationOptions(TranslationOptions):
    fields = ("city_name", "address")



translator.register(Tag, TagTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Vacancy, VacancyTranslationOptions)
translator.register(Requirement, RequirementTranslationOptions)
translator.register(Responsibility, ResponsibilityTranslationOptions)
translator.register(Condition, ConditionTranslationOptions)
translator.register(Branch, BranchTranslationOptions)