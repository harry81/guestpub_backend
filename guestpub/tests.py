# -*- coding: utf-8 -*-
from django.test import TestCase
from mock import patch, Mock
import urllib2
from helpers import MessageGateway, PubScrapy
from models import Pub


class PubScrapyTest(TestCase):
    def setUp(self):
        self.pubspider = PubScrapy()
        self.res = open('guestpub/fixtures/daum_detailinfo_12026394.json').read()

    @patch('urllib2.urlopen')
    def test_get_review(self, mock_urlopen):
        mock = Mock()
        mock.read.side_effect = [self.res]
        mock_urlopen.return_value = mock

        response = self.pubspider.get_review('13727191')
        self.assertEqual(response['homepage'], 'http://cafe.naver.com/jejusai', 'Homepage is different')
        self.assertEqual(len(response['comments']), 6)


class GuestpubModelTest(TestCase):
    fixtures = ['initial_data']

    def test_get_review(self):
        pub = Pub.objects.all()[0]
        pub.get_review()
        self.assertEqual(Pub.objects.all().count(), 15, u'숙소의 개수가 15개 아님.')
