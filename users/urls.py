#coding:utf-8
from django.conf.urls import url,include
from . import views
from .views import LoginView,LogoutView

app_name = 'users'
urlpatterns = [
    url(r'^$',LoginView.as_view(),name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]