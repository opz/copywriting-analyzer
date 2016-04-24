from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import LandingPage

@login_required
def index(request):
    landingpages = LandingPage.objects.all()

    context = {
        'landingpages': landingpages
    }

    return render(request, 'copywriting/index.html', context)
