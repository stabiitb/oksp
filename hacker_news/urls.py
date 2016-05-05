from django.conf.urls import url

from hacker_news.views import NewsListView

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news_list'),
]
