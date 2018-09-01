# from django.conf import settings
from django.contrib.auth import get_user_model
import graphene
from graphene_django.types import DjangoObjectType

from .models import UserDetail


class BasicUserInfoType(DjangoObjectType):
    """Django basic user information."""

    class Meta(object):
        """Metadata."""
        model = get_user_model()


class AdvancedUserInfoType(DjangoObjectType):
    """Django advanced user information."""

    class Meta(object):
        """Metadata."""
        model = UserDetail


class Query(object):
    """Query."""
    public_users = graphene.List(
        BasicUserInfoType,
        offset=graphene.Int(default_value=0),
        limit=graphene.Int(default_value=3)
    )

    def resolve_public_users(self, info, offset, limit):
        """Resolve public users."""
        return get_user_model().objects.filter(
            details__is_public=True
        ).all()[offset:limit]
