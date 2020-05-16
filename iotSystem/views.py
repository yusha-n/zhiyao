#coding:utf-8
import functools
import time
from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse,HttpResponseRedirect
from .models import Data,Warning,SaveWarning,Environment,DataWarning,SaveDataWarning,Incubator,Control
import datetime
import json
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
#from WEB.WEB.settings import EMAIL_FROM
from zhiyao.settings import EMAIL_FROM

from django.core.mail import send_mail

def templatemytest(request):
    if request.user.is_authenticated:
        pass
    else:
        return render(request, "login.html", {"msg": u"无权查看"})

def is_valid_control_data(type, val):
    if type == 'hl':
        pass
    elif type == 'ha':
        pass
    elif type == 'ta':
        pass
    elif type == 'tl':
        pass
    elif type == 'ps':
        pass
    elif type == 'il':
        pass
    return True
def control(request, iden):
    if request.user.is_authenticated:
        incu = Incubator.objects.filter(iden=iden)
        if incu:
            incu = incu[0]
            if incu.stat == 'connected':
                if request.method == 'POST':
                    my_data = []
                    my_type = ['hl', 'ha', 'tl', 'ta', 'pr', 'il']
                    for i in range(len(my_type)):
                        my_data.append(request.POST.get(my_type[i], None))
                    # hl = request.POST.get('hl', None)
                    # ha = request.POST.get('ha', None)
                    # tl = request.POST.get('tl', None)
                    # ta = request.POST.get('ta', None)
                    # ps = request.POST.get('ps', None)
                    # il = request.POST.get('il', None)

                    if all(list(map(is_valid_control_data, my_type, my_data))):
                        ctl = Control(incubator_iden = iden)
                        ind = 0
                        ctl.humi_land = my_data[ind]; ind += 1
                        ctl.humi_area = my_data[ind]; ind += 1
                        ctl.temp_land = my_data[ind]; ind += 1
                        ctl.temp_area = my_data[ind]; ind += 1
                        ctl.pres = my_data[ind]; ind += 1
                        ctl.illu = my_data[ind]; ind += 1
                        ctl.time = datetime.datetime.now()
                        print("ctl:2")
                        print(my_data)
                        print(ctl.incubator_iden, ctl.humi_area, ctl.temp_area,ctl.humi_land, ctl.temp_land, ctl.pres, ctl.illu)
                        ctl.save()
                        return HttpResponseRedirect(reverse('iotSystem:dev-detail', kwargs={'iden':iden}))

                    else:
                        return render(request, 'iotSystem/dev_detail.html', {"msg": "格式错误"})
                else:
                    return render(request, 'iotSystem/dev_detail.html', {"msg": None})
            elif incu.stat == 'disconnected':
                #培养箱未注册
                return HttpResponseRedirect(reverse('iotSystem:dev-list',))
            else:
                #故障
                return HttpResponseRedirect(reverse('iotSystem:dev-list',))
        else:
            #编号错误
            return HttpResponseRedirect(reverse('iotSystem:dev-list', ))
    else:
        return render(request, "login.html", {"msg": u"无权查看"})


def dev_detail(request, iden):
    if request.user.is_authenticated:
        incu = Incubator.objects.filter(iden=iden)
        if incu:
            incu = incu[0]
            if incu.stat == 'connected':
                data_list = Environment.objects.filter(incubator_iden= iden).order_by("-time").values("time", "humi_land", "humi_area", "temp_land", "temp_area", "illu", "pres")[:30]
                data_list = list(data_list)
                for data in data_list:
                    data['time'] = data['time'].strftime("%Y/%m/%d %H:%M:%S")
                key_dict = [{'时间': 'time'},{'土壤湿度':'humi_land'},{'空气湿度':'humi_area'},{'土壤温度':'temp_land'},{'空气温度':'temp_area'},{'光照':'illu'},{'压强':'pres'}]
                env_list = []
                for i, data in enumerate(data_list):
                    env_list.append([ {key : data[val]} for d in key_dict for key,val in d.items() ])
                control_list = Control.objects.filter(incubator_iden= iden).order_by("-time").values("time", "humi_land", "humi_area", "temp_land", "temp_area", "illu", "pres")[:30]
                control_list = list(control_list)
                ctl_list = []
                for i, data in enumerate(control_list):
                    ctl_list.append([ {key : data[val]} for d in key_dict for key,val in d.items() ])
                return render(request, 'iotSystem/dev_detail.html', {'env_list': env_list, 'data_list':data_list, 'ctl_list': ctl_list, 'box':incu, })

            elif incu.stat == 'disconnected':
                #培养箱未注册
                return HttpResponseRedirect(reverse('iotSystem:dev-list',))
            else:
                #故障
                return HttpResponseRedirect(reverse('iotSystem:dev-list',))
        else:
            #编号错误
            return HttpResponseRedirect(reverse('iotSystem:dev-list', ))
    else:
        return render(request, "login.html", {"msg": u"无权查看"})


