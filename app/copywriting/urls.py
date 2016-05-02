from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import LandingPageListView, LandingPageAPIViewSet

landingpage_list = LandingPageAPIViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

landingpage_detail = LandingPageAPIViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

app_name = 'copywriting'
urlpatterns = [
    url(r'^$', login_required(LandingPageListView.as_view()), name='index'),
    url(r'^api/$', landingpage_list, name='landingpage-list'),
    url(r'^api/(?P<pk>[0-9]+)/$', landingpage_detail, name='landingpage-detail'),
]
