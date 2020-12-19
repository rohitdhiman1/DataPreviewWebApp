from django.urls import path

from . import views


urlpatterns = [
    path('<int:id>', views.detail_s, name="detail_source"),
    path('src_db', views.source_databases_list, name="src_db"),
    path('new', views.new, name="new"),
]