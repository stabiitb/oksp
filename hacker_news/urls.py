from django.conf.urls import url
from hacker_news.views import NewsListView, SSOAuthorizationView

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news_list'),
    url(r'^authorization/$', SSOAuthorizationView.as_view("auth"), name='authorization'),
]
