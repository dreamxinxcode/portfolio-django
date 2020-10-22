# Generated by Django 2.2.4 on 2019-08-31 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_project_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_link',
            new_name='project_client_website',
        ),
        migrations.AddField(
            model_name='project',
            name='project_client',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='project_client_industry',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='project_intro',
            field=models.TextField(default=1),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_github',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]