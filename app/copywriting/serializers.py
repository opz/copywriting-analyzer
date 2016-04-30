from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from rest_framework.serializers import ModelSerializer

from .models import LandingPage

class LandingPageSerializer(ModelSerializer):
    """
    Serialization for :model:`LandingPage` instances used with the REST API.
    """

    def __init__(self, *args, **kwargs):
        """
        Dynamically set the ``url`` ``placeholder`` attribute to the
        assigned ``label``.
        """
        super(LandingPageSerializer, self).__init__(*args, **kwargs)
        self.fields['url'].style['placeholder'] = self.fields['url'].label

    class Meta:
        model = LandingPage
        fields = '__all__'
        read_only_fields = (
            'user',
            'date',
            'title',
            'content',
            'flesch_reading_ease',
            'flesch_kincaid_grade',
            'gunning_fog',
            'smog_index',
            'automated_readability_index',
            'coleman_liau_index',
            'linsear_write_formula',
            'dale_chall_readability_score',
        )
        extra_kwargs = {'url': {'label': _('URL')}}
