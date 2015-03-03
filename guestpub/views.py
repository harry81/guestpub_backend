import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from guestpub.serializers import PubSerializer, MessageSerializer
from rest_framework import generics
from guestpub.models import Pub, Message


class PubList(generics.ListCreateAPIView):
    permission_classes = ()
    queryset = Pub.objects.all()
    serializer_class = PubSerializer


class PubDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    queryset = Pub.objects.all()
    serializer_class = PubSerializer


class MessageList(generics.ListCreateAPIView):
    permission_classes = ()
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @csrf_exempt
    def perform_create(self, serializer):
        serializer.save(message=self.request.message)
