from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from guestpub.models import Pub, Message

class PubSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Pub
        geo_field = "point"
        fields = ('refer_id', 'title',  'phone', 'address', 'imageurl',
                    'category', 'placeurl',
                    )

    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.refer_id, self.title)

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('sender_tel', 'receiver_tel', 'result','username', 'day', 'num_men', 'num_women', 'num_children')

    def __unicode__(self):
        return u'%s %s' % (self.id, self.sender_tel)
