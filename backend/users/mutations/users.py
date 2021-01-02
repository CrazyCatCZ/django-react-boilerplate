import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.dispatch import receiver
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphql_jwt.refresh_token.signals import refresh_token_rotated




class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


# Revoke refresh token after it has been used
@receiver(refresh_token_rotated)
def revoke_refresh_token(sender, request, refresh_token, **kwargs):
    refresh_token.revoke(request)


class Register(DjangoModelFormMutation):
    user = graphene.Field(CustomUserType)

    class Meta:
        form_class = RegisterForm
        return_field_name = 'user'
   

class Login(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    message = graphene.String()

    def mutate(self, info, username, password):
        request = info.context
        user = authenticate(username=username, password=password)
        current_user = request.user

        if user is None:
            message = "You provided wrong credentials!"

        elif current_user.is_authenticated:
            message = 'User is already authenticated!'

        else:
            message = 'Success!'
            login(request, user)

        return Login(message)


class Logout(graphene.Mutation):
   message = graphene.String()

   def mutate(self, info, input=None):
        request = info.context
        user = request.user

        if user.is_authenticated:
            message = 'Success!'
            logout(request)
      
        else:
            message = 'User is not authenticated!'

        return Logout(message)


class VerifyAccessToken(graphene.Mutation):
    is_expired = graphene.String()

    def mutate(self, info, input=None):
        is_expired = None
        request = info.context
        access_token = request.COOKIES.get('accessToken')
        refresh_token = request.COOKIES.get('refreshToken')

        if refresh_token != None and access_token == None:
            is_expired = True
        
        else:
            is_expired = False

        return VerifyAccessToken(is_expired)



class AuthMutation(graphene.ObjectType):
    register = Register.Field()
    login = Login.Field()
    logout = Logout.Field()
    verify_access_token = VerifyAccessToken.Field()

    # Django-graphql-jwt
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()