from django.views.generic import ListView, TemplateView
from post_app.models import Slider, News


class IndexView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['slider'] = Slider.objects.all()
        context['news'] = News.objects.all()[:1]
        context['news_offset'] = 1
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
        context['object_list_offset'] = self.default_list_limit
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