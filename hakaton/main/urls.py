from django.urls import path
from . import views
from rest_framework import routers
from django.urls import include
app_name = 'main'
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('index',views.index.as_view(),name='index'),
    path('teachers/',views.teachers.as_view(),name='teachers')
]
