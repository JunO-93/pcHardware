"""web_project URL Configuration

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
from django.urls import path
from crawling.crawling_tasks import task_hello
from crawling.crawling_tasks import crawling_cpu
from crawling.crawling_tasks import crawling_gpu
from crawling.crawling_tasks import crawling_pcEst

task_hello(schedule= 60,repeat=60*2)
crawling_cpu(schedule=60, repeat=60*60*12)
crawling_gpu(schedule=60, repeat=60*60*12)
crawling_pcEst(schedule=60, repeat=60*60*6)

urlpatterns = [
    path('admin/', admin.site.urls),
]
