# Generated by Django 3.2.6 on 2021-10-17 04:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_delete_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('lessons', models.ManyToManyField(blank=True, to='main.Lesson')),
            ],
        ),
    ]
