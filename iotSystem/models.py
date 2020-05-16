#coding:utf-8
from __future__ import unicode_literals


from django.db import models
from datetime import datetime
# Create your models here.
class Data(models.Model):
    humi=models.CharField(max_length=20,default="",verbose_name=u"湿度")
    temp=models.CharField(max_length=20,default="",verbose_name=u"温度")
    #at=models.CharField(max_length=20,default="",verbose_name=u"光照")
    pm= models.CharField(max_length=20, default='',verbose_name=u"粉尘")
    #position args
    jingdu = models.CharField(max_length=20, default='', verbose_name=u"经度")
    weidu = models.CharField(max_length=20, default='', verbose_name=u"维度")
    time=models.DateTimeField(default=datetime.now,verbose_name=u"采集数据时间")
    class Meta:
        ordering=("time",)
        verbose_name=u"数据信息"
        verbose_name_plural=verbose_name
    # def __str__(self):
    #     return self.name
class Warning(models.Model):
    mailtitle=models.CharField(max_length=50,default="浓度超标了",verbose_name=u"邮件标题")
    messageContent=models.TextField(default="报警！",verbose_name=u"报警内容")
    value=models.IntegerField(default=100,verbose_name=u"阈值")
    interval=models.IntegerField(default=10,verbose_name=u"报警时间间隔")
    level=models.CharField(max_length=20,default="primary",choices=(("primary","初级报警"),("serious","严重报警"),("fatal","致命报警")),verbose_name="报警类型");
    class Meta:
        verbose_name=u"报警信息"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.level


class SaveWarning(models.Model):
    warning=models.ForeignKey(Warning,verbose_name="所属报警", on_delete=models.CASCADE)
    currentvalue=models.CharField(max_length=10,default="",verbose_name=u"报警平均值")
    time = models.DateTimeField(default=datetime.now, verbose_name=u"报警时间")
    class Meta:
        verbose_name=u"报警信息记录"
        verbose_name_plural=verbose_name


##############################
#添加的新模型:
##############################






class Incubator(models.Model):
    #培养箱
    STATUS_CHOICES = (
        ('disconnected', "未连接"),
        ('connected', "已连接"),
        ('breakdown', "故障")
    )
    #此编号形式没有任何规定
    iden = models.CharField(max_length=20, primary_key=True, verbose_name="编号")
    key = models.CharField(max_length=20, verbose_name="密钥")
    stat = models.CharField(max_length=20, default="disconnected", choices=STATUS_CHOICES, verbose_name='状态')
    user_phon = models.CharField( max_length=11, null=True, blank=True, verbose_name='电话号码',)
    time = models.DateTimeField( default=datetime.now, verbose_name='注册日期',)


    class Meta:
        ordering=("iden",)
        verbose_name=u"培养箱"
        verbose_name_plural=verbose_name


class Environment(models.Model):
    #培养箱环境数据信息
    humi_land=models.CharField(max_length=20,default="",verbose_name=u"土壤湿度")
    humi_area = models.CharField(max_length=20, default="", verbose_name=u"大气湿度")
    temp_area = models.CharField(max_length=20, default="", verbose_name=u"空气温度")
    temp_land=models.CharField(max_length=20,default="",verbose_name=u"土壤温度")
    illu=models.CharField(max_length=20,default="",verbose_name=u"光照")
    pres= models.CharField(max_length=20, default='',verbose_name=u"压强")
    #position args
    longi = models.CharField(max_length=20, default='', verbose_name=u"经度")
    lati = models.CharField(max_length=20, default='', verbose_name=u"维度")
    time=models.DateTimeField(default=datetime.now,verbose_name=u"采集数据时间")
    image = models.TextField(verbose_name=u"监控图片", blank=True, null=True)
    incubator_iden = models.CharField(max_length=20, verbose_name=u"培养箱编号")


    class Meta:
        ordering=("time",)
        verbose_name=u"培养箱环境"
        verbose_name_plural=verbose_name


class Control(models.Model):
    #用于存放用户控制培养箱的信息
    humi_land=models.CharField(max_length=20,default="",verbose_name=u"土壤湿度")
    humi_area = models.CharField(max_length=20, default="", verbose_name=u"大气湿度")
    temp_area = models.CharField(max_length=20, default="", verbose_name=u"空气温度")
    temp_land=models.CharField(max_length=20,default="",verbose_name=u"土壤温度")
    illu=models.CharField(max_length=20,default="",verbose_name=u"光照")
    pres= models.CharField(max_length=20, default='',verbose_name=u"压强")
    #position args
    time=models.DateTimeField(default=datetime.now,verbose_name=u"修改时间")
    incubator_iden = models.CharField(max_length=20, verbose_name=u"培养箱编号")


    class Meta:
        ordering=("time",)
        verbose_name=u"控制记录"
        verbose_name_plural=verbose_name




class DataWarning(models.Model):
    #培养箱中的数据超标时发送报警邮件
    mailtitle=models.CharField(max_length=50,default="浓度超标了",verbose_name=u"邮件标题")
    messageContent=models.TextField(default="报警！",verbose_name=u"报警内容")
    value=models.IntegerField(default=100,verbose_name=u"阈值")
    interval=models.IntegerField(default=10,verbose_name=u"报警时间间隔")
    level=models.CharField(max_length=20,default="primary",choices=(("primary","初级报警"),("serious","严重报警"),("fatal","致命报警")),verbose_name="报警类型");
    class Meta:
        verbose_name=u"报警信息"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.level


class SaveDataWarning(models.Model):
    #保存一条报警数据的记录
    warning=models.ForeignKey(Warning,verbose_name="所属报警", on_delete=models.CASCADE)
    currentvalue=models.CharField(max_length=10,default="",verbose_name=u"报警平均值")
    time = models.DateTimeField(default=datetime.now, verbose_name=u"报警时间")
    class Meta:
        verbose_name=u"报警信息记录"
        verbose_name_plural=verbose_name