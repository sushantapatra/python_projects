# Generated by Django 4.2.6 on 2023-10-27 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
