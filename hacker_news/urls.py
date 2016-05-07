from django.conf.urls import url
from hacker_news.views import NewsListView, SSOAuthorizationView
from hacker_news import views

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news_list'),
    url(r'^authorization/$', SSOAuthorizationView.as_view("auth"), name='authorization'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^vote-update/(?P<id>\d+)/$', views.vote_update, name='update'),
    url(r'^detail/(?P<id>\d+)/$', views.news_detail, name='news_detail'),
]
