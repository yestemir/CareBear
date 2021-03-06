# Generated by Django 3.1.7 on 2022-03-19 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_healthstatus_custom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthstatus',
            name='custom',
            field=models.ManyToManyField(blank=True, help_text='custom', related_name='custom', to='library.Checkboxes', verbose_name='custom'),
        ),
        migrations.AlterField(
            model_name='healthstatus',
            name='nutrition',
            field=models.ManyToManyField(blank=True, help_text='nutrition', related_name='nutrition', to='library.Checkbox', verbose_name='nutrition'),
        ),
        migrations.AlterField(
            model_name='healthstatus',
            name='pills',
            field=models.ManyToManyField(blank=True, help_text='pills', related_name='pills', to='library.Checkbox', verbose_name='pills'),
        ),
        migrations.AlterField(
            model_name='healthstatus',
            name='todos',
            field=models.ManyToManyField(blank=True, help_text='todos', related_name='todos', to='library.Checkbox', verbose_name='todos'),
        ),
    ]
