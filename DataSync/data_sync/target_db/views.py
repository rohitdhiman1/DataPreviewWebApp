from django.shortcuts import render,get_object_or_404

from .models import TargetDatabase

def detail_t(request , id):
    target_db_detail = get_object_or_404(TargetDatabase, pk=id)
    return render(request, "target_db/detail.html", {"target_db_detail": target_db_detail})
