# Generated by Django 2.2.4 on 2019-08-13 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
