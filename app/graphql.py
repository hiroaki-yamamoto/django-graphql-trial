"""GraphQL API."""

from graphene import ObjectType, Schema
from .user.schema import Query as UserQuery


class Query(UserQuery, ObjectType):
    """Merge all query schema."""
    pass


schema = Schema(query=Query)
