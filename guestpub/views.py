from django.views.decorators.csrf import csrf_exempt
from rest_framework import filters
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_gis.filters import InBBoxFilter
from guestpub.serializers import PubSerializer, MessageSerializer, CommentSerializer
from guestpub.models import Pub, Message, Comment


class PubList(generics.ListCreateAPIView):
    permission_classes = ()
    queryset = Pub.objects.all()
    serializer_class = PubSerializer
    bbox_filter_field = 'point'
    filter_backends = (InBBoxFilter, )


class PubDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    queryset = Pub.objects.all()
    serializer_class = PubSerializer


class MessageList(generics.ListCreateAPIView):
    permission_classes = ()
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

@api_view(['GET', 'POST'])
def message_list(request):
    if request.method == 'GET':
        snippets = Message.objects.all()
        serializer = MessageSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentList(generics.ListAPIView):
    permission_classes = ()
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('pub','comment_id', 'time')
