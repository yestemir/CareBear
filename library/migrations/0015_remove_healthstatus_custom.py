# Generated by Django 3.1.7 on 2022-03-19 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_auto_20220319_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthstatus',
            name='custom',
        ),
    ]