# Generated by Django 2.2.4 on 2019-08-12 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_image', models.ImageField(upload_to='projects')),
                ('project_title', models.CharField(max_length=100)),
                ('project_description', models.TextField()),
                ('project_link', models.CharField(max_length=100)),
                ('project_github', models.CharField(max_length=100)),
            ],
        ),
    ]