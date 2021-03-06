# Generated by Django 3.1.7 on 2022-05-06 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0026_auto_20220506_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='name', max_length=250, verbose_name='name')),
                ('description', models.CharField(default='', help_text='description', max_length=250, verbose_name='description')),
            ],
            options={
                'verbose_name': 'badge',
                'verbose_name_plural': 'badge',
                'db_table': 'library.badges',
            },
        ),
        migrations.CreateModel(
            name='UserBadge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('have_seen', models.BooleanField(default=False, help_text='have_seen', verbose_name='have_seen')),
                ('current_days_steak', models.IntegerField(default=0, help_text='current_days_steak', verbose_name='current_days_steak')),
                ('current_perfect_days_steak', models.IntegerField(default=0, help_text='current_perfect_days_steak', verbose_name='current_perfect_days_steak')),
                ('badge', models.ForeignKey(help_text='badge', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_badge', to='library.badge', verbose_name='badge')),
                ('user', models.ForeignKey(help_text='user', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_badge', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'user_badge',
                'verbose_name_plural': 'user_badge',
                'db_table': 'library.user_badges',
            },
        ),
    ]
