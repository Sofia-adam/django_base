"""
URL configuration for sat18 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from satapp1 import views 
from satapp2 import views as v
from satapp3 import views as w

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/',views.a),
    path('b/',views.b),
    path('c/',views.c),
    path('d/',views.d),
    path('e/',v.time),
    path('f/',w.dmy)
]
