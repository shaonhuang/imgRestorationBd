from django.http.response import Http404
from filesSys.models import File
import os
import json
from django.shortcuts import render
from django.http import HttpResponse
import datetime


# 存放地址
orpath = "../imgRestorationBd/files/or"
or_vpath = "../imgRestorationBd/files/or_v"
hrpath = "../imgRestorationBd/files/hr"
hr_vpath = "../imgRestorationBd/files/hr_v"
lrpath = "../imgRestorationBd/files/lr"
lr_vpath = "../imgRestorationBd/files/lr_v"

imgpath = './files/or'
# Create your views here.

# dependency


def UtcNow():
    now = datetime.datetime.utcnow()
    return now


def upload(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile = request.FILES.get("file", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")

        # currentDir = os.path.dirname(os.path.abspath(__file__))
        # fileDir = os.path.join(currentDir, "\\files")
        # 判断文件类型，归类存放文件地址
        filename = myFile.name
        destination = ""
        if(filename.endswith("png") or filename.endswith("jpg") or filename.endswith("jpeg")):
            destination = open(os.path.join(imgpath, filename),
                               'wb+')    # 打开特定的文件进行二进制的写操作
        elif(filename.endswith("mp4") or filename.endswith("mkv")):
            destination = open(os.path.join(videopath, filename), 'wb+')
        else:
            return HttpResponse("Not supported file type!")

        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()

        # 在collection中添加新数据
        file = File()
        file.f_name = filename
        file.f_status = 'processing'
        file.f_type = filename.split('.')[-1]
        file.f_upload_date = UtcNow()
        file.save()

        return HttpResponse("添加成功！")


def test(response):
    return HttpResponse("Ok!")

# 获取所有文件id


def getFileList(request):
    if(request.method == "GET"):
        files = File.objects.all()
        numbers = []
        for file in files:
            numbers.append(file.id)

    return HttpResponse(json.dumps(numbers))


# 所有字段
fieldnames = ['id', 'filename', 'type', 'status', 'upload_date']


def getInfo(request, id):
    if(request.method == "GET"):
        file = File.objects.get(id=id)
        # if(file.id != id):
        #     return Http404
        # else:
        id = file.id
        filename = file.f_name
        filetype = file.f_type
        status = file.f_status
        update_time = file.f_upload_date
        vals = [id, filename, filetype, status, update_time]
        fileDict = {}
        for index in range(len(fieldnames)):
            fileDict[fieldnames[index]] = str(vals[index])
        return HttpResponse(json.dumps(fileDict))

# 获得文件


def getFileById(request, type, id):
    if(request.method == "GET"):
        file = File.objects.get(id=id)
        if(type == "or"):
            filepath = os.path.join(orpath, file.f_name)
            with open(filepath, 'rb') as f:
                image_data = f.read()
            return HttpResponse(image_data, content_type='image/jpg')
        elif(type == "or_v"):
            filepath = os.path.join(or_vpath, file.f_name)
            with open(filepath, 'rb') as f:
                video_data = f.read()
            return HttpResponse(video_data, content_type='video/mp4')


def getFileByName(request, name):
    if(request.method == "GET"):
        file = File.objects.get(f_name=name)
        filepath = os.path.join(orpath, file.f_name)
        with open(filepath, 'rb') as f:
            image_data = f.read()
        return HttpResponse(image_data, content_type='image/jpg')


def deleteById(request, id):
    try:
        if(request.method == "GET"):
            File.objects.get(id=id).delete()
            name = File.objects.get(id=id).f_name
            os.system('rm -f files/or/' + name)
            return HttpResponse('deleted ' + name)
        else:
            return HttpResponse('methods error')
    except:
        return HttpResponse('deleting ' + str(id) + ' fail')


def deleteByName(request, name):
    try:
        if(request.method == "GET"):
            File.objects.get(f_name=name).delete()
            os.system('rm -f files/or/'+name)
            return HttpResponse('deleted ' + name)
        else:
            return HttpResponse('methods error')
    except:
        return HttpResponse('deleting ' + name + ' fail')
