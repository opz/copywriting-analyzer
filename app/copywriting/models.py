from __future__ import unicode_literals

from lxml import html

import requests

from textstat.textstat import textstat

from decimal import Decimal

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator

@python_2_unicode_compatible
class LandingPage(models.Model):
    """
    Stores a single landing page analysis, related to :model:`auth.User`.
    """

    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    date    = models.DateTimeField(auto_now_add=True)
    title   = models.TextField(blank=True)
    url     = models.TextField(validators=[URLValidator()])
    content = models.TextField(blank=True)

    # Readability scores
    _decimal_field_args = {'null': True, 'max_digits': 5, 'decimal_places': 2}

    flesch_reading_ease          = models.DecimalField(**_decimal_field_args)
    flesch_kincaid_grade         = models.DecimalField(**_decimal_field_args)
    gunning_fog                  = models.DecimalField(**_decimal_field_args)
    smog_index                   = models.DecimalField(**_decimal_field_args)
    automated_readability_index  = models.DecimalField(**_decimal_field_args)
    coleman_liau_index           = models.DecimalField(**_decimal_field_args)
    linsear_write_formula        = models.DecimalField(**_decimal_field_args)
    dale_chall_readability_score = models.DecimalField(**_decimal_field_args)

    def analyze(self):
        """
        Scrape text content from :model:`copywriting.LandingPage` and calculate
        readability scores.
        """
        page = requests.get(self.url)
        tree = html.fromstring(page.content)

        self.title   = tree.xpath('//head/title/text()')[0]

        for el in tree.xpath('//script|//style'):
            el.drop_tree()

        self.content = tree.xpath('//body')[0].text_content()

        metrics = (
            'flesch_reading_ease',
            'flesch_kincaid_grade',
            'gunning_fog',
            'smog_index',
            'automated_readability_index',
            'coleman_liau_index',
            'linsear_write_formula',
            'dale_chall_readability_score',
        )

        for metric in metrics:
            value         = getattr(textstat, metric)(self.content)
            decimal_value = Decimal(value).quantize(Decimal('0.01'))

            setattr(self, metric, decimal_value)

    def __str__(self):
        return self.url

    def __eq__(self, other):
        """
        Compare :model:`copywriting.LandingPage` based on content and
        readability scores.
        """
        return self.url                           == other.url \
            and self.flesch_reading_ease          == other.flesch_reading_ease \
            and self.flesch_kincaid_grade         == other.flesch_kincaid_grade \
            and self.gunning_fog                  == other.gunning_fog \
            and self.smog_index                   == other.smog_index \
            and self.automated_readability_index  == other.automated_readability_index \
            and self.coleman_liau_index           == other.coleman_liau_index \
            and self.linsear_write_formula        == other.linsear_write_formula \
            and self.dale_chall_readability_score == other.dale_chall_readability_score
