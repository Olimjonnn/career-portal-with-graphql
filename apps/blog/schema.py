import strawberry 
import graphene
from typing import List
from apps.blog.models import Blog
from apps.blog.types import BlogType
from apps.blog.filters import BlogFilter
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from graphene_django.filter import DjangoFilterConnectionField


class Query(graphene.ObjectType):
    all_blogs = DjangoFilterConnectionField(
        BlogType, filterset_class=BlogFilter
    )

    def resolve_all_blogs(self, info, **kwargs):
        return Blog.objects.all()
    
class CreateBlog(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)  
        short_description = graphene.String(required=True)  
        created_by_id = graphene.ID(required=True)  


    blog = graphene.Field(BlogType)

    def mutate(self, info, title, description, short_description, created_by_id):
        user = User.objects.get(pk=created_by_id)
        blog = Blog(title=title, description=description,
                short_description=short_description, created_by=user)
        blog.save()
        return CreateBlog(blog=blog)

class UpdateBlog(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
        short_description = graphene.String()
        modified_by_id = graphene.ID(required=True)

    blog = graphene.Field(BlogType)
    def mutate(self, info, modified_by_id, id, title=None, description=None, short_description=None):
        
        user = get_object_or_404(User, pk=modified_by_id)
        blog = get_object_or_404(Blog, pk=id)

        if title:
            blog.title = title
        if description:
            blog.description = description
        if short_description:
            blog.short_description = short_description
        
        blog.modified_by = user
        blog.save()
        
        return UpdateBlog(blog=blog)

class DeleteBlog(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    id = graphene.ID()

    def mutate(self, info, id):
        blog = get_object_or_404(Blog, pk=id)
        blog.delete()
        return DeleteBlog(id=id)
    

class Mutation(graphene.ObjectType):
    create_blog = CreateBlog.Field()
    update_blog = UpdateBlog.Field()
    delete_blog = DeleteBlog.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

























# from config.decorators import is_authenticated

# def is_authenticated(func):
#     def wrapper(self, info, id: int = None) -> List[BlogType]:
#         user_authenticated = info.context.request.user.is_authenticated

#         if not user_authenticated:
#             raise Exception("Unauthorized access. User must be authenticated.")

#         return func(self, info, id)

#     return wrapper



# @strawberry.type
# class Query:
#     @strawberry.field
#     # @is_authenticated
#     def blogpage(self, id: int=None) -> List[BlogType]:
#         if id:
#             blog_post = get_object_or_404(Blog, id=id)
#             return [blog_post]
#         return Blog.objects.all()
    
# @strawberry.type
# class Mutation:

#     @strawberry.mutation
#     def token_auth(self, username: str, password: str) -> AuthType:
#         user = User.objects.get(username=username)

#         if user.check_password(password):
#             expiration = datetime.utcnow() + timedelta(minutes=60)
#             token = jwt.encode({"user_id": str(user.id), "exp":expiration}, 'SECRET_KEY', algorithm='HS256')
#             return AuthType(token=token, user=user)
#         return ValueError("Invalid credentials.")

#     @strawberry.field
#     def create_blog(self, title:str, short_description:str,
#         description:str, created_by__id:int) -> BlogType:
#         created_by = User.objects.get(id=created_by__id)
#         blog = Blog.objects.create(
#             title=title,
#             short_description=short_description,
#             description=description,
#             created_by=created_by
#         )
#         blog.save()
#         return blog

#     @strawberry.field
#     def update_homepage(self, id:int, title:str, short_description:str,
#         description:str, modified_by__id:int) -> BlogType:

#         modified_by = get_object_or_404(User, id=modified_by__id)
#         blog = get_object_or_404(Blog, pk=id)

#         blog.title = title
#         blog.short_description = short_description
#         blog.description = description
#         blog.modified_by = modified_by
        
#         Blog.objects.filter(pk=id).update(
#             title=title,
#             short_description=short_description,
#             description=description,
#             modified_by=modified_by
#         )

#         blog.save()
#         return blog
    
#     @strawberry.field
#     def delete_blog(self, id:int) -> bool:
#         blog = get_object_or_404(Blog, pk=id)
#         blog.delete()
#         return True
    