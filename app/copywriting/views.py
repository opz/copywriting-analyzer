from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import LandingPage

@login_required
def index(request):
    landingpages = LandingPage.objects.filter(user=request.user)

    context = {
        'landingpages': landingpages
    }

    return render(request, 'copywriting/index.html', context)
