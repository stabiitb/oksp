from django.conf.urls import url

from hacker_news import views
from hacker_news.views import NewsListView

urlpatterns = [
    url(r'^$', NewsListView.as_view(),
        name='news_list'),
    # url(r'^profile/(?P<pk>\d+)/$', UserProfileView.as_view(), name='profile'),
    # url(r'^profile/$', UserProfileView.as_view(), name='self_profile'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^edit-link/(?P<id>\d+)/$',
        views.news_edit,
        name='news_edit'),
    url(r'^delete-link/(?P<id>\d+)/$',
        views.news_delete,
        name='news_delete'),
    url(r'^upvote/(?P<id>\d+)/$',
        views.upvote,
        name='upvote'),
    url(r'^downvote/(?P<id>\d+)/$',
        views.downvote,
        name='downvote'),
    url(r'^detail/(?P<id>\d+)/$',
        views.news_detail,
        name='news_detail'),
]
