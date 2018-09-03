# from django.conf import settings
from django.contrib.auth import get_user_model, authenticate, login, logout
import graphene
from graphene_django.types import DjangoObjectType

from .models import UserDetail


class BasicUserInfoType(DjangoObjectType):
    """Django basic user information."""

    class Meta(object):
        """Metadata."""
        model = get_user_model()


class PublicBasicUserInfoType(DjangoObjectType):
    """Django public basic user information."""

    class Meta(object):
        """Metadata."""
        model = get_user_model()
        exclude_fields = ('password', 'email', 'id')


class AdvancedUserInfoType(DjangoObjectType):
    """Django advanced user information."""

    class Meta(object):
        """Metadata."""
        model = UserDetail


class Login(graphene.Mutation):
    """Login mutation."""

    class Arguments(object):
        """Arguments."""
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, username, password):
        """Mutation."""
        user = authenticate(username=username, password=password)
        if user is None:
            return Login(ok=False)
        login(info.context, user)
        return Login(ok=True)


class Logout(graphene.Mutation):
    """Logout mutation."""

    ok = graphene.Boolean()

    def mutate(self, info):
        """Mutate."""
        logout(info.context)
        return Logout(ok=True)


class PublicQuery(object):
    """Query."""
    public_users = graphene.List(
        PublicBasicUserInfoType,
        offset=graphene.Int(default_value=0),
        limit=graphene.Int(default_value=3)
    )

    def resolve_public_users(self, info, offset, limit):
        """Resolve public users."""
        return get_user_model().objects.filter(
            details__is_public=True
        ).all()[offset:limit]


class PublicMutations(object):
    """Public mutations."""
    login = Login.Field()


class PrivateMutations(object):
    """Private Mutations."""
    logout = Logout.Field()


class PrivateQuery(object):
    """Private query."""
    me = graphene.Field(BasicUserInfoType)

    def resolve_me(self, info):
        """Resolve user information that is logged in."""
        return info.context.user
