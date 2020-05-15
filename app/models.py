# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


from datetime import datetime
from django.db import models


class ChangeLog(models.Model):
    tem=models.CharField(max_length=5)#温度
    pre=models.CharField(max_length=6)#压强
    hum=models.CharField(max_length=5)#湿度
    led=models.CharField(max_length=5)#光照
    addtime=models.DateTimeField(default=datetime.now)#最后一次更新时间


class ViewParam(models.Model):
    tem=models.CharField(max_length=5)#温度
    pre=models.CharField(max_length=6)#压强
    hum=models.CharField(max_length=5)#湿度
    led=models.CharField(max_length=5)#光照
    addtime=models.DateTimeField(auto_now=True)#最近一次更新时间


class Alterenvironment(models.Model):
    #修改环境信息
    alteid = models.CharField(db_column='AltEid', primary_key=True, max_length=45)  # Field name made lowercase.
    atime = models.DateTimeField(db_column='ATime',auto_now=True)  # Field name made lowercase.
    incubatorusing_iuno = models.ForeignKey('Incubatorusing', models.DO_NOTHING, db_column='IncubatorUsing_IUNo', blank=True, null=True)  # Field name made lowercase.
    atemperature = models.FloatField(db_column='ATemperature', blank=True, null=True)  # Field name made lowercase.
    ahumidity = models.FloatField(db_column='AHumidity', blank=True, null=True)  # Field name made lowercase.
    alightlntensity = models.FloatField(db_column='ALightlntensity', blank=True, null=True)  # Field name made lowercase.
    apressure = models.FloatField(db_column='APressure', blank=True, null=True)  # Field name made lowercase.
    aplantstage = models.CharField(db_column='APlantStage', max_length=20, blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'alterenvironment'
        verbose_name_plural = '修改环境信息'


class Buypost(models.Model):
    bid = models.CharField(verbose_name='编号', db_column='BID', primary_key=True, max_length=30)  # Field name made lowercase.
    bplant = models.TextField(verbose_name='名称', db_column='BPlant')  # Field name made lowercase.
    bdescription = models.TextField(verbose_name='描述', db_column='BDescription')  # Field name made lowercase.
    bphonenum = models.CharField(verbose_name='联系方式', db_column='BPhoneNum', max_length=11)  # Field name made lowercase.
    bprice = models.DecimalField(verbose_name='价格', db_column='BPrice', max_digits=6, decimal_places=2)  # Field name made lowercase.
    releasebtime = models.DateTimeField(verbose_name='发布时间', db_column='releaseBTime',auto_now=True)  # Field name made lowercase.
    user_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='User_userId', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'buypost'
        verbose_name_plural = '订单'


class Cart(models.Model):
    cartid = models.CharField(db_column='CartID', primary_key=True, max_length=50)  # Field name made lowercase.
    citemname = models.CharField(db_column='CItemName', max_length=45)  # Field name made lowercase.
    citemnum = models.IntegerField(db_column='CItemNum')  # Field name made lowercase.
    citembasicprice = models.DecimalField(db_column='CItemBasicPrice', max_digits=6, decimal_places=2)  # Field name made lowercase.
    user_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='User_userId', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'cart'
        verbose_name_plural = '购物车'


class Commentpost(models.Model):
    ctitle = models.CharField(db_column='CTitle', max_length=50)  # Field name made lowercase.
    cid = models.CharField(db_column='CID', primary_key=True, max_length=20)  # Field name made lowercase.
    cdescription = models.TextField(db_column='CDescription')  # Field name made lowercase.
    cimage = models.TextField(db_column='CImage', blank=True, null=True)  # Field name made lowercase.
    releasectime = models.DateTimeField(db_column='releaseCTime')  # Field name made lowercase.
    user_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='User_userId', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'commentpost'
        verbose_name_plural = '评论'


class Customenvironment(models.Model):
    #自定义信息
    ceid = models.CharField(db_column='CEid', primary_key=True, max_length=45)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='addTime')  # Field name made lowercase.
    cname = models.CharField(db_column='CName', max_length=100)  # Field name made lowercase.
    cvalue = models.DecimalField(db_column='CValue', max_digits=10, decimal_places=0)  # Field name made lowercase.
    cunit = models.CharField(db_column='CUnit', max_length=10)  # Field name made lowercase.
    cplantstage = models.CharField(db_column='CPlantStage', max_length=20)  # Field name made lowercase.
    cnotes = models.TextField(db_column='CNotes', blank=True, null=True)  # Field name made lowercase.
    incubatorusing_iuno = models.ForeignKey('Incubatorusing', models.DO_NOTHING, db_column='IncubatorUsing_IUNo', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'customenvironment'
        verbose_name_plural = '定制环境'


class Customstatistics(models.Model):
    #自定义的环境的统计信息
    cstaticid = models.CharField(db_column='CStaticid', primary_key=True, max_length=45)  # Field name made lowercase.
    cname = models.CharField(db_column='CName', max_length=100)  # Field name made lowercase.
    csvalue = models.DecimalField(db_column='CSValue', max_digits=10, decimal_places=0)  # Field name made lowercase.
    cunit = models.CharField(db_column='CUnit', max_length=10)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    plantstatistics_pstaticid = models.ForeignKey('Plantstatistics', models.DO_NOTHING, db_column='PlantStatistics_PStaticid', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'customstatistics'
        verbose_name_plural = '定制环境统计参数'


class Incubator(models.Model):
    #培养箱实体的信息
    incuno = models.CharField(verbose_name='编号', db_column='IncuNo', primary_key=True, max_length=20)  # Field name made lowercase.
    incuname = models.CharField(verbose_name='名称', db_column='IncuName', max_length=45)  # Field name made lowercase.
    purchasetime = models.DateTimeField(verbose_name='购买时间', db_column='purchaseTime', blank=True, null=True)  # Field name made lowercase.
    user_userid = models.ForeignKey('User', models.DO_NOTHING, verbose_name='用户', db_column='User_userId', blank=True, null=True)  # Field name made lowercase.
    usetime = models.IntegerField(verbose_name='使用时长', db_column='useTime',null=True)
    managerstage = models.CharField(verbose_name='状态', db_column='managerStage',max_length=45, null=True)


    class Meta:
        managed = True
        db_table = 'incubator'
        verbose_name_plural = '培养箱'


class Incubatorusing(models.Model):
    #正在使用的培养箱的信息
    iuno = models.CharField(db_column='IUNo', primary_key=True, max_length=20)  # Field name made lowercase.
    initializetime = models.DateTimeField(db_column='initializeTime')  # Field name made lowercase.
    itemperature = models.FloatField(db_column='ITemperature', blank=True, null=True)  # Field name made lowercase.
    ihumidity = models.FloatField(db_column='IHumidity', blank=True, null=True)  # Field name made lowercase.
    ipressure = models.FloatField(db_column='IPressure', blank=True, null=True)  # Field name made lowercase.
    ilightlntensity = models.FloatField(db_column='ILightlntensity', blank=True, null=True)  # Field name made lowercase.
    #istate = models.IntegerField(db_column="IState", blank=True, null=True, default=0)
    incubator_incuno = models.ForeignKey(Incubator, models.DO_NOTHING, db_column='Incubator_IncuNo', blank=True, null=True)  # Field name made lowercase.
    plant_plantname = models.ForeignKey('Plant', models.DO_NOTHING, db_column='Plant_plantName', blank=True, null=True)  # Field name made lowercase.
    user_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='User_userId', blank=True, null=True)  # Field name made lowercase.




    class Meta:
        managed = True
        db_table = 'incubatorusing'
        verbose_name_plural = '运行中的培养箱'


class Monitorinform(models.Model):
    #monitorid = models.CharField(db_column='Monitorid', primary_key=True, max_length=45)  # Field name made lowercase.
    mtime = models.DateTimeField(db_column='MTime',default=datetime.now,)  # Field name made lowercase.
    incubatorusing_iuno = models.ForeignKey(Incubatorusing, models.DO_NOTHING, db_column='IncubatorUsing_IUNo', blank=True, null=True)  # Field name made lowercase.
    mtemperature = models.FloatField(db_column='MTemperature')  # Field name made lowercase.
    mhumidity = models.FloatField(db_column='MHumidity')  # Field name made lowercase.
    mpressure = models.FloatField(db_column='MPressure')  # Field name made lowercase.
    mlightlntensity = models.FloatField(db_column='MLightlntensity')  # Field name made lowercase.
    mplantstage = models.CharField(db_column='MPlantStage', max_length=20)  # Field name made lowercase.
    mscore = models.IntegerField(db_column='MScore', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'monitorinform'
        verbose_name_plural = '监视'


class Order(models.Model):
    orderid = models.CharField(db_column='orderId', primary_key=True, max_length=50)  # Field name made lowercase.
    odatetime = models.DateTimeField(db_column='ODateTime')  # Field name made lowercase.
    oreceivername = models.CharField(db_column='OReceiverName', max_length=45)  # Field name made lowercase.
    oaddress = models.CharField(db_column='OAddress', max_length=45)  # Field name made lowercase.
    oreceiverphon = models.CharField(db_column='OReceiverPhon', max_length=11)  # Field name made lowercase.
    ordertotalprice = models.DecimalField(db_column='orderTotalPrice', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    user_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='User_userId', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'order'
        verbose_name_plural = '订单'


class Orderitem(models.Model):
    orderitemid = models.CharField(db_column='orderItemId', primary_key=True, max_length=45)  # Field name made lowercase.
    oiname = models.CharField(db_column='OIName', max_length=50)  # Field name made lowercase.
    oinum = models.IntegerField(db_column='OINum')  # Field name made lowercase.
    oibasicprice = models.DecimalField(db_column='OIBasicPrice', max_digits=6, decimal_places=2)  # Field name made lowercase.
    order_orderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='Order_orderId', blank=True, null=True)  # Field name made lowercase.
    product_productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='Product_productID', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'orderitem'
        verbose_name_plural = '订单记录'


# class Plant(models.Model):
#     plantID = models.CharField(verbose_name='编号', db_column='PlantNo', primary_key=True,
#                      max_length=20)  # Field name made lowercase.
#     plantname = models.CharField(verbose_name='名称', db_column='plantName', max_length=50)  # Field name made lowercase.
#     #pplantaverpeople = models.IntegerField(verbose_name='培养人', db_column='pplantaverPeople' , null=True)
#     pplantaverpeople = models.CharField(verbose_name='培养人', db_column='pplantaverPeople', max_length=50, null=True)
#     #pplantsumpeople = models.IntegerField(db_column='pplantsumPeople' , null=True)
#     #pplantavertime = models.IntegerField(verbose_name='种植时间', db_column='pplantaverTime' , null=True)
#     pplantavertime = models.DateTimeField(verbose_name='时间', db_column='pplantaverTime', blank=True, null=True)  # Field name made lowercase.
#     #pplantsumtime = models.IntegerField(db_column='pplantsumTime' , null=True)
#     pavermark = models.IntegerField(verbose_name='评分', db_column='paverMark' , null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'plant'
#         #verbose_name = '植物'
#         verbose_name_plural = '植物'


class Plant(models.Model):
    #plantID = models.CharField(verbose_name='编号', db_column='PlantNo', primary_key=True,
     #                max_length=20)  # Field name made lowercase.
    plantname = models.CharField(verbose_name='名称', db_column='plantName', primary_key=True, max_length=50)  # Field name made lowercase.
    #pplantaverpeople = models.IntegerField(verbose_name='培养人', db_column='pplantaverPeople' , null=True)
    pplantaverpeople = models.CharField(verbose_name='培养人', db_column='pplantaverPeople', max_length=50, null=True)
    pplantsumpeople = models.IntegerField(db_column='pplantsumPeople' , null=True)
    #pplantavertime = models.IntegerField(verbose_name='种植时间', db_column='pplantaverTime' , null=True)
    pplantavertime = models.DateTimeField(verbose_name='时间', db_column='pplantaverTime', blank=True, null=True)  # Field name made lowercase.
    pplantsumtime = models.IntegerField(db_column='pplantsumTime' , null=True)
    pavermark = models.IntegerField(verbose_name='评分', db_column='paverMark' , null=True)


    class Meta:
        managed = True
        db_table = 'plant'
        #verbose_name = '植物'
        verbose_name_plural = '植物'


class Plantstatistics(models.Model):
    pstaticid = models.CharField(db_column='PStaticid', primary_key=True, max_length=45)  # Field name made lowercase.
    plantstage = models.CharField(db_column='plantStage', max_length=20, default="firststage")  # Field name made lowercase.
    plant_plantname = models.ForeignKey(Plant, models.DO_NOTHING, db_column='Plant_plantName', blank=True, null=True)  # Field name made lowercase.
    stemperature = models.FloatField(db_column='STemperature')  # Field name made lowercase.
    shumidity = models.FloatField(db_column='SHumidity')  # Field name made lowercase.
    spressure = models.FloatField(db_column='SPressure')  # Field name made lowercase.
    slightlntensity = models.FloatField(db_column='Slightlntensity')  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'plantstatistics'
        verbose_name_plural = '植物统计'


class Product(models.Model):
    productid = models.CharField(db_column='productID', primary_key=True, max_length=20)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=45)  # Field name made lowercase.
    pdescribtion = models.TextField(db_column='pDescribtion', blank=True, null=True)  # Field name made lowercase.
    pprice = models.DecimalField(db_column='pPrice', max_digits=6, decimal_places=2)  # Field name made lowercase.
    producteddate = models.DateField(db_column='productedDate')  # Field name made lowercase.
    expirationdate = models.DateField(db_column='expirationDate')  # Field name made lowercase.
    repository_productclass = models.ForeignKey('Repository', models.DO_NOTHING, db_column='Repository_productClass', blank=True, null=True)  # Field name made lowercase.
    productrepertory = models.IntegerField(db_column='productRepertory')  # Field name made lowercase.
    productunit = models.CharField(db_column='productUnit', max_length=45)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'product'
        verbose_name_plural = '产品'


class Productdetail(models.Model):
    pdid = models.CharField(db_column='PDid', primary_key=True, max_length=45)  # Field name made lowercase.
    pdname = models.CharField(db_column='PDName', max_length=45)  # Field name made lowercase.
    pdvalue = models.CharField(db_column='PDValue', max_length=45)  # Field name made lowercase.
    pdunit = models.CharField(db_column='PDUnit', max_length=45)  # Field name made lowercase.
    pdnotes = models.CharField(db_column='PDNotes', max_length=45, blank=True, null=True)  # Field name made lowercase.
    product_productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='Product_productID', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'productdetail'
        verbose_name_plural = '产品详情'


class Repository(models.Model):
    productclass = models.CharField(db_column='productClass', primary_key=True, max_length=50)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'repository'
        verbose_name_plural = '仓库'


class Sellpost(models.Model):
    sid = models.CharField(db_column='SID', primary_key=True, max_length=30)  # Field name made lowercase.
    splant = models.TextField(db_column='SPlant')  # Field name made lowercase.
    sdescription = models.TextField(db_column='SDescription')  # Field name made lowercase.
    sphonenum = models.CharField(db_column='SPhoneNum', max_length=11)  # Field name made lowercase.
    sprice = models.DecimalField(db_column='SPrice', max_digits=6, decimal_places=2)  # Field name made lowercase.
    simage = models.TextField(db_column='SImage', blank=True, null=True)  # Field name made lowercase.
    sscore = models.IntegerField(db_column='SScore', blank=True, null=True)  # Field name made lowercase.
    releasestime = models.DateTimeField(db_column='releaseSTime')  # Field name made lowercase.
    user_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='User_userId', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'sellpost'
        verbose_name_plural = '销售单'


class User(models.Model):
    userid = models.CharField(db_column='userId', primary_key=True, max_length=45)  # Field name made lowercase.
    userphonenum = models.CharField(verbose_name='电话号码',db_column='userPhoneNum', unique=True, max_length=11)  # Field name made lowercase.
    usermail = models.CharField(verbose_name='邮箱',db_column='userMail', unique=True, max_length=50)  # Field name made lowercase.
    username = models.CharField(verbose_name='用户名', db_column='userName', unique=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(max_length=50)
    userstate = models.IntegerField(db_column='userState',default=0)  # Field name made lowercase.
    registrationdate = models.DateTimeField(db_column='registrationDate',auto_now=True)  # Field name made lowercase.
    userimg = models.CharField(db_column='userImg', max_length=50, default="md.ipg")
    usersex = models.IntegerField(verbose_name='性别', db_column='userSex',default=0)
    userintroduction =models.CharField(db_column='userIntroduction', max_length=255 ,default="22")
    userlastlogintime = models.DateTimeField(db_column='userLastlogintime',null=True)


    class Meta:
        managed = True
        db_table = 'user'
        verbose_name_plural = '用户'




######新加数据库######




class MangerUser(models.Model):
    muserid = models.CharField(db_column='MuserId', primary_key=True, max_length=45)
    musername =models.CharField(db_column='MuserName', unique=True, max_length=50)
    muserphonenum = models.CharField(db_column='MuserPhoneNum', unique=True, max_length=11)
    mpassword = models.CharField(db_column='Mpassword', max_length=50)


    class Meta:
        managed = True
        db_table = 'MangerUser'
        verbose_name_plural = '管理用户'


class PlantShow(models.Model):
    spid = models.CharField(db_column='spID',primary_key=True,max_length=45)
    spname = models.CharField(db_column='spName',max_length=45,default="123")
    spintrc = models.CharField(db_column='spIntrc',max_length=255,default="eafef")
    spmark = models.CharField(db_column='spMark',max_length=45,default="23")
    spplantstime = models.DateField(db_column='spPlantstime',auto_now=True)
    spplantetime = models.DateField(db_column='spPlantetime',auto_now=True)
    spheat = models.CharField(db_column='spHeat',max_length=45,default="32")
    incubator_incuno = models.ForeignKey(Incubator, models.DO_NOTHING, db_column='Incubator_IncuNo', blank=True,null=True)


    class Meta:
        managed = True
        db_table = 'plantshow'
        verbose_name_plural = '可视植物'


class UsershowLink(models.Model):
    uslinkid = models.CharField(db_column='uslinkID',primary_key=True,max_length=45)
    user_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='User_userId', blank=True, null=True)
    plantshow_spid = models.ForeignKey('PlantShow', models.DO_NOTHING, db_column='plantshow_spID', blank=True,null=True)


    class Meta:
        managed = True
        db_table = 'usershowlink'
        verbose_name_plural = '可视用户'


class Incubatorhardinf(models.Model):
    inchardinfID = models.CharField(db_column='InchardinfID',primary_key=True, max_length=45)
    icpu = models.CharField(db_column='iCPU', max_length=45, null=True)
    itemph = models.CharField(db_column='iTemph', max_length=45, null=True)
    ihumh = models.CharField(db_column='iHumh', max_length=45, null=True)
    ipressh = models.CharField(db_column='iPressh', max_length=45, null=True)
    ilighth = models.CharField(db_column='iLighth', max_length=45, null=True)
    inchardinfdate = models.DateField(db_column=' inchardinfDate' , auto_now=True)
    incubator_incuno = models.ForeignKey(Incubator, models.DO_NOTHING, db_column='Incubator_IncuNo', blank=True,null=True)


    class Meta:
        managed = True
        db_table = 'incubatorhardinf'
        verbose_name_plural = '培养箱硬件'


class Incplantdetail(models.Model):
    dayavertemp = models.CharField(db_column='dayAvertemp',max_length=45, null=True)
    dayaverhum = models.CharField(db_column='dayAverhum',max_length=45, null=True)
    dayaverpress = models.CharField(db_column='dayAverpress',max_length=45, null=True)
    dayaverlight = models.CharField(db_column='dayAverlight',max_length=45, null=True)
    incplantdetaildate = models.DateField(db_column='incplantdetailDate',auto_now=True)
    incubator_incuno = models.ForeignKey(Incubator, models.DO_NOTHING, db_column='Incubator_IncuNo', blank=True, null=True)
    Plant_plantname = models.ForeignKey(Plant, models.DO_NOTHING, db_column='plant_plantname', blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'Incplantdetail'
        verbose_name_plural = '植物详情'


class Selldetail(models.Model):
    sdid = models.CharField(db_column='sdID', primary_key=True,max_length=45)
    sddate = models.DateField(db_column='sdDate', auto_now=True)
    mostsellperson = models.CharField(db_column='mostsellPerson',max_length=45,null=True)
    mostsellInc = models.CharField(db_column='mostsellInc',max_length=45,null=True)
    mostsellarea = models.CharField(db_column='mostsellarea',max_length=45,null=True)


    class Meta:
        managed = True
        db_table = 'selldetail'
        verbose_name_plural = '销售单'


class SellManger(models.Model):
    areaname = models.CharField(db_column='areaName',max_length=45, null=True)
    managername = models.CharField(db_column='managerName', max_length=45, null=True)


    class Meta:
        managed = True
        db_table = 'sellmanager'
        verbose_name_plural = '？'


class Fixinfo(models.Model):
    fixinfoid = models.CharField(db_column='fixinfoID',max_length=45, primary_key=True)
    incubator_incuno = models.ForeignKey(Incubator, models.DO_NOTHING, db_column='Incubator_IncuNo', blank=True,null=True)
    user_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='User_userId', blank=True, null=True)
    ifover = models.IntegerField(db_column='ifOver',null=True)
    fixmanager = models.CharField(db_column='fixManager',max_length=45,null=True)
    fixputdate = models.DateField(db_column='fixputDate', auto_now=True)


    class Meta:
        managed =True
        db_table = 'fixinfo'
        verbose_name_plural = '修改环境'