def dev_list(request):
    if request.user.is_authenticated:
        list_box = []
        user = (request.user.userprofile.phon, request.user.username)
        print(1, user)
        list_incu = Incubator.objects.all()
        print(list_incu[0].user_phon)
        list_incu = Incubator.objects.filter(user_phon=user[0])
        for incu in list_incu:
            box = dict()
            box["phon"] = incu.user_phon
            box["iden"] = incu.iden
            box["stat"] = incu.stat
            box["time"] = incu.time
            box["key"] = incu.key
            box["username"] = user[1]
            list_box.append(box)
        return render(request, "iotSystem/dev_list.html", {"box_list": list_box})
    else:
        return render(request, "login.html", {"msg": u"无权查看"})

def connect(request ):
    if request.user.is_authenticated:
        #处理POST请求
        if request.method == 'POST':
            #request.POST.get("key", "default_value") 从POST字典里取出关键字对应的值，关键字不存在时返回默认值；
            id_incubator = request.POST.get('id_incubator', 'none')
            key = request.POST.get('key', 'none')
            list_incu = Incubator.objects.filter(pk=id_incubator)
            if list_incu:
                incu = list_incu[0]
                if incu.stat == "connected":
                    return render(request, "iotSystem/connect.html", {"msg": u'编号已占用'})
                if key == incu.key:
                    #通过一对一键访问userprofile表，取得电话号码
                    incu.user_phon = request.user.userprofile.phon
                    incu.stat = 'connected'
                    incu.time = datetime.datetime.now()
                    incu.save()
                    return HttpResponseRedirect(reverse('iotSystem:dev-list',))
                    #return redirect('iotSystem/dev_list.html',)
                else:
                    return render(request, "iotSystem/connect.html", {"msg": u"密钥错误"})
            else:
                return render(request, "iotSystem/connect.html", {"msg": u"培养箱编号错误"})
        else:
            return render(request, "iotSystem/connect.html", {"msg": None})
    else:
        return render(request, "iotSystem/login.html", {"msg": u"无权查看"})

# def data_dis(request):
#     if request.user.is_authenticated:
#         datas = Data.objects.order_by("-time").values("time","humi","temp","pres")[:30]
#         datas=list(datas)
#         for data in datas:
#              data["time"]=data["time"].strftime("%Y/%m/%d %H:%M:%S")
#         datas=json.dumps(datas[::1])
#         return render(request, "index_v1.html", {"data_list": datas})
#     else:
#         return render(request,"index_v1.html",{"msg":u"无权查看"})
def data_dis(request):
    datas = Environment.objects.order_by("-time").values("time","humi_land","humi_area","temp_land","temp_area","illu","pres")[:30]
    #print(datas)
    datas=list(datas)
    for data in datas:
        data["time"]=data["time"].strftime("%Y/%m/%d %H:%M:%S")
    datas=json.dumps(datas[::1])
    #print("yougood")
    # return render(request, "iotSystem/new_index_v3.html",{"data_list":datas})
    return render(request, "iotSystem/new_index_v1.html", {"data_list": datas})

# def index(request):
#     if request.user.is_authenticated:
#         return render(request,"index.html",{"msg":u"成功进入"})
#     else:
#         return render(request,"login.html",{"msg":u"无权查看"})
#
def index(request):
    if request.user.is_authenticated:
        datas = Environment.objects.order_by("-time").values("time","humi_land","humi_area","temp_land","temp_area","illu","pres")[:30]
        # print(datas)
        datas = list(datas)
        for data in datas:
            data["time"] = data["time"].strftime("%Y/%m/%d %H:%M:%S")
        datas = json.dumps(datas[::1])
        # print("yougood")
        return render(request, "iotSystem/index.html", {"msg": u"成功进入", "data_list": datas})
    else:
        return render(request, "iotSystem/login.html", {"msg": u"无权查看"})


