from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import ListView

from hacker_news.models import New

from .forms import NewsUploadForm


class NewsListView(ListView):
    queryset = New.objects.all()#order_by("-date")[:10]
    template_name = 'hacker-news/news.html'
    context_object_name = 'news'

    def get(self, request, *args, **kwargs):
        context = locals()
        context[self.context_object_name] = self.queryset
        return render_to_response(self.template_name, context, context_instance=RequestContext(request))
 
def vote_update(request, id=None):
    instance = get_object_or_404(New, id = id)
    instance.upvotes += 1
    instance.save()
    return HttpResponseRedirect(reverse('hacker-news:news_list'))


def register(request):
    return render(request, 'hacker-news/register.html')

def login(request):
    return render(request, 'hacker-news/login.html')

def upload(request):
    form = NewsUploadForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False) 
        instance.save()
        return HttpResponseRedirect(reverse('hacker-news:news_list'))
    context = {
        "form": form,
    }
    return render(request, "hacker-news/news_upload.html", context)
