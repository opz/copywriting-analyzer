from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator

@python_2_unicode_compatible
class LandingPage(models.Model):
    """
    Stores a single landing page analysis, related to :model:`auth.User`.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date    = models.DateTimeField(auto_now_add=True)
    title   = models.TextField(blank=True)
    url     = models.TextField(validators=[URLValidator()])
    content = models.TextField(blank=True)

    # Readability scores
    flesch_reading_ease          = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    flesch_kincaid_grade         = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    gunning_fog                  = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    smog_index                   = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    automated_readability_index  = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    coleman_liau_index           = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    linsear_write_formula        = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    dale_chall_readability_score = models.DecimalField(null=True, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.url

    def __eq__(self, other):
        """
        Compare :model:`copywriting.LandingPage` based on content and
        readability scores.
        """
        return self.url == other.url \
            and self.content                      == other.content \
            and self.flesch_reading_ease          == other.flesch_reading_ease \
            and self.flesch_kincaid_grade         == other.flesch_kincaid_grade \
            and self.gunning_fog                  == other.gunning_fog \
            and self.smog_index                   == other.smog_index \
            and self.automated_readability_index  == other.automated_readability_index \
            and self.coleman_liau_index           == other.coleman_liau_index \
            and self.linsear_write_formula        == other.linsear_write_formula \
            and self.dale_chall_readability_score == other.dale_chall_readability_score
