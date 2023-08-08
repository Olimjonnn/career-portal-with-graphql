# import strawberry
import graphene
from typing import List
from apps.main.models import HomePage, ContactUs
from django.contrib.auth.models import User
from apps.main.types import (
    HomePageType,
    ContactUsType
)
from apps.main.filters import HomePageFilter

from apps.main.permissions import IsOwner
from django.shortcuts import get_object_or_404
from graphene_django.filter import DjangoFilterConnectionField


class Query(graphene.ObjectType):
    all_pages = DjangoFilterConnectionField(
        HomePageType, filterset_class=HomePageFilter)

    def resolve_all_pages(root, info, **kwargs):
        return HomePage.objects.all()
    
class CreateHomePage(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        type = graphene.String(required=True)
        created_by_id = graphene.ID(required=True)

    home = graphene.Field(HomePageType)

    def mutate(self, info, title, description, type, created_by_id):
        user = User.objects.get(pk=created_by_id)
        home = HomePage(title=title, description=description,
                        type=type, created_by_id=user)
        home.save()
        return CreateHomePage(home=home)

class UpdateHomePage(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
        type = graphene.String()
        modified_by_id = graphene.ID(required=True)
    
    home = graphene.Field(HomePageType)
    
    def mutate(self, info, id, modified_by_id,
            title=None, description=None, type=None):
        user = get_object_or_404(User, pk=modified_by_id)
        home = get_object_or_404(HomePage, pk=id)

        if title:
            home.title = title
        if description:
            home.description = description
        if type:
            home.type = type

        home.modified_by = user
        home.save()
        return UpdateHomePage(home=home)
    
class DeleteHomePage(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    id = graphene.ID()

    def mutate(self, info, id):
        home = get_object_or_404(HomePage, pk=id)
        home.delete()
        return DeleteHomePage(id=id)

### Create function for ContactUs Model

class SendingLetter(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        type = graphene.String(required=True)
        created_by = graphene.ID(required=True)
    
    home = graphene.Field(HomePageType)

    def mutate(self, info, title, description, type, created_by_id):
        user = get_object_or_404(User, pk=created_by_id)
        home = HomePage(
            title=title,
            description=description,
            type=type,
            created_by_id=user
        )
        home.save()
        return CreateHomePage(home=home)
    
class Mutation(graphene.ObjectType):
    create_home_page = CreateHomePage.Field()
    update_home_page = UpdateHomePage.Field()
    delete_home_page = DeleteHomePage.Field()
    sending_letter = SendingLetter.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)



##### Here is a version made by the strawberry library

# @strawberry.type
# class Query:

#     @strawberry.field(permission_classes=[IsOwner])
#     def homepages(self, id: int=None) -> List[MainType]:
#         if id:
#             return get_object_or_404(HomePage, id=id)
#         return HomePage.objects.all()
    
#     ### GET function for ContactUs model:
#     @strawberry.field
#     def contactuslist(self) -> List[ContatUsType]:
#         return ContactUs.objects.all()

# @strawberry.type
# class Mutation:

#     @strawberry.field(permission_classes=[IsOwner])
#     def create_homepage(self, title:str, description:str, type:str,created_by__id:int) -> MainType:
#         created_by = User.objects.get(id=created_by__id)
#         home = HomePage.objects.create(
#             title=title,
#             description=description,
#             type=type,
#             created_by = created_by,
#         )
#         home.save()
#         return home

#     @strawberry.field(permission_classes=[IsOwner])
#     def update_homepage(self, id: int, title:str, description:str, type:str,modified_by__id:int) -> MainType:
#         modified_by = User.objects.get(id=modified_by__id)
#         home = HomePage.objects.get(pk=id)
#         home.title = title
#         home.description = description
#         home.type = type
#         home.modified_by = modified_by
#         home.save()
#         return home

#     @strawberry.field(permission_classes=[IsOwner])
#     def delete_homapage(self, id: int) -> bool:
#         home = HomePage.objects.get(pk=id)
#         home.delete()
#         return True
    
#     ### Create function for ContactUs model:    
#     @strawberry.field
#     def sendind_letter(self, phone:str, letter:str) -> ContatUsType:
#         post = ContactUs.objects.create(
#             phone = phone,
#             letter = letter,
#         )
#         post.save()
#         return post
