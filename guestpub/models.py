# -*- coding: utf-8 -*-

from datetime import datetime
from django.contrib.gis.db import models
from cms.models import CMSPlugin
from guestpub.helpers import MessageGateway

import logging
logger = logging.getLogger(__name__)


class Message(models.Model):
    # customer
    # accomodation
    sender_tel = models.CharField(max_length=20, blank=True, default='')
    receiver_tel = models.CharField(max_length=20, blank=True, default='')
    username = models.CharField(max_length=20, blank=True, default='')
    day = models.CharField(max_length=20, blank=True, default='')
    result = models.BooleanField(default=False)
    num_men = models.IntegerField(default=0, blank=True)
    num_women= models.IntegerField(default=0, blank=True)
    num_children= models.IntegerField(default=0, blank=True)
    message = models.CharField(max_length=256, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    def send(self, sender, receiver, message):
        gateway = MessageGateway()
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.result = gateway.send(sender, receiver, message)
        self.save()
        return True

    def __unicode__(self):
        return u'%s %s' % (self.pk, self.message)

    def save(self, *args, **kwargs):
        self.message = u"안녕하세요 {day}에 남{num_men}명 여{num_women} 어린이 {num_children} 숙박 가능한가요?".format(**self.__dict__)
        msgGate = MessageGateway()
        #self.result = msgGate.send(self.sender_tel, [self.receiver_tel,], self.message)
        self.result = msgGate.send('01064117846', ['01064117846',], self.message)
        super(Message, self).save(*args, **kwargs)


class Pub(models.Model):
    refer_id = models.CharField(max_length=20, blank=True, default='', primary_key=True)
    title = models.CharField(max_length=128, blank=False, default='')
    phone = models.CharField(max_length=32, blank=True, default='')
    address = models.CharField(max_length=256, blank=True, default='')
    imageUrl = models.CharField(max_length=256, blank=True, default='')
    category = models.CharField(max_length=256, blank=True, default='')
    placeUrl = models.CharField(max_length=256, blank=True, default='')
    point = models.PointField(blank=True, default="POINT(0 0)")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        kwargs['force_insert'] = not Pub.objects.filter(refer_id=self.refer_id).exists()
        if not kwargs['force_insert']:
            kwargs['update_fields'] = ['title', 'phone','address','imageUrl', 'category']

        super(Pub, self).save(*args, **kwargs) # Call the "real" save() method.

    def __unicode__(self):
        return u'%s %s' % (self.refer_id, self.title)

class PubListPlugin(CMSPlugin):
    number = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%d' % (self.number)
