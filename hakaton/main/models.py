from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
import uuid
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Lesson(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4)
    title = models.CharField(max_length=250)
    video = models.FileField(upload_to="lessons{0}_videos/".format(uuid))
    text = RichTextUploadingField()