# Generated by Django 3.1.7 on 2022-03-19 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20220319_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthstatus',
            name='nutrition',
            field=models.ForeignKey(help_text='task', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nutrition', to='library.checkbox', verbose_name='task'),
        ),
        migrations.AddField(
            model_name='healthstatus',
            name='pills',
            field=models.ForeignKey(help_text='task', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pills', to='library.checkbox', verbose_name='task'),
        ),
        migrations.AddField(
            model_name='healthstatus',
            name='todos',
            field=models.ForeignKey(help_text='task', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='todos', to='library.checkbox', verbose_name='task'),
        ),
        migrations.DeleteModel(
            name='Checkboxes',
        ),
    ]
