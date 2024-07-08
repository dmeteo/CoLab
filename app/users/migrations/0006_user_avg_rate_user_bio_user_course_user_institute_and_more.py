# Generated by Django 5.0.4 on 2024-06-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_options_alter_profile_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avg_rate',
            field=models.CharField(default=0.0, null=True, verbose_name='Средняя оценка'),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(null=True, verbose_name='О себе, кратко'),
        ),
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.SmallIntegerField(null=True, verbose_name='Курс'),
        ),
        migrations.AddField(
            model_name='user',
            name='institute',
            field=models.CharField(null=True, verbose_name='Институт'),
        ),
        migrations.AddField(
            model_name='user',
            name='trend',
            field=models.CharField(null=True, verbose_name='Направление'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
