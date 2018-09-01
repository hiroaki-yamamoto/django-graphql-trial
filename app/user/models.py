from django.db import models as db
from django.conf import settings
from django.utils.translation import ugettext as _

from django_countries import fields as ct

# Create your models here.


class UserDetail(db.Model):
    """Additional user detail."""

    user = db.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=db.CASCADE,
        related_name="details",
        related_query_name="details"
    )
    is_public = db.BooleanField(default=False)
    gender = db.CharField(
        max_length=2, choices=(
            ("MM", "Male"),
            ("FF", "Female"),
            ("MF", "My body is male, but my soul is female"),
            ("FM", "My body is female, but my soul is male"),
        )
    )
    address1 = db.CharField(max_length=140)
    address2 = db.CharField(max_length=140)
    city = db.CharField(max_length=20)
    region = db.CharField(max_length=20)
    country = ct.CountryField(blank_label=_("Select Country"))
