from guestpub.models import Pub
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class PubSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Pub
        geo_field = "point"
        fields = ('refer_id', 'title',  'phone',
                    'point', 'address', 'imageUrl',
                    'category', 'placeUrl',
                    )

    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.refer_id, self.title)

