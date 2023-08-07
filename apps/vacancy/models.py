from django.db import models
import random
import string
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from apps.vacancy.constants import JOB_TYPE, CANDIDATE_LEVEL, STATUS



class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=55)
    is_recommended = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Branch(models.Model):
    latitude = models.CharField(max_length=40)
    longitude = models.CharField(max_length=40)
    address = models.CharField(max_length=255)
    city_name = models.CharField(max_length=40, verbose_name="City")

    def __str__(self) -> str:
        return self.city_name

    class Meta:
        verbose_name_plural = 'Branches'


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='vacancies')
    job_type = models.CharField(max_length=20, choices=JOB_TYPE.CHOICES)
    candidate_level = models.CharField(max_length=50, choices=CANDIDATE_LEVEL.CHOICES)
    experience = models.IntegerField()
    tags = models.ManyToManyField(Tag, related_name='vacancies')
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True,
                               blank=True, related_name='vacancy')
    is_recommended = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Vacancies'


class Requirement(models.Model):
    description = models.CharField(max_length=500)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='requirements')

    def __str__(self) -> str:
        return self.description


class Responsibility(models.Model):
    description = models.CharField(max_length=500)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='responsibilities')

    def __str__(self) -> str:
        return self.description

    class Meta:
        verbose_name_plural = 'Responsibilities'


class Condition(models.Model):
    description = models.CharField(max_length=500)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='conditions')

    def __str__(self) -> str:
        return self.description


class Apply(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applies', null=True)
    status = models.CharField(max_length=20, choices=STATUS.CHOICES, default=STATUS.PENDING)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name_plural = 'Applies'



