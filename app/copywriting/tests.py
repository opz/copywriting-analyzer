from __future__ import unicode_literals

from decimal import Decimal

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from .models import LandingPage

class AuthenticatedTestMixin(object):
    """
    Mixin for setting up a :class:`test.TestCase` with an authenticated
    test :model:`auth.User`.
    """

    def setUp(self):
        """
        Create a test :model:`auth.User` and authenticate with
        :func:`auth.UserManager.create_user`.
        """
        self.user = User.objects.create_user('test', password='password')

        login = self.client.login(username='test', password='password')

        self.assertTrue(login)

class LandingPageTests(AuthenticatedTestMixin, TestCase):
    """
    Test all :model:`copywriting.LandingPage` features.
    """

    def test_analyze_landingpage(self):
        """
        Test :func:`copywriting.analyze_landingpage` function for successful
        web scraping and correct readability analysis.
        """
        landingpage = LandingPage(
            url                          = 'http://willshahda.com',
            user                         = self.user,
            flesch_reading_ease          = Decimal('40.34'),
            flesch_kincaid_grade         = Decimal('11.10'),
            gunning_fog                  = Decimal('7.60'),
            smog_index                   = Decimal('8.80'),
            automated_readability_index  = Decimal('18.10'),
            coleman_liau_index           = Decimal('21.57'),
            linsear_write_formula        = Decimal('7.00'),
            dale_chall_readability_score = Decimal('9.77')
        )

        test_landingpage = LandingPage(
            url  = 'http://willshahda.com',
            user = self.user,
        )

        test_landingpage.analyze()

        self.assertEqual(landingpage, test_landingpage)

class LandingPageListViewTests(AuthenticatedTestMixin, TestCase):
    """
    Test :view:`copywriting.LandingPageListView`.
    """

    def test_list_view_with_no_landingpages(self):
        """
        If no :model:`copywriting.LandingPage` instances exist for current
        :model:`auth.User`, an error message should display.
        """
        response = self.client.get(reverse('copywriting:index'))

        message = 'No landing pages available for analysis.'
        self.assertContains(response, message, status_code=200)
        self.assertQuerysetEqual(response.context['landingpages'], [])

    def test_list_view_with_one_landingpage(self):
        """
        If :model:`copywriting.LandingPage` instances exist for current
        :model:`auth.User`, they should all display.
        """
        url = 'http://willshahda.com'
        landingpage = LandingPage(url=url, user=self.user)
        landingpage. analyze()

        landingpage.save()

        response = self.client.get(reverse('copywriting:index'))

        self.assertQuerysetEqual(response.context['landingpages'], ['<LandingPage: %s>' % url])

class LandingPageAPIViewTests(AuthenticatedTestMixin, APITestCase):
    """
    Test :view:`copywriting.LandingPageAPIView`.

    Subclasses :class:`test.APITestCase` so the :class:`test.APIClient` can be
    used in place of :class:`test.Client`.
    """

    def test_post_request(self):
        """
        If a ``POST`` request is made to the ``copywriting`` API, a new
        :model:`copywriting.LandingPage` instance should be created.
        """
        data = {'url': 'http://willshahda.com'}
        response = self.client.post('/copywriting/api/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(LandingPage.objects.count(), 1)
        self.assertEqual(LandingPage.objects.get().url, data['url'])
