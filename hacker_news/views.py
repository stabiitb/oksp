from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.views.generic import ListView, TemplateView

from hacker_news.models import *

from .forms import CommentForm, NewsUploadForm


class UserProfileView(TemplateView):
    template_name = 'profile/profile.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs.pop('pk', None)

        if not pk:
            if request.user.is_authenticated():
                pk = request.user.id
            else:
                return redirect(reverse('hacker-news:login'))

        user = get_object_or_404(User, pk=pk)

        kwargs['user'] = user
        return super().get(request, *args, **kwargs)


class NewsListView(ListView):
    template_name = 'hacker-news/news.html'

    def get(self, request, *args, **kwargs):
        queryset = News.objects.order_by('-post_date')
        context = locals()
        context[self.context_object_name] = queryset
        tags = []
        for i in News.objects.all():

        return render_to_response(self.template_name, {
            'news': News.objects.all()
        })


def news_edit(request, id=None):
    instance = get_object_or_404(News, id=id)
    form = NewsUploadForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('hacker-news:news_list'))
    context = {"form": form, }
    return render(request, "hacker-news/news_upload.html", context)


def news_delete(request, id=None):
    instance = get_object_or_404(News, id=id)
    instance.delete()
    return redirect('hacker-news:news_list')


def news_detail(request, id=None):
    instance = get_object_or_404(News, id=id)
    form = CommentForm(request.POST or None)
    reply = CommentForm(request.POST or None)
    if 'Comment' in request.POST:
        if form.is_valid():
            form_obj = Comment(text=request.POST.get('text'),
                               link=instance,
                               comment_link=None)
            form_obj.save()
            return HttpResponseRedirect(reverse('hacker-news:news_detail',
                                                kwargs={'id': id}))
    else:
        if reply.is_valid():
            comment_instance = get_object_or_404(
                Comment, id=request.POST.get('comment_id'))
            form_obj = Comment(text=request.POST.get('text'),
                               link=instance,
                               comment_link=comment_instance)
            form_obj.save()
            return HttpResponseRedirect(reverse('hacker-news:news_detail',
                                                kwargs={'id': id}))
    comments = instance.comment_set.filter(comment_link=None)
    reply_comments = instance.comment_set.filter(comment_link__isnull=False)

    context = {
        'news': instance,
        'comments': comments,
        'form': form,
        'reply': reply,
        'reply_comments': reply_comments,
    }
    return render(request, 'hacker-news/news_detail.html', context)


def upvote(request, id=None):
    instance = get_object_or_404(News, id=id)
    user = request.user
    member = Member.objects.get(user=user)
    vote = Vote.objects.get(user=member)
    votes = vote.amount
    if votes == 1:
        instance.votes -= 1
        vote.amount = 0
    elif votes == 0:
        instance.votes += 1
        vote.amount = 1
    else:
        instance.votes += 2
        vote.amount = 1
    instance.save()
    vote.save()
    return HttpResponseRedirect(reverse('hacker-news:news_list'))


def downvote(request, id=None):
    instance = get_object_or_404(News, id=id)
    user = request.user
    member = Member.objects.get(user=user)
    vote = Vote.objects.get(user=member)
    votes = vote.amount
    if votes == 1:
        instance.votes -= 2
        vote.amount = -1
    elif votes == 0:
        instance.votes -= 1
        vote.amount = -1
    else:
        instance.votes += 1
        vote.amount = 0
    instance.save()
    vote.save()
    return HttpResponseRedirect(reverse('hacker-news:news_list'))


def upload(request):
    form = NewsUploadForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('hacker-news:news_list'))
    context = {"form": form, }
    return render(request, "hacker-news/news_upload.html", context)
