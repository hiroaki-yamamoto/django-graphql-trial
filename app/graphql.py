"""GraphQL API."""

from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView
from graphene import ObjectType, Schema
from .user.schema import (
    PublicQuery as PublicUserQuery,
    PrivateQuery as PrivateUserQuery,
    PublicMutations as PublicUserMutation,
    PrivateMutations as PrivateUserMutations
)


class PublicQuery(PublicUserQuery, ObjectType):
    """Merge all query schema."""
    pass


class PublicMut(PublicUserMutation, ObjectType):
    """Merge all public mutations."""


class PrivateQuery(PrivateUserQuery, ObjectType):
    """Merge private query."""
    pass


class PrivateMut(PrivateUserMutations, ObjectType):
    """Merge all private mutations."""
    pass


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass


schema = Schema(query=PublicQuery, mutation=PublicMut)
private_schema = Schema(query=PrivateQuery, mutation=PrivateMut)
