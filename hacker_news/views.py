from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView

from hacker_news.models import New

from .forms import NewsUploadForm


class NewsListView(ListView):
    queryset = New.objects.order_by("-date")[:10]
    template_name = 'hacker-news/news.html'
    context_object_name = 'news'

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
