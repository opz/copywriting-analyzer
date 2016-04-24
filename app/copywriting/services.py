from __future__ import unicode_literals

from lxml import html
import requests

from textstat.textstat import textstat

from .models import LandingPage

def analyze_landingpage(id):
    landingpage = LandingPage.objects.get(id=id)

    page = requests.get(landingpage.url)
    tree = html.fromstring(page.content)

    landingpage.title = tree.xpath('//head/title/text()')[0]
    landingpage.content = tree.xpath('//body')[0].text_content()

    landingpage.flesch_reading_ease = textstat.flesch_reading_ease(landingpage.content)
    landingpage.flesch_kincaid_grade = textstat.flesch_kincaid_grade(landingpage.content)
    landingpage.gunning_fog = textstat.gunning_fog(landingpage.content)
    landingpage.smog_index = textstat.smog_index(landingpage.content)
    landingpage.automated_readability_index = textstat.automated_readability_index(landingpage.content)
    landingpage.coleman_liau_index = textstat.coleman_liau_index(landingpage.content)
    landingpage.linsear_write_formula = textstat.linsear_write_formula(landingpage.content)
    landingpage.dale_chall_readability_score = textstat.dale_chall_readability_score(landingpage.content)

    landingpage.save()
