# Generated by Django 2.2.4 on 2019-08-13 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='open_source',
            field=models.BooleanField(default=True),
        ),
    ]
