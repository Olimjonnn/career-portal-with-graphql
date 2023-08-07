from django.contrib import admin
from apps.vacancy import models


admin.site.register(models.Tag)
admin.site.register(models.Branch)
admin.site.register(models.Vacancy)
admin.site.register(models.Category)
admin.site.register(models.Apply)
admin.site.register(models.Condition)
admin.site.register(models.Requirement)
admin.site.register(models.Responsibility)
# Register your models here.
