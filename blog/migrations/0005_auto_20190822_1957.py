# Generated by Django 2.2.4 on 2019-08-22 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190813_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_image',
            field=models.ImageField(upload_to='blog'),
        ),
    ]
