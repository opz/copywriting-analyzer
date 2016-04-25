from django.conf.urls import url

from . import views

app_name = 'copywriting'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^landingpage/$', views.index, name='landingpage'),
]
