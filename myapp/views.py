from urllib import parse

from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.shortcuts import render, redirect

from myapp import models

# Create your views here.
import random

from myapp.models import FileModel

def lifeispython(request):
    number = random.randint(1, 99)
    return render(request, 'myapp/lifeispython.html', {
        'numbervalue': number
    })


def uploadanywhere(request) :
    if len(request.FILES) > 0:
        print(request.FILES)
        file = request.FILES['uploaded_file']
        model = FileModel(
            key=randomkey(),
            file=file
        )

        model.save()
        print(model)
        return render(request, 'myapp/1_2keyshow.html', {
            'key': model.key
        })

    return render(request, 'myapp/1_1uploadanywhere.html')

def randomkey():
    key1 = random.randint(100000, 999999)
    while FileModel.objects.filter(key=key1).exists():
        key1 += 1

    return key1

def claimbutton(request):
    if len(request.POST)>0:

        print(request.POST)
        keybutton = request.POST['keybutton']
        # keybutton is an array but it acts like int. it's weird.
        keyvalue= int(keybutton)
        print(keyvalue)
        filemodels=FileModel.objects.filter(key=keyvalue)
        print (filemodels)
        if len(filemodels)>0:

            matchfile = filemodels[0].file

            fs = FileSystemStorage(matchfile.path)
            response = FileResponse(fs.open(matchfile.path, 'rb'),
                                    content_type='multipart/form-data;')
            response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'%s' % parse.quote(matchfile.name)
            return response
        else:
            return render(request,'myapp/2_1claimbutton.html',{
                "error": "There is no file, please submit it."
            })


    return render(request, 'myapp/2_1claimbutton.html')

def home(request):
    return render(request,'myapp/0_home.html')
