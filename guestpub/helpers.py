# -*- coding: utf-8 -*-
import base64
import httplib, urllib2
import json
from collections import namedtuple
from lxml import etree

from constance import config
from django.conf import settings

path = "/smscenter/v1.0/sendsms"
credential = "Basic "+base64.encodestring(settings.BLUEHOUSE_APPID +':'+ settings.BLUEHOUSE_APIKEY).strip()
headers = {
    "Content-type": "application/json;charset=utf-8",
    "Authorization": credential,
}

DAUM_DETAIL_URL = "http://m.map.daum.net/actions/detailInfoView?id=%s"

CommentEntry = namedtuple('CommentEntry', ['comment_id', 'time', 'name', 'num_rate', 'msg'])

class MessageGateway():
    def send(self, sender, receiver, message):
        if not config.ENABLE_SEND_SMS:
            return False

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
            return True
        return False

class PubScrapy():
    def get_review(self, daum_id):
        reqUrl = DAUM_DETAIL_URL % daum_id
        response = urllib2.urlopen(reqUrl).read()
        tree = etree.HTML(response)

        response = {'comments':[], 'homepage': tree.xpath("//p/a")[0].values()[0]}

        for cmt_body in tree.xpath('//div[@class="list_cmt"]'):
            comment_id = cmt_body.attrib['data-commentid']
            time = cmt_body.xpath('div/span[@class="txt_time"]')[0].text
            name = cmt_body.xpath('div/span[@class="txt_name"]')[0].text
            num_rate = cmt_body.xpath('div/em[@class="num_rate"]')[0].text
            msg = cmt_body.xpath('div/div/span[@class="txt_desc"]')[0].text

            ent = CommentEntry(comment_id = comment_id, time = time, name = name, num_rate = num_rate, msg = msg)
            response['comments'].append(dict(ent.__dict__))
        return response
