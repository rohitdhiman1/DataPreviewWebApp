"""data_sync URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from website.views import welcome,date,about
#from source_db.views import detail_s,source_databases_list
from target_db.views import detail_t

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',welcome,name = 'welcome'),
    path('date',date),
    path('about',about),
    path('target_db/', include('target_db.urls')),
    path('source_db/', include('source_db.urls')),
    path('new_connection/', include('new_connection.urls')),
]
