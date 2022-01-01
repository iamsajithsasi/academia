from django.contrib import admin
from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('sample', views.sample),
    path('', views.index),
    path('list', views.StudentList),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]