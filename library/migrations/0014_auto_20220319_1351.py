# Generated by Django 3.1.7 on 2022-03-19 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_auto_20220319_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthstatus',
            name='comment',
            field=models.CharField(default='', help_text='comment', max_length=250, verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='healthstatus',
            name='date',
            field=models.DateTimeField(auto_now_add=True, help_text='date', verbose_name='date'),
        ),
        migrations.CreateModel(
            name='Checkboxes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', help_text='title', max_length=250, verbose_name='title')),
                ('checkboxes', models.ManyToManyField(help_text='task', related_name='checkboxes', to='library.Checkbox', verbose_name='task')),
            ],
            options={
                'verbose_name': 'checkboxes',
                'verbose_name_plural': 'checkboxes',
                'db_table': 'library.checkboxes',
            },
        ),
        migrations.AddField(
            model_name='healthstatus',
            name='custom',
            field=models.ManyToManyField(help_text='custom', related_name='custom', to='library.Checkboxes', verbose_name='custom'),
        ),
    ]
