from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.core.validators import URLValidator

@python_2_unicode_compatible
class LandingPage(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(blank=True)
    url = models.TextField(validators=[URLValidator()])
    content = models.TextField(blank=True)

    # Readability scores
    flesch_reading_ease = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    flesch_kincaid_grade = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    gunning_fog = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    smog_index = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    automated_readability_index = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    coleman_liau_index = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    linsear_write_formula = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    dale_chall_readability_score = models.DecimalField(null=True, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.url
