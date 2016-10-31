from django.conf.urls import url
from django.contrib import admin
from login import views
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^index/', TemplateView.as_view(template_name='index.html')),
    url(r'^test/', TemplateView.as_view(template_name='test.html')),
    url(r'^about/', TemplateView.as_view(template_name='about.html')),
    url(r'^cursus/', TemplateView.as_view(template_name='cursus.html')),
    url(r'^login/', TemplateView.as_view(template_name='login.html')),
    url(r'^register/', TemplateView.as_view(template_name='register.html')),
    url(r'^admin/', admin.site.urls),
]
