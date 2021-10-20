from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,FileResponse
from rest_framework import viewsets
from .serializers import *
from django.views.generic import View,ListView
from .models import *
from django.core import serializers
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class  index(View):
    def get(self, request, *args, **kw):
        tl=Teacher.objects.all()
        request.session['uh']=12
        tl_json = serializers.serialize('json',tl)
        send_mail(
            'Subject here',
            'Here is the message.',
            'bahromiddinibragimov03brr@gmail.com',
            ['bahromiddinibragimov03brr@gmail.com'],
            fail_silently=False,
        )
        for i in request.META:
            print(i,request.META[i])
        return HttpResponse(tl_json,content_type='application/json')
class teachers(ListView):
    model = Teacher
    template_name='teachers.html'