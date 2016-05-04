from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^editor_choice/$', views.editor_choice, name='editor_choice'),
    url(r'^editor_choice/markdown$', views.markdown_editor, name='markdown_editor'),
    url(r'^editor_choice/wsyiwyg$', views.wsyiwyg_editor, name='wsyiwyg_editor'),
]
