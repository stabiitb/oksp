from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^redirect/?$',
        views.redirect_function,
        name='redirect'),
]
