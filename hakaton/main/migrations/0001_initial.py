# Generated by Django 3.2.6 on 2021-10-03 09:05

import ckeditor_uploader.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('video', models.FileField(upload_to='lessons<django.db.models.fields.UUIDField>_videos/')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
