from django.conf.urls import url
from django.contrib import admin
from MonkeyBusiness import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^index/', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', admin.site.urls),
]
