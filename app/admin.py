from django.contrib import admin

# Register your models here.
from django.contrib import admin

from . import models

class BuypostInline(admin.TabularInline):
    model = models.Buypost
    extra = 1
class BuypostAdmin(admin.ModelAdmin):
    list_display = ['bid', 'bplant', 'bdescription', 'bphonenum', 'bprice', 'releasebtime', 'user_userid']
    #设置带链接（可以点进去修改记录）的字段
    list_display_links = ['bid']
    ordering = ['bid']
    #fields = ['userphonenum', 'usermail']
    #inlines = [BuypostInline]
    #list_filter = ['username', 'userphonenum']
    search_fields = ['bplant', 'releasebtime']
    list_per_page = 5

def make_published(modeladmin, request, queryset):
    queryset.update(usersex=9)
make_published.short_description = "让选中的用户性别改为9"
class UserAdmin(admin.ModelAdmin):
    list_display = ['userphonenum', 'userid', 'usermail', 'usersex', 'username']
    #设置带链接（可以点进去修改记录）的字段
    list_display_links = ['userid']
    ordering = ['userid']
    actions = [make_published]
    fields = ['userphonenum', 'usermail']
    inlines = [BuypostInline]
    list_filter = ['username', 'userphonenum']
    search_fields = ['username']
    list_per_page = 2

class PlantAdmin(admin.ModelAdmin):
    list_filter = ('plantname', 'pavermark',)
    list_display = [ 'plantname', 'pplantaverpeople', 'pplantavertime', 'pavermark']
    list_per_page = 2

class IncubatorAdmin(admin.ModelAdmin):
    list_display = ['incuno', 'incuname', 'purchasetime', 'user_userid', 'usetime', 'managerstage']
    list_per_page = 1

admin.site.register(models.Plant, PlantAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Buypost, BuypostAdmin)
admin.site.register(models.Incubator, IncubatorAdmin)
# admin.site.register(models.Incubatorusing)
# admin.site.register(models.Monitorinform)
# admin.site.register(models.Plant)
# admin.site.register(models.Alterenvironment)
# admin.site.register(models.Sellpost)
# admin.site.register(models.Commentpost)
# admin.site.register(models.ChangeLog)
# admin.site.register(models.ViewParam)

admin.site.site_header = '智药后台管理系统'