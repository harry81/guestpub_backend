from django.conf.urls import patterns, url
from guestpub.views import PubList, PubDetail, message_list, CommentList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('guestpub.views',
                    url(r'^pub/$', PubList.as_view()),
                    url(r'^pub/(?P<pk>[0-9]+)/$', PubDetail.as_view()),
                    url(r'^message$', message_list),
                    url(r'^comment/$', CommentList.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)

