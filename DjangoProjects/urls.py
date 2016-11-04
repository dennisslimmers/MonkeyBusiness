from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from login.forms import LoginForm
from django.contrib.auth import views as authviews
from django.core.urlresolvers import reverse
from login import views as loginviews

urlpatterns = [
    url(r'^index/', TemplateView.as_view(template_name='index.html')),
    url(r'^test/', TemplateView.as_view(template_name='test.html')),
    url(r'^about/', TemplateView.as_view(template_name='about.html')),
    url(r'^cursus/', TemplateView.as_view(template_name='cursus.html')),
    url(r'^logintest/', TemplateView.as_view(template_name='login.html')),
    url(r'^register/', TemplateView.as_view(template_name='register.html')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('login.urls')),
    url(r'^login/$', authviews.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name="login"),
    url(r'registerSubmit/', loginviews.create, name="registerSubmit"),
]