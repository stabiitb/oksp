from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView

from hacker_news.models import New, comment

from .forms import NewsUploadForm, CommentForm


class NewsListView(ListView):
    template_name = 'hacker-news/news.html'
    context_object_name = 'news'

    def get(self, request, *args, **kwargs):
        queryset = New.objects.order_by('-post_date')
        context = locals()
        context[self.context_object_name] = queryset
        return render_to_response(self.template_name, context, context_instance=RequestContext(request))

def news_detail(request, id=None):
    instance = get_object_or_404(New, id = id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form_obj = comment(text=request.POST.get('text'), link = instance, comment_link=None)
        form_obj.save()
        return HttpResponseRedirect(reverse('hacker-news:news_detail', kwargs={'id': id}))
    comments = instance.comment_set.all()


    context = {
        'news': instance,
        'comments': comments,
        'form': form,
    }
    return render(request, 'hacker-news/news_detail.html', context) 

def vote_update(request, id=None):
    instance = get_object_or_404(New, id = id)
    instance.upvotes += 1
    instance.save()
    return HttpResponseRedirect(reverse('hacker-news:news_list'))


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
