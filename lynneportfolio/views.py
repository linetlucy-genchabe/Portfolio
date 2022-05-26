from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Project,Skills

# Create your views here.
def index(request):
    return render(request,'index.html')

def project(request):
    try:
        project = Project.objects.all()
    except Project.DoesNotExist:
        raise Http404()
    return render(request,"project.html", {"project":project})

def skills(request):
    try:
        skills = Skills.objects.all()
    except Skills.DoesNotExist:
        raise Http404()
    return render(request,"skills.html", {"skills":skills})


