from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from rest_framework.routers import DefaultRouter

from .views import LandingPageListView, LandingPageAPIViewSet

router = DefaultRouter()
router.register(r'landingpages', LandingPageAPIViewSet)

app_name = 'copywriting'
urlpatterns = [
    url(r'^$', login_required(LandingPageListView.as_view()), name='index'),
    url(r'^', include(router.urls)),
]
