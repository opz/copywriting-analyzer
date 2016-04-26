from django.test import TestCase

from .models import LandingPage
from .services import analyze_landingpage

class LandingPageTests(TestCase):
    fixtures = ['test_landingpage']

    def test_analyze_landingpage(self):
        landingpage = LandingPage.objects.get(id=1)

        analyze_landingpage(1)

        test_landingpage = LandingPage.objects.get(id=1)

        self.assertEqual(landingpage, test_landingpage)
