import strawberry
from typing import List, Optional

@strawberry.type
class TagType:
    id: int
    name: str

@strawberry.type
class CategoryType:
    id: int
    name: str
    is_recommended: bool


@strawberry.type
class BranchType:
    id: int
    latitude: str
    longitude: str
    address: str
    city_name: str



@strawberry.type
class VacancyType:
    id: int
    title: str
    description: str
    category: CategoryType
    job_type: str
    candidate_level: str
    experience: int
    tags: List['TagType']
    branch: BranchType
    is_recommended: bool
    requirements: List['RequirementType']
    responsibilities: List['ResponsibilityType']
    conditions: List['ConditionType ']


@strawberry.type
class RequirementType:
    id:Optional[int]
    description: str
    vacancy: VacancyType


@strawberry.type
class ResponsibilityType:
    id:int=None
    description: str
    vacancy: VacancyType


@strawberry.type
class ConditionType:
    id:int=None
    description: str
    vacancy: VacancyType


@strawberry.type
class ApplyType:
    id: int
    vacancy: VacancyType
    status: str
    first_name: str
    last_name: str
    father_name: str
    email: str
    phone: str
    created_at: str