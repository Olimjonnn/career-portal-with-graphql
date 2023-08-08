import strawberry
import graphene
from typing import List, Optional
from graphene_django.types import DjangoObjectType
from apps.vacancy.models import (
    Tag, 
    Category, 
    Branch,
    Vacancy,
    Requirement,
    Responsibility,
    Condition,
    Apply)
from apps.vacancy.filters import VacancyFilter
from django.contrib.auth.models import User 

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = "__all__"


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"
        

class BranchType(DjangoObjectType):
    class Meta:
        model = Branch
        fields = "__all__"
        

class VacancyType(DjangoObjectType):
    class Meta:
        model = Vacancy
        fields = "__all__"
        interfaces = (graphene.relay.Node,)
        filterset_class = VacancyFilter
        

class RequirementType(DjangoObjectType):
    class Meta:
        model = Requirement
        fields = "__all__"
        

class ResponsibilityType(DjangoObjectType):
    class Meta:
        model = Responsibility
        fields = "__all__"
        

class ConditionType(DjangoObjectType):
    class Meta:
        model = Condition
        fields = "__all__"


class ApplyType(DjangoObjectType):
    class Meta:
        model = Apply
        fields = "__all__"








# @strawberry.type
# class TagType:
#     id: int
#     name: str

# @strawberry.type
# class CategoryType:
#     id: int
#     name: str
#     is_recommended: bool


# @strawberry.type
# class BranchType:
#     id: int
#     latitude: str
#     longitude: str
#     address: str
#     city_name: str



# @strawberry.type
# class VacancyType:
#     id: int
#     title: str
#     description: str
#     category: CategoryType
#     job_type: str
#     candidate_level: str
#     experience: int
#     tags: List['TagType']
#     branch: BranchType
#     is_recommended: bool
#     requirements: List['RequirementType']
#     responsibilities: List['ResponsibilityType']
#     conditions: List['ConditionType ']


# @strawberry.type
# class RequirementType:
#     id:Optional[int]
#     description: str
#     vacancy: VacancyType


# @strawberry.type
# class ResponsibilityType:
#     id:int=None
#     description: str
#     vacancy: VacancyType


# @strawberry.type
# class ConditionType:
#     id:int=None
#     description: str
#     vacancy: VacancyType


# @strawberry.type
# class ApplyType:
#     id: int
#     vacancy: VacancyType
#     status: str
#     first_name: str
#     last_name: str
#     father_name: str
#     email: str
#     phone: str
#     created_at: str