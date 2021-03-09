# Generated by Django 3.1.7 on 2021-03-09 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, help_text='rating', max_digits=3, verbose_name='rating'),
        ),
    ]
