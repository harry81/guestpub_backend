# -*- coding: utf-8 -*-
import base64
import httplib
import json

from constance import config
from django.conf import settings

path = "/smscenter/v1.0/sendsms"
credential = "Basic "+base64.encodestring(settings.BLUEHOUSE_APPID +':'+ settings.BLUEHOUSE_APIKEY).strip()
headers = {
    "Content-type": "application/json;charset=utf-8",
    "Authorization": credential,
}

class MessageGateway():
    def send(self, sender, receiver, message):
        if not config.ENABLE_SEND_SMS:
            return False, 'ENABLE_SEND_SMS is disabled.'

        c = httplib.HTTPSConnection(settings.BLUEHOUSE_URL)
        value = {
            'sender'     : sender,
            'receivers'  : receiver,
            'content'    : message,
        }
        data = json.dumps(value, ensure_ascii=False).encode('utf-8')
        c.request("POST", path, data, headers)
        res = c.getresponse()
        if res.status == 200:
            return True, 'Success'
        return False,  'Success'

