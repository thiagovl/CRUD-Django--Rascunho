"""notifire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from core.views import delete, index, list, list_id, inserir, update, vcriar, vupdate, vdelete, filter, vfilter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('list/', list),
    path('list_id/<id>/', list_id),
    path('vcriar/', vcriar),
    path('criar/submit', inserir),
    path('vupdate/<id>/', vupdate),
    path('update/submit/<id>', update),
    path('vdelete/<id>/', vdelete),
    path('delete/submit/<id>/', delete),
    path('vfilter/', vfilter),
    path('filter/submit', filter),
]
