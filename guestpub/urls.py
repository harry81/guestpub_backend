from django.conf.urls import patterns, url
from guestpub.views import PubList, PubDetail, message_list
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('guestpub.views',
                    url(r'^pub/$', PubList.as_view()),
                    url(r'^pub/(?P<pk>[0-9]+)/$', PubDetail.as_view()),
                    url(r'^message$', message_list),
)

urlpatterns = format_suffix_patterns(urlpatterns)

