from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,FileResponse
from rest_framework import viewsets
from .serializers import *
from django.views.generic import View
from .models import *
from django.core import serializers
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
    tl=Teacher.objects.all()
    request.session['uh']=12
    tl_json = serializers.serialize('json',tl)
    user = User.objects.get(id=Session.objects.get(session_key=request.COOKIES['sessionid']).get_decoded()['_auth_user_id'])
    print(user.username)
    return HttpResponse(tl_json,content_type='application/json')