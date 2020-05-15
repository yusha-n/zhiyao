#coding:utf-8
from django.conf.urls import url,include
from django.urls import path
from . import views
app_name = 'iotSystem'

urlpatterns = [
    path('', views.index, name='index'),
    path('introduce/', views.introduce, name="introduce"),
    path('data_dis/', views.data_dis, name='data_dis'),
    path('historyDataFilter/', views.historyDataFilter, name="historyDataFilter"),
    path('data_history',views.data_history,name="data_history"),
    path('warningHistory/', views.warningHistory, name="warningHistory"),
    path('data_in/',views.data_in,name="data_in"),
    path('ajax_data/', views.ajax_data, name="ajax_data"),
    path('position/', views.position, name="position"),
    path('background/', views.background, name="background"),
    path('control-old/', views.control_old, name="control-old"),
    path('connect/', views.connect, name="connect"),
    path('dev-list/', views.dev_list, name="dev-list"),
    path('dev-detail/<str:iden>/', views.dev_detail, name='dev-detail'),
    path('control/<str:iden>/', views.control, name='control',),
    path('profile/', views.profile, name="profile")
]
# urlpatterns = [
#
#     path(r'^index/$',views.index,name='index'),
#     path(r'^data_dis/$', views.data_dis, name='data_dis'),
#     #path(r'^state_in/$',views.state_in,name="state_in"),
#     path(r'^data_history/$',views.data_history,name="data_history"),
#     path(r"data_in/$",views.data_in,name="data_in"),
#     path(r"ajax_data/$", views.ajax_data, name="ajax_data"),
#    #path(r"^dataShow/$",views.dataShow,name="dataShow"),
#     path(r"^position/$", views.position, name="position"),
#     path(r"^historyDataFilter/$", views.historyDataFilter, name="historyDataFilter"),
#     path(r"^introduce/$", views.introduce, name="introduce"),
#     path(r"^background/$", views.background, name="background"),
#     path(r"^warningHistory/$", views.warningHistory, name="warningHistory"),
#     path(r"^control/$", views.control, name="control"),
# ]
#
