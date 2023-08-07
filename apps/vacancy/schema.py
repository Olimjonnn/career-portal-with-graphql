import strawberry
from typing import List, Dict, Union
from django.contrib.auth.models import User
from typing import List
from apps.vacancy.models import (
    Tag,
    Category,
    Branch,
    Vacancy,
    Requirement,
    Responsibility,
    Condition,
    Apply
)
from django.shortcuts import get_object_or_404
from apps.vacancy.types import (
    TagType,
    RequirementType,
    ResponsibilityType,
    ConditionType,
    CategoryType,
    BranchType,
    VacancyType,
    ApplyType,
)

@strawberry.type
class Query:
    ### Get funcrion for Tag model: 
    @strawberry.field
    def taglist(self, name: str=None) -> List[TagType]:
        if name:
            return Tag.objects.filter(name=name)
        return Tag.objects.all()
    
    ### Get funcrion for Branch model:
    @strawberry.field
    def bgranchlist(self, city_name: str=None) -> List[BranchType]:
        if city_name:
            return Branch.objects.filter(city_name=city_name)
        return Branch.objects.all()
    
    ### Get funcrion for Category model:
    @strawberry.field
    def categorylist(self, name: str=None) -> List[CategoryType]:
        if name:
            return Category.objects.filter(name=name)
        return Category.objects.all()
    
    ### Get funcrion for Apply model:
    @strawberry.field
    def apllylist(self, first_name: str=None) -> List[ApplyType]:
        if first_name:
            return Apply.objects.filter(first_name=first_name)
        return Apply.objects.all()

    ### Get requirements:
    @strawberry.field
    def get_requirements(self, vacancy__id: int=None) -> List[RequirementType]:
        if vacancy__id:
            return Requirement.objects.filter(vacancy__id=vacancy__id)
        return Requirement.objects.all()

    ### Get responsibilities:
    @strawberry.field
    def get_reresposibilities(self, vacancy__id: int=None) -> List[ResponsibilityType]:
        if vacancy__id:
            return Responsibility.objects.filter(vacancy__id=vacancy__id)
        return Responsibility.objects.all()

    ### Get conditions:
    @strawberry.field
    def get_conditions(self, vacancy__id: int=None) -> List[ConditionType]:
        if vacancy__id:
            return Condition.objects.filter(vacancy__id=vacancy__id)
        return Condition.objects.all()
    

