import json
from django.http import HttpResponse

from guestpub.serializers import PubSerializer
from rest_framework import generics
from guestpub.models import Pub


class PubList(generics.ListCreateAPIView):
    permission_classes = ()
    queryset = Pub.objects.all()
    serializer_class = PubSerializer


class PubDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    queryset = Pub.objects.all()
    serializer_class = PubSerializer


def send_message(request):
    # coupon_code = request.POST['coupon_code']
    # phone = request.POST['phone']
    # email = request.POST['email']
    email = {'name':'hello'}
    return HttpResponse(json.dumps(email), content_type="application/json")

