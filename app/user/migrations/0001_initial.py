# Generated by Django 2.1 on 2018-08-31 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('MM', 'Male'), ('FF', 'Female'), ('MF', 'My body is male, but my soul is female'), ('FM', 'My body is female, but my soul is male')], max_length=2)),
                ('address1', models.CharField(max_length=140)),
                ('address2', models.CharField(max_length=140)),
                ('city', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
