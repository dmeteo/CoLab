# Generated by Django 5.0.4 on 2024-06-20 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_slug_alter_project_about_alter_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='author',
            field=models.CharField(blank=True, null=True, verbose_name='Автор'),
        ),
    ]
