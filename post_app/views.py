#coding: UTF-8
from django.views.generic import ListView, TemplateView
from post_app.models import Slider, News


class IndexView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['slider'] = Slider.objects.all()

        context['news'] = News.objects.all()[:1]
        context['news_offset'] = 1
        context['news_list_limit'] = 1
        context['news_url'] = 'news'
        context['news_more_button_id'] = 'news-more-id'
        context['news_more_button_label'] = u'Ещё новости'
        context['news_tab_id'] = 'first'

        return context


class PaginationMixin(object):
    def get_queryset(self):
        if 'offset' in self.request.GET:
            self.offset = int(self.request.GET['offset'])
        else:
            self.offset = None

        if 'limit' in self.request.GET:
            self.limit = int(self.request.GET['limit'])
        else:
            self.limit = None

        return self.model.objects.all()[self.offset: self.offset + self.limit]

    def get_context_data(self, **kwargs):
        context = super(PaginationMixin, self).get_context_data(**kwargs)
        context['default_list_limit'] = self.default_list_limit
        context['data_url'] = self.data_url
        context['more_button_id'] = self.more_button_id
        context['more_button_label'] = self.more_button_label
        context['tab_id'] = 'first'

        if self.offset and self.limit:
            context['object_list_offset'] = self.offset + self.limit
        else:
            context['object_list_offset'] = 0

        return context


class NewsView(PaginationMixin, ListView):
    template_name = 'news.html'
    model = News
    data_url = 'news'
    default_list_limit = 1
    more_button_id = 'news-more-id'
    more_button_label = u'Ещё новости'
    tab_id = 'First'
