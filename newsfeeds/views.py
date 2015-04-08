import string

from django.views.generic import FormView, TemplateView
from django.http import HttpResponseRedirect, HttpResponse

from .forms import CountryForm
from .models import News
from get_trending_tags import get_tags, keyword_generator, get_urls, get_articles


class CountryFormView(FormView):
    form_class = CountryForm
    template_name = 'newsfeeds/index.html'
    success_url = '/data'

    def form_valid(self, form):
        data = form.cleaned_data
        print data
        return HttpResponseRedirect(self.get_success_url()), data



