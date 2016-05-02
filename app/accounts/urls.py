from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as auth_views

from forms import BootstrapAuthenticationForm

app_name = 'accounts'
urlpatterns = [
    url(r'^login/$', auth_views.login, {
        'authentication_form': BootstrapAuthenticationForm,
        'extra_context': {
            'next': reverse_lazy('copywriting:index')}
    }, 'login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
