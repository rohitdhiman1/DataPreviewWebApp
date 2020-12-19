from django.shortcuts import render
from django.http import HttpResponse
from _datetime import datetime

from source_db.models import SourceDatabase
from target_db.models import TargetDatabase

def welcome(request):
    return render(request, "website/welcome.html", {'source_databases': SourceDatabase.objects.all(),
                                                    'target_databases': TargetDatabase.objects.all()})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("Hi, I'm Rohit Dhiman. I'm an open source enthusiast.")