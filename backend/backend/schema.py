import graphene
from users.schema import *


class Query(UserQuery, graphene.ObjectType):
   pass


class Mutation(UserMutation, graphene.ObjectType):
   pass


schema = graphene.Schema(query=Query, mutation=Mutation)