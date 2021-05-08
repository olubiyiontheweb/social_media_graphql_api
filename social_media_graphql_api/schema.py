import graphene
from graphene_django import DjangoObjectType
from graphql_api import models

class User(DjangoObjectType):
    class Meta:
        model = models.User

class Query(graphene.ObjectType):
    #hello = graphene.String(default_value="Hi!")
    user = graphene.Field(User, id=graphene.Int())

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return models.User.objects.get(pk=id)

schema = graphene.Schema(query=Query)

