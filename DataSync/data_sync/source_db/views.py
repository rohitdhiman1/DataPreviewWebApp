from django.shortcuts import render,get_object_or_404, redirect
from django.forms import modelform_factory
import json
from .models import SourceDatabase

def detail_s(request , id):
    source_db_detail = get_object_or_404(SourceDatabase, pk =id)
    return render(request, "source_db/detail_s.html", {"source_db_detail": source_db_detail})

def source_databases_list(request):
    return render(request, "source_db/source_databases.html", {"src_db": SourceDatabase.objects.all()})


Src_DB = modelform_factory(SourceDatabase, exclude=[])


def new(request):
    if request.method == "POST":
        form = Src_DB(request.POST)
        if form.is_valid():
            form.save()
            #with open('data.txt', 'w') as outfile:
            #    json.dump(form.cleaned_data, outfile)
            return redirect("welcome")

    else:
        form = Src_DB()
    return render(request, "source_db/new.html", {"form": form})