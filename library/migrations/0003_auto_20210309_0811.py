# Generated by Django 3.1.7 on 2021-03-09 08:11
from django.contrib.auth.hashers import make_password
from django.db import migrations


def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.create(
        username='dina', password=make_password('Chocofood1'),
        is_superuser=True,
        is_staff=True
    )


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20210309_0806'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