def data_in(request):
    if request.method == "GET":
        temp_land=request.GET.get("temp_land", "50")
        temp_area = request.GET.get("temp_area", "50")
        humi_land=request.GET.get("humi_land", "120")
        humi_area = request.GET.get("humi_area", "120")
        pres= request.GET.get("pres", "320")
        illu = request.GET.get("illu", "30")
        data=Environment(temp_land=temp_land, temp_area=temp_area,humi_land=humi_land,humi_area = humi_area,pres=pres,illu=illu)
        data.save()
        return HttpResponse("OK")


#ajax请求新的气体数据
time1=""
average=[]
value=0
timesend=0
def ajax_data(request):
    global time1, average, value, timesend
    data = Environment.objects.order_by("-time").values("time","humi_land","humi_area","temp_land","temp_area","illu","pres")[0]
    #是不是最新的记录
    if time1 != data["time"]:
        time1 = data["time"]
        if len(average) == 5:
            #取5个记录计算平均值，如果超过警告线就发送邮件
            warning = DataWarning.objects.get(level="primary")
            msgContent = warning.messageContent
            mailtitle = warning.mailtitle
            interval = warning.interval
            valueWarning = warning.value
            value = functools.reduce(lambda x, y: x + y, map(int, average)) / len(average)
            if int(time.time()) >= timesend + int(interval) * 60:
                if value >= int(valueWarning):
                    # send message and save warnring msg
                    timesend = int(time.time())
                    send_mail(mailtitle, msgContent, EMAIL_FROM, ["1843115916@qq.com"])
                    SaveDataWarning.objects.create(warning=warning, currentvalue=value)
                average = []
        else:
            #不到五个记录时继续添加
            average.append(data["temp_land"])
    data["time"] = data["time"].strftime("%Y/%m/%d %H:%M:%S")
   # resp={"ch1":q1.value,"time1":q1.time.strftime("%Y/%m/%d %H:%M:%S"),"ch2":q2.value,"time2":q2.time.strftime("%Y/%m/%d %H:%M:%S")}
   # resp = {"temp": data.temp,"humi":data.humi,"ch4":data.ch4, "time": data.time.strftime("%Y/%m/%d %H:%M:%S")}
    return HttpResponse(json.dumps(data),content_type="application/json")

#查询历史数据
def data_history(request):
    datas=Environment.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(datas, 8, request=request)
    data=p.page(page)
    return render(request,"iotSystem/new_index_v2.html",{"data":data})


def position(request):
    return render(request,"iotSystem/position.html")
def historyDataFilter(request):
    if request.method=="GET":
        #返回最近的100条数据
        datas = Environment.objects.order_by("-time").values("time","humi_land","humi_area","temp_land","temp_area","illu","pres")[:100]
        datas = list(datas)
        for data in datas:
            data["time"] = data["time"].strftime("%Y/%m/%d %H:%M:%S")
        datas = json.dumps(datas[::1])
        return render(request, "iotSystem/new_historyDataFilter.html", {"data_list": datas})
    else:
        start=request.POST.get("start","no")
        end=request.POST.get("end","no")
        time=request.POST.get("time","no")
        start=datetime.datetime.strptime(start,"%Y/%m/%d %H:%M:%S")
        end= datetime.datetime.strptime(end,"%Y/%m/%d %H:%M:%S")
        datas=Environment.objects.values("time","humi_land","temp_land","humi_area","temp_area","pres","illu").filter(time__range=(start,end))
        for data in datas:
            data["time"] = data["time"].strftime("%Y/%m/%d %H:%M:%S")
        datas = json.dumps(datas[::1])
        return render(request,"iotSystem/new_historyDataFilter.html",{"data_list": datas})

    #return render(request,"historyDataFilter.html")
def control_old(request):
    return render(request,"iotSystem/new_control.html")

def introduce(request):
    return render(request,"iotSystem/new_introduce.html")
def background(request):
    return render(request,"iotSystem/background.html")

def warningHistory(request):
    datas=SaveDataWarning.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(datas, 8, request=request)
    data = p.page(page)
    return render(request, "iotSystem/new_warning.html", {"data": data})