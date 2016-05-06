from django.conf.urls import url

from hacker_news import views
from hacker_news.views import NewsListView

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news_list'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^vote-update/(?P<id>\d+)/$', views.vote_update, name='update'),
]
