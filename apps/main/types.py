# import strawberry
import graphene
from graphene_django.types import DjangoObjectType
from apps.main.models import ContactUs, HomePage
from django.contrib.auth.models import User
from apps.main.filters import HomePageFilter

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class HomePageType(DjangoObjectType):
    class Meta:
        model = HomePage
        fields = "__all__"
        interfaces = (graphene.relay.Node,)
        fields = '__all__'
        filterset_class = HomePageFilter
        

class ContactUsType(DjangoObjectType):
    class Meta:
        model = ContactUs
        fields = "__all__"













# @strawberry.type
# class UserType:
#     id: int
#     username: str
#     email: str


# @strawberry.type
# class MainType:
#     id: int
#     title: str
#     description: str
#     type: str
#     created_date: str
#     modified_date: str
#     created_by: UserType
#     modified_byle: UserType

# @strawberry.type
# class ContatUsType:
#     id: int
#     phone: str
#     letter: str
#     created_at: str