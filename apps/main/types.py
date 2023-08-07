import strawberry

@strawberry.type
class UserType:
    id: int
    username: str
    email: str


@strawberry.type
class MainType:
    id: int
    title: str
    description: str
    type: str
    created_date: str
    modified_date: str
    created_by: UserType
    modified_byle: UserType

@strawberry.type
class ContatUsType:
    id: int
    phone: str
    letter: str
    created_at: str