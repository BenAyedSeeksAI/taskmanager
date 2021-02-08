from django.conf.urls import url
from . import views
urlpatterns = [
    url('^About/$', views.About_website, name='About_website'),
    url('^$', views.main, name='main'),
]