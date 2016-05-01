from django.views.generic.list import ListView

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import LandingPage
from .serializers import LandingPageSerializer

class LandingPageListView(ListView):
    """
    Display :model:`copywriting.LandingPage` analysis for logged in
    :model:`auth.User` with :class:`copywriting.LandingPageForm` for performing
    additional analysis.

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
        return LandingPage.objects.filter(user=self.request.user).order_by('-date')

    def get_context_data(self, **kwargs):
        """
        Add :class:`copywriting.LandingPageForm` instance to context.
        """
        context = super(LandingPageListView, self).get_context_data(**kwargs)

        context['serializer'] = LandingPageSerializer()

        return context

class LandingPageAPIView(ListCreateAPIView):
    """
    Handles all CRUD operations for :model:`LandingPage` instances.
    """

    queryset           = LandingPage.objects.all()
    serializer_class   = LandingPageSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """
        Associate new :model:`LandingPage` instance with current
        :model:`auth.User` and analyze before saving.
        """
        landingpage = serializer.save(user=self.request.user)
        landingpage.analyze()
        landingpage.save()
