# -*- coding: utf-8 -*-
import json
from django.test import TestCase
from django.test import Client
from django.contrib.admin.options import (
    HORIZONTAL, VERTICAL, ModelAdmin, TabularInline,
)
from django.contrib.admin.sites import AdminSite
from mock import patch, Mock
import urllib2
from helpers import MessageGateway, get_comment
from models import Pub, Message


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

    def test_pub_list_it_should_respect_boundary(self):
        c = Client()
        response = c.get('/api/pub/?in_bbox=126.01831,32.682825,127.072998,34.052184')
        data = response.content
        output = json.loads(data)
        self.assertEqual(  len(output['results']), 15 )

        response = c.get('/api/pub/?in_bbox=126.499649,33.37794,126.763321,33.719579')
        data = response.content
        output = json.loads(data)
        self.assertEqual(  len(output['results']), 3 )
        

class ModelTest(TestCase):
    fixtures = ['initial_data']
    c = Client()

    def test_get_comment_when_save(self):
        pub = Pub.objects.all()[0]
        pub._get_comment()
        self.assertEqual(Pub.objects.all().count(), 15, u'숙소의 개수가 15개 아님.')

    def test_message_save(self):
        message = {
            'day':'2014-03-12',
            'num_men':'1',
            'num_women':'2',
            'num_children':'3',
            }
        response = self.c.post('/api/message', data=message)
        self.assertEqual(Message.objects.all().count(), 1)
        self.assertTrue(u'남' in Message.objects.all()[0].message)
        import ipdb; ipdb.set_trace()

        message = {
            'day':'2014-03-12',
            'num_women':'2',
            'num_children':'3',
            }
        response = self.c.post('/api/message', data=message)
        self.assertFalse(u'남' in Message.objects.all()[1].message, Message.objects.all()[1].message)
        self.assertEqual(Message.objects.all().count(), 2)

        message = {
            'day':'2014-03-12',
            'num_children':'3',
            }
        response = self.c.post('/api/message', data=message)
        self.assertFalse(u'여' in Message.objects.all()[2].message)
        self.assertEqual(Message.objects.all().count(), 3)

        message = {
            'day':'2014-03-12',
            'num_men':'1',
            'num_women':'2',
            }
        response = self.c.post('/api/message', data=message)
        self.assertFalse(u'어린이' in Message.objects.all()[3].message)
        self.assertEqual(Message.objects.all().count(), 4)
