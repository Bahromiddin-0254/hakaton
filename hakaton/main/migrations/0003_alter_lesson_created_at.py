# Generated by Django 3.2.6 on 2021-10-13 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_lesson_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]