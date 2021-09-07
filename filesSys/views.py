from django.http.response import Http404
from filesSys.models import File
import os
import json
from django.shortcuts import render
from django.http import HttpResponse


# 存放地址
orpath = "D:\\Pisces65\\Project\\imgRestorationBd\\files\\or"
or_vpath = "D:\\Pisces65\\Project\\imgRestorationBd\\files\\or_v"
hrpath = "D:\\Pisces65\\Project\\imgRestorationBd\\files\\hr"
hr_vpath = "D:\\Pisces65\\Project\\imgRestorationBd\\files\\hr_v"
lrpath = "D:\\Pisces65\\Project\\imgRestorationBd\\files\\lr"
lr_vpath = "D:\\Pisces65\\Project\\imgRestorationBd\\files\\lr_v"
# Create your views here.
def upload(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None  
        if not myFile:  
            return HttpResponse("no files for upload!")

        # currentDir = os.path.dirname(os.path.abspath(__file__))
        # fileDir = os.path.join(currentDir, "\\files")
        # 判断文件类型，归类存放文件地址
        filename = myFile.name
        destination = ""
        if(filename.endswith("png") or filename.endswith("jpg")):
            destination = open(os.path.join(imgpath,filename),'wb+')    # 打开特定的文件进行二进制的写操作  
        elif(filename.endswith("mp4") or filename.endswith("mkv")):
            destination = open(os.path.join(videopath,filename),'wb+')
        else:
            return HttpResponse("Not supported file type!")

        for chunk in myFile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close() 


        # 在collection中添加新数据 
        file = File()
        file.f_filename = filename
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
fieldnames = ['id', 'filename', 'upload_date']
def getInfo(request, id):
    if(request.method == "GET"):
        file = File.objects.get(id=id)
        # if(file.id != id):
        #     return Http404
        # else:
        id = file.id
        filename = file.f_filename
        update_time = file.f_upload_date
        vals = [id, filename, update_time]
        fileDict = {}
        for index in range(len(fieldnames)):
            fileDict[fieldnames[index]] = str(vals[index])
        return HttpResponse(json.dumps(fileDict))

# 获得文件
def getFile(request, type, id):
    if(request.method == "GET"):
        file = File.objects.get(id=id)
        if(type == "or"):
            filepath = os.path.join(orpath,file.f_filename)
            with open(filepath, 'rb') as f:
                image_data = f.read()
            return HttpResponse(image_data, content_type='image/jpg')
        elif(type == "or_v"):
            filepath = os.path.join(or_vpath,file.f_filename)
            with open(filepath, 'rb') as f:
                video_data = f.read()
            return HttpResponse(video_data, content_type='video/mp4')