# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from mock import patch, Mock
import urllib2
from helpers import MessageGateway, get_comment
from models import Pub


class PubScrapyTest(TestCase):
    def setUp(self):
        self.res = open('guestpub/fixtures/daum_detailinfo_12026394.json').read()

    @patch('urllib2.urlopen')
    def test_get_comment(self, mock_urlopen):
        mock = Mock()
        mock.read.side_effect = [self.res]
        mock_urlopen.return_value = mock

        response = get_comment('12026394')
        self.assertEqual(response['homepage'], 'http://cafe.naver.com/jejusai', 'Homepage is different')
        self.assertEqual(len(response['comments']), 6)
        self.assertEqual(response['comments'][3]['time'], '2012-04-01')

class APITest(TestCase):
    fixtures = ['initial_data']

    def test_pub_list(self):
        c = Client()
        response = c.get('/api/pub/')
        self.assertTrue('13080037' in response.content)

    def test_pub_detail(self):
        c = Client()
        response = c.get('/api/pub/13080037/')
        self.assertTrue('13080037' in response.content)

    def test_pub_list_it_should_have_comment_number(self):
        c = Client()
        response = c.get('/api/pub/')
        self.assertTrue('comment_set' in response.content)

        

class ModelTest(TestCase):
    fixtures = ['initial_data']

    def test_get_comment_when_save(self):
        pub = Pub.objects.all()[0]
        pub._get_comment()
        self.assertEqual(Pub.objects.all().count(), 15, u'숙소의 개수가 15개 아님.')
