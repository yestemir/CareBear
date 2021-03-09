# Generated by Django 3.1.7 on 2021-03-09 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title', max_length=32, verbose_name='title')),
                ('description', models.TextField(default='', help_text='description', verbose_name='description')),
                ('author', models.CharField(default='', help_text='author', max_length=32, verbose_name='author')),
                ('genre', models.CharField(default='', help_text='genre', max_length=32, verbose_name='genre')),
                ('rating', models.DecimalField(decimal_places=1, default=0, help_text='rating', max_digits=1, verbose_name='rating')),
                ('image', models.FileField(blank=True, upload_to='photos/%d-%m-%Y')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='created', verbose_name='created')),
                ('release_date', models.DateTimeField(help_text='release_date', verbose_name='release_date')),
                ('isbn', models.CharField(default='', help_text='isbn', max_length=32, verbose_name='isbn')),
                ('quantity', models.IntegerField(default=0, help_text='quantity', verbose_name='quantity')),
                ('language', models.CharField(default='russian', help_text='language', max_length=32, verbose_name='language')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
                'db_table': 'library.books',
            },
        ),
    ]
