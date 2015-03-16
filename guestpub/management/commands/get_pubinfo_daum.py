# -*- coding: utf-8 -*-

import urllib2
import json
import requests
from requests.auth import HTTPBasicAuth

from django.core.management.base import BaseCommand
from guestpub.models import Pub

class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        urls  = [u'https://apis.daum.net/local/v1/search/keyword.json?page=%s&query=제주게스트하우스&apikey=9f68e425f40e190b407745eb855619262ce0b2cc&image=only&location=127.0017531,37.5395269'
                 % page for page in range(1, 4)]
        for url in urls:
            response = urllib2.urlopen(url.encode('utf-8'))
            data = response.read()
            output = json.loads(data)
            houses = output['channel']['item']

            print url
            for entry in houses:
                payload = {}
                for k, v in entry.items():
                    payload[k.lower()] = v
                payload['point']= "POINT(%s %s)" % (payload['longitude'], payload['latitude'])
                payload['refer_id'] = payload['id']
                req = requests.post("http://localhost:8000/api/pub/", data=payload, auth=HTTPBasicAuth('admin', 'jkl'))
                print payload['refer_id']