@strawberry.type
class Mutation:
    ### Create, Update and Destroy functions for Tag model:
    @strawberry.field
    def create_tag(self, name: str) -> TagType:
        tag = Tag.objects.create(
            name=name,
        )
        tag.save()
        return tag

    @strawberry.field
    def update_tag(self, id: int, name: str) -> TagType:
        tag = Tag.objects.get(pk=id)
        tag.name = name
        tag.save()
        return tag

    @strawberry.field
    def delete_tag(self, id: int) -> bool:
        tag = Tag.objects.get(pk=id)
        tag.delete()
        return True
    

    ### Create, Update and Delete functions for Branch model:
    @strawberry.field
    def create_branch(self, latitude: str, 
            longitude: str, address: str, city_name: str) -> BranchType:
        branch = Branch.objects.create(
            latitude=latitude,
            longitude=longitude,
            address=address,
            city_name=city_name
        )
        branch.save()
        return branch
    
    @strawberry.field
    def update_branch(self, id: int, latitude: str, 
            longitude: str, address: str, city_name: str) -> BranchType:
        branch = Branch.objects.get(pk=id)
        branch.latitude = latitude
        branch.longitude = longitude
        branch.address = address
        branch.city_name = city_name
        branch.save()
        return branch

    @strawberry.field
    def delete_branch(self, id: int) -> bool:
        branch = Branch.objects.get(pk=id)
        branch.delete()
        return True
    

    ### Create, Update and Destroy functions for Category model:
    @strawberry.field
    def create_category(self, name: str, is_recommended: bool) -> CategoryType:
        category = Category.objects.create(name=name, is_recommended=is_recommended)
        category.save()
        return category
    
    @strawberry.field
    def update_category(self, id: int, name: str, is_recommended: bool) -> CategoryType:
        category = Category.objects.get(pk=id)
        category.name = name
        category.is_recommended = is_recommended
        category.save()
        return category

    @strawberry.field
    def delete_category(self, id: int) -> bool:
        category = Category.objects.get(pk=id)
        category.delete()
        return True
    
    ### Create function for Apply model:
    @strawberry.field
    def applying(self, vacancy__id:int, status:str, email:str,
            first_name:str, last_name:str, father_name:str, phone:str) -> ApplyType:
        vacancy = Vacancy.objects.get(pk=vacancy__id)
        apply = Apply.objects.create(
            vacancy = vacancy,
            status = status,
            first_name = first_name,
            last_name = last_name,
            father_name = father_name,
            email = email,
            phone = phone,
        )
        apply.save()
        return apply
    

    ### Create, Update and Destroy functions for Vacancy model:
    @strawberry.field
    def create_vacancy(self, title: str, description: str, category__id: int,
        job_type: str, candidate_level: str, experience: int,
        branch__id: int, is_recommended: bool, requirements: List[str],
        responsibilities: List[str], conditions: List[str], tags: List[int]) -> VacancyType:
        category = Category.objects.get(pk=category__id)
        branch = Branch.objects.get(pk=branch__id)


        vacancy = Vacancy.objects.create(
            title = title,
            description = description,
            category = category,
            job_type = job_type,
            candidate_level = candidate_level,
            experience = experience,
            branch = branch,
            is_recommended = is_recommended,
        )

        for rq, rs, cn in zip(requirements, responsibilities, conditions):
            Requirement.objects.create(vacancy=vacancy, description=rq)
            Responsibility.objects.create(vacancy=vacancy, description=rs)
            Condition.objects.create(vacancy=vacancy, description=cn)

        for tag in tags:
            vacancy.tags.add(tag)

        vacancy.save()        
        return vacancy

    @strawberry.field
    def update_vacancy(self, id:int, title: str, description: str, category__id: int,
        job_type: str, candidate_level: str, experience: int,
        branch__id: int, is_recommended: bool, requirements:List[str],
        responsibilities: List[str], conditions: List[str], tags: List[int]) -> VacancyType:
        
        vacancy = Vacancy.objects.select_related("category", "branch").get(pk=id)

        vacancy.title = title
        vacancy.description = description
        vacancy.category_id = category__id
        vacancy.branch_id = branch__id
        vacancy.job_type = job_type
        vacancy.candidate_level = candidate_level
        vacancy.experience = experience
        vacancy.is_recommended = is_recommended

        tags_data = Tag.objects.filter(pk__in=tags)
        vacancy.tags.set(tags_data)



        ### Update related fields:
        # Requirements:
        existing_requirements = list(vacancy.requirements.all())
        existing_requirement_ids = {requirement.id for requirement in existing_requirements}
        updated_requirement_ids = set()

        for item in requirements:
            if item.strip():  
                requirement_obj, created = Requirement.objects.get_or_create(description=item, vacancy=vacancy)
                updated_requirement_ids.add(requirement_obj.id)

        for requirement in existing_requirements:
            if requirement.id not in updated_requirement_ids:
                requirement.delete()

        # Responsibilities:
        existing_responsibility = list(vacancy.responsibilities.all())
        existing_responsibility_ids = {responsibility.id for responsibility in existing_responsibility}
        updated_responsibility_ids = set()

        for item in responsibilities:
            if item.strip():
                responsibility_obj, created = Responsibility.objects.get_or_create(description=item, vacancy=vacancy)
                updated_responsibility_ids.add(responsibility_obj.id)
        
        for responsibility in existing_responsibility:
            if responsibility.id not in updated_responsibility_ids:
                requirement.delete()
        
        # Conditions:
        existing_condition = list(vacancy.responsibilities.all())
        existing_condition_ids = {condition.id for condition in existing_condition}
        updated_conditons_ids = set()

        for item in conditions:
            if item.strip():
                condition_obj, created = Condition.objects.get_or_create(description=item, vacancy=vacancy)
                updated_conditons_ids.add(condition_obj.id)
        
        for condition in existing_condition:
            if condition.id not in updated_conditons_ids:
                condition.delete()
                
        vacancy.save()
        return vacancy

    @strawberry.field
    def delete_vacancy(self, id: int) -> bool:
        vacancy = get_object_or_404(Vacancy, pk=id)
        vacancy.delete()
        return True
    # def update_related_items(queryset, items, model_class):
    #     existing_item_ids = set(queryset.values_list('id', flat=True))

    #     new_items = [model_class(description=item) for item in items if item.strip()]
    #     new_items, _ = model_class.objects.bulk_create(new_items, ignore_conflicts=True)

    #     new_item_ids = [item.id for item in new_items]

    #     items_to_remove = existing_item_ids - set(new_item_ids)

    #     model_class.objects.filter(id__in=items_to_remove).delete()    
        
schema = strawberry.Schema(query=Query, mutation=Mutation)
