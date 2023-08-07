import strawberry
from typing import List
from apps.main.models import HomePage, ContactUs
from django.contrib.auth.models import User
from apps.main.types import (
    MainType,
    ContatUsType
)
from apps.main.permissions import IsOwner
from django.shortcuts import get_object_or_404

@strawberry.type
class Query:

    @strawberry.field(permission_classes=[IsOwner])
    def homepages(self, id: int=None) -> List[MainType]:
        if id:
            return get_object_or_404(HomePage, id=id)
        return HomePage.objects.all()
    
    ### GET function for ContactUs model:
    @strawberry.field
    def contactuslist(self) -> List[ContatUsType]:
        return ContactUs.objects.all()

@strawberry.type
class Mutation:

    @strawberry.field(permission_classes=[IsOwner])
    def create_homepage(self, title:str, description:str, type:str,created_by__id:int) -> MainType:
        created_by = User.objects.get(id=created_by__id)
        home = HomePage.objects.create(
            title=title,
            description=description,
            type=type,
            created_by = created_by,
        )
        home.save()
        return home

    @strawberry.field(permission_classes=[IsOwner])
    def update_homepage(self, id: int, title:str, description:str, type:str,modified_by__id:int) -> MainType:
        modified_by = User.objects.get(id=modified_by__id)
        home = HomePage.objects.get(pk=id)
        home.title = title
        home.description = description
        home.type = type
        home.modified_by = modified_by
        home.save()
        return home

    @strawberry.field(permission_classes=[IsOwner])
    def delete_homapage(self, id: int) -> bool:
        home = HomePage.objects.get(pk=id)
        home.delete()
        return True
    
    ### Create function for ContactUs model:    
    @strawberry.field
    def sendind_letter(self, phone:str, letter:str) -> ContatUsType:
        post = ContactUs.objects.create(
            phone = phone,
            letter = letter,
        )
        post.save()
        return post

schema = strawberry.Schema(query=Query, mutation=Mutation)