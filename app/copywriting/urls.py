from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'copywriting'
urlpatterns = [
    url(r'^$', login_required(views.LandingPageListView.as_view()), name='index'),
]
