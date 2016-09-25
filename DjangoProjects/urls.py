from django.conf.urls import url
from django.contrib import admin
from MonkeyBusiness import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^admin/', admin.site.urls),
]
