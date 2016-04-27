from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import LandingPage

@login_required
def index(request):
    """
    Display logged in user's :model:`copywriting.LandingPage` analysis.

    **Context**

    ``landingpages``
        Array of :model:`copywriting.LandingPage` instances.

    **Template**

    :template:`copywriting/index.html`
    """
    landingpages = LandingPage.objects.filter(user=request.user)

    context = {
        'landingpages': landingpages
    }

    return render(request, 'copywriting/index.html', context)
