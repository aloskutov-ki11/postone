from django.conf.urls import patterns, url
from post_app.views import IndexView, NewsView

urlpatterns = patterns('',
    url(r'^news/$', NewsView.as_view()),
    url(r'^$', IndexView.as_view()),
)
