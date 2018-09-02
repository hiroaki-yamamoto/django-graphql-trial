"""GraphQL API."""

from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView
from graphene import ObjectType, Schema
from .user.schema import (
    PublicQuery as PublicUserQuery,
    PrivateQuery as PrivateUserQuery
)


class PublicQuery(PublicUserQuery, ObjectType):
    """Merge all query schema."""
    pass


class PrivateQuery(PrivateUserQuery, ObjectType):
    """Merge private query."""
    pass


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass


schema = Schema(query=PublicQuery)
private_schema = Schema(query=PrivateQuery)
