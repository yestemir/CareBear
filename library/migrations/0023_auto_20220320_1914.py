# Generated by Django 3.1.7 on 2022-03-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0022_auto_20220320_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkbox',
            name='task',
        ),
        migrations.AddField(
            model_name='checkbox',
            name='name',
            field=models.CharField(default='', help_text='name', max_length=250, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='checkbox',
            name='title',
            field=models.CharField(default='', help_text='title', max_length=250, verbose_name='title'),
        ),
    ]