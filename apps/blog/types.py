import graphene 
from graphene_django.types import DjangoObjectType
from apps.blog.models import Blog
from django.contrib.auth.models import User
from apps.blog.filters import BlogFilter


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class BlogType(DjangoObjectType):
    class Meta:
        model = Blog
        interfaces = (graphene.relay.Node,)
        fields = '__all__'
        filterset_class = BlogFilter
















# @strawberry.type
# class UserType:
#     id: int
#     username: str
#     email: str

# @strawberry.type
# class AuthType:
#     token: str
#     user: UserType  


# @strawberry.type
# class BlogType:
#     id: int
#     title: str
#     short_description: str
#     description: str
#     image: str
#     created_date: str
#     modified_date: str
#     created_by: UserType
#     modified_byle: UserType