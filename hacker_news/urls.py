from django.conf.urls import url

from hacker_news import views
from hacker_news.views import NewsListView, SSOAuthorizationView, UserProfileView

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news_list'),
    url(r'^authorization/$', SSOAuthorizationView.as_view(), name='authorization'),
    url(r'^profile/(?P<pk>\d+)/$', UserProfileView.as_view(), name='profile'),
    url(r'^profile/$', UserProfileView.as_view(), name='self_profile'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^vote-update/(?P<id>\d+)/$', views.vote_update, name='update'),
    url(r'^detail/(?P<id>\d+)/$', views.news_detail, name='news_detail'),
]
