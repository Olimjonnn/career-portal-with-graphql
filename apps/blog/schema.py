import strawberry 
from typing import List
from apps.blog.models import Blog
from apps.blog.types import BlogType, AuthType

from apps.main.permissions import IsOwner

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from datetime import datetime, timedelta
import jwt
from jwt.exceptions import ExpiredSignatureError

# from config.decorators import is_authenticated

# def is_authenticated(func):
#     def wrapper(self, info, id: int = None) -> List[BlogType]:
#         user_authenticated = info.context.request.user.is_authenticated

#         if not user_authenticated:
#             raise Exception("Unauthorized access. User must be authenticated.")

#         return func(self, info, id)

#     return wrapper



@strawberry.type
class Query:
    @strawberry.field
    # @is_authenticated
    def blogpage(self, id: int=None) -> List[BlogType]:
        if id:
            blog_post = get_object_or_404(Blog, id=id)
            return [blog_post]
        return Blog.objects.all()
    
@strawberry.type
class Mutation:

    @strawberry.mutation
    def token_auth(self, username: str, password: str) -> AuthType:
        user = User.objects.get(username=username)

        if user.check_password(password):
            expiration = datetime.utcnow() + timedelta(minutes=60)
            token = jwt.encode({"user_id": str(user.id), "exp":expiration}, 'SECRET_KEY', algorithm='HS256')
            return AuthType(token=token, user=user)
        return ValueError("Invalid credentials.")

    @strawberry.field
    def create_blog(self, title:str, short_description:str,
        description:str, created_by__id:int) -> BlogType:
        created_by = User.objects.get(id=created_by__id)
        blog = Blog.objects.create(
            title=title,
            short_description=short_description,
            description=description,
            created_by=created_by
        )
        blog.save()
        return blog

    @strawberry.field
    def update_homepage(self, id:int, title:str, short_description:str,
        description:str, modified_by__id:int) -> BlogType:

        modified_by = get_object_or_404(User, id=modified_by__id)
        blog = get_object_or_404(Blog, pk=id)

        blog.title = title
        blog.short_description = short_description
        blog.description = description
        blog.modified_by = modified_by
        
        Blog.objects.filter(pk=id).update(
            title=title,
            short_description=short_description,
            description=description,
            modified_by=modified_by
        )

        blog.save()
        return blog
    
    @strawberry.field
    def delete_blog(self, id:int) -> bool:
        blog = get_object_or_404(Blog, pk=id)
        blog.delete()
        return True
    
schema = strawberry.Schema(query=Query, mutation=Mutation)