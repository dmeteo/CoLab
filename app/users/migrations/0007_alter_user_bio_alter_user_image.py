# Generated by Django 5.0.4 on 2024-06-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_avg_rate_user_bio_user_course_user_institute_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(default='', null=True, verbose_name='О себе, кратко'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to='users_images/', verbose_name='Аватар'),
        ),
    ]
