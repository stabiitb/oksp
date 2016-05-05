from django.shortcuts import render
from django.views.generic import ListView

from hacker_news.models import News


class NewsListView(ListView):
    queryset = News.objects.order_by("-date")[:10]
    template_name = 'hacker-news/news.html'
    context_object_name = 'news'