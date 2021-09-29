from django.shortcuts import render,redirect
from albumapp import models
from django.contrib.auth import authenticate
from django.contrib import auth
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

import albumapp

# Create your views here.
def index(request):
    albums=models.AlbumModel.objects.all().order_by('-id')
    totalalbum=len(albums)
    photos=[]
    lengths=[]
    for album in albums:
        photo=models.PhotoModel.objects.filter(palbum__atitle=album.atitle).order_by('-id')
        lengths.append(len(photo))
        if len(photo)==0:
            photos.append('')
        else:
            photos.append(photo[0].purl)
    return render(request,'index.html',locals())

def albumshow(request,albumid=None):
    album=albumid
    photos=models.PhotoModel.objects.filter(palbum__id=albumid).order_by('-id')
    monophoto=photos[0]
    totalphoto=len(photos)
    return render(request,'albumshow.html',locals())


