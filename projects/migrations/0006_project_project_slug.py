# Generated by Django 2.2.4 on 2019-08-31 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20190831_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_slug',
            field=models.SlugField(default=1, max_length=100),
        ),
    ]
