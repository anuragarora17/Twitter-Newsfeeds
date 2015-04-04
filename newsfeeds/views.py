from django.views.generic import FormView
from django.http import HttpResponseRedirect

from newsfeeds.forms import CountryForm
from get_trending_tags import get_tags


class CountryFormView(FormView):
    form_class = CountryForm
    template_name = 'newsfeeds/index.html'
    success_url = '/'

    def form_valid(self, form):
        data = form.cleaned_data
        print data
        trending_tags = get_tags(data['country'])
        for item in trending_tags:
            print item

        return HttpResponseRedirect(self.get_success_url())


