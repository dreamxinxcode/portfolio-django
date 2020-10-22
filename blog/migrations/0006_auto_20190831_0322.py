# Generated by Django 2.2.4 on 2019-08-31 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190822_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='blog_slug',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]
