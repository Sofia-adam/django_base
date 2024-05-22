"""
URL configuration for mon20 project.

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
from django.urls import path,re_path
from work1 import views
from work2 import views as v
from work3 import views as v1
from work4 import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('w/',views.welcome),
    path('w2/',views.date),
    path('w3/',v.a),
    re_path('w33/',v.addition),
    path('w4/',v1.input),
    re_path('add/',v1.adds),
    path('w5/',v2.getin),
    path('w6/',v2.postin),
    re_path('ww',v2.additions)

]
