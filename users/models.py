#coding:utf-8
from __future__ import unicode_literals


from django.db import models
# Create your models here.
# class UserProfile(AbstractUser):
#     nick_name=models.CharField(max_length=50,verbose_name=u'昵称',default='')
#     class Meta:
#         verbose_name=u'用户信息'
#         verbose_name_plural=verbose_name
#     def __str__(self):
#         return self.username


from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User




class UserProfile(models.Model):
    SEX_CHOICES=(
        ('male', "男"),
        ('female', "女"),
        ('other', '其他'),
        ('secret', '保密'),
    )
    STATUS_CHOICES=(
        ('alive', "活跃"),
        ('silence', '禁言'),
        ('restrict', '限制登录'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户认证表')
    phon = models.CharField(verbose_name='电话号码', max_length=11, unique='True', )
    #emai = models.CharField(verbose_name='邮箱', unique=True, max_length=50)
    stat = models.CharField( default='alive', max_length=20,  choices=STATUS_CHOICES, verbose_name='账户状态')  # Field name made lowercase.
    sex = models.CharField(max_length=20, default="secret", choices=SEX_CHOICES, verbose_name='性别', )
    img = models.TextField(default="md.img", verbose_name='头像')
    intr = models.TextField(default="一个神秘的果壳", verbose_name='个人简介')


    class Meta:
        #按照账户最近一次登录的时间排序
        verbose_name=u"配置"
        verbose_name_plural=verbose_name


    def __str__(self):
        #必须返回一个字符串
        return self.phon