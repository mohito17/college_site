from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
