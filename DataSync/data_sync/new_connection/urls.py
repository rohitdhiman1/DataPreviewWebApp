from django.urls import path

from . import views


urlpatterns = [
    path('details', views.new_connection_list, name="new_connection"),
    path('new', views.new, name="new"),
    path('metadata_info', views.metadata_info, name="metadata_info"),
    path('sample_data', views.sample_data, name="sample_data"),
]