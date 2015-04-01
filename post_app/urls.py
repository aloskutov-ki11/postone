from django.conf.urls import patterns, url
from post_app.views import *
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^news/$', NewsView.as_view()),
    url(r'^document/$', DocumentView.as_view()),
    url(r'^resource/$', ResourceView.as_view()),
    url(r'^schedule/$', GuardGroupView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^$', IndexView.as_view()),
)
