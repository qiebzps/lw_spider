"""lw_spider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from mainsite.views import homepage,showbook,showchapter
from django.conf.urls import include,url

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('homepage/',homepage),
#]

urlpatterns = [
    url(r'^$',homepage),
    url(r'^book/(\w+)$',showbook),
    # 两个参数，一个book_id,一个chapter_id
    # book/0/0001
    url(r'^book/(\w+)/(\w+)$',showchapter),
    url(r'admin/', admin.site.urls),
]

