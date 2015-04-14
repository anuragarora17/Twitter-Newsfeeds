import string

from django.views.generic import FormView, ListView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .forms import CountryForm
from .models import Country, News
from get_trending_tags import get_tags, keyword_generator, get_urls, get_articles


class CountryFormView(FormView):
    form_class = CountryForm
    template_name = 'newsfeeds/index.html'

    def form_valid(self, form):
        data = form.cleaned_data
        country = Country.objects.filter(code=data['country']).first()
        return redirect('/' + country.name.lower())


class CountryNewsView(ListView):
    template_name = 'newsfeeds/news.html'
    model = News

    def get_queryset(self):
        country = self.kwargs['country']
        query_set = News.objects.filter(country=Country.objects.filter(name=country).first()).all()
        return query_set