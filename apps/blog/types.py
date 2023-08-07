import strawberry 

@strawberry.type
class UserType:
    id: int
    username: str
    email: str

@strawberry.type
class AuthType:
    token: str
    user: UserType  


@strawberry.type
class BlogType:
    id: int
    title: str
    short_description: str
    description: str
    image: str
    created_date: str
    modified_date: str
    created_by: UserType
    modified_byle: UserType