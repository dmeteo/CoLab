# Generated by Django 5.0.4 on 2024-06-20 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='author',
        ),
    ]
