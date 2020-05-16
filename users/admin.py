from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import UserProfile
# Register your models here.

class UserProfileInline(admin.TabularInline):
    model = UserProfile
    can_delete = False
    #表示别名(复数的形式)
    verbose_name_plural = '用户配置信息'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['intr', 'phon', 'img', 'sex']

admin.site.register(UserProfile, UserProfileAdmin)