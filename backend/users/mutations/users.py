import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from users.models import CustomUser


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser


class AuthMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()