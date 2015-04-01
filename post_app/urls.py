from django.conf.urls import patterns, url
from post_app.views import *

urlpatterns = patterns('',
    url(r'^news/$', NewsView.as_view()),
    url(r'^document/$', DocumentView.as_view()),
    url(r'^resource/$', ResourceView.as_view()),
    url(r'^schedule/$', GuardGroupView.as_view()),
    url(r'^$', IndexView.as_view()),
)
