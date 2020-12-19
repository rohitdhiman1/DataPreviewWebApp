from django.urls import path

from . import views


urlpatterns = [
    path('<int:id>', views.detail_t, name="detail_target"),
]