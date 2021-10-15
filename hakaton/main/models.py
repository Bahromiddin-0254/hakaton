from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator


# Create your models here.
class Lesson(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4)
    title = models.CharField(max_length=250)
    video = models.FileField(upload_to=f"lessons{uuid}_videos/",validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    text = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Teacher(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    lessons = models.ManyToManyField(Lesson, blank=True)
    @classmethod
    def full_name(cls):
        "Full name"
        return cls.objects.all()

__all__ = ["Lesson","Teacher"]
