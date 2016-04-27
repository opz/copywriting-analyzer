from django.views.generic.list import ListView

from .models import LandingPage

class LandingPageListView(ListView):
    """
    Display :model:`copywriting.LandingPage` analysis for logged in
    :model:`auth.User`.

    **Context**

    ``landingpages``
        Array of :model:`copywriting.LandingPage` instances.

    **Template**

    :template:`copywriting/landingpage_list.html`
    """

    context_object_name = 'landingpages'

    def get_queryset(self):
        """
        Return :model:`copywriting.LandingPage` instances for
        :model:`auth.User`.
        """
        return LandingPage.objects.filter(user=self.request.user)
