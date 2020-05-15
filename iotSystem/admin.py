#coding:utf-8
from django.contrib import admin
from .models import Data,Warning,SaveWarning,Incubator,Environment,Control
admin.site.site_header=u"智药后台管理系统"
admin.site.site_title=u"智药"
#Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ("humi","temp","time","pm","jingdu","weidu")
    list_per_page = 30
    ordering = ("-time",)
admin.site.register(Data,DataAdmin)

class WaringAdmin(admin.ModelAdmin):
    list_display=["mailtitle","messageContent","value","level"]

admin.site.register(Warning,WaringAdmin)

class SavewarningAdmin(admin.ModelAdmin):
    list_display = ["warning","currentvalue","time"]

admin.site.register(SaveWarning,SavewarningAdmin)

class IncubatorAdmin(admin.ModelAdmin):
    list_display = ['user_phon', 'iden', 'key', 'stat', 'time']

admin.site.register(Incubator, IncubatorAdmin)

class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ['incubator_iden', 'humi_land', 'humi_area', 'temp_land', 'temp_area', 'pres', 'illu', 'time',]

admin.site.register(Environment, EnvironmentAdmin)

class ControlAdmin(admin.ModelAdmin):
    list_display = ['incubator_iden', 'humi_land', 'humi_area', 'temp_land', 'temp_area', 'pres', 'illu', 'time',]

admin.site.register(Control, ControlAdmin)