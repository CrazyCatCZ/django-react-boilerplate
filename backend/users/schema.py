import graphene
from .mutations.users import *


class UserMutation(AuthMutation):
    pass


class UserQuery:
    me = graphene.Field(CustomUserType)

    def resolve_me(root, info, **kwargs):
        user = info.context.user

        if user.is_authenticated:
            return user 
        else:
            return None