from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import ListView
from flask.views import View

from django.contrib import auth
from django.contrib.auth.models import User, Group
from hacker_news.models import News, UserProfile
from oauth.authorization import Authorization
from oauth.exceptions import OAuthError
from oauth.request import UserFieldAPIRequest

class NewsListView(ListView):
    queryset = News.objects.order_by("-date")[:10]
    template_name = 'hacker-news/news.html'
    context_object_name = 'news'

class SSOAuthorizationView(View):

    def get(self, request):
        if request.user.is_authenticated():
            if request.GET.get('next') != '' and request.GET.get('next') is not None:
                return redirect(request.GET.get('next'))
            else:
                return redirect(settings.LOGIN_REDIRECT_URL)
        try:
            token = Authorization(request).get_token()
        except OAuthError as e:
            return render(request, 'hacker-news/login.html', {'error': e.message, 'client_id': settings.CLIENT_ID})

        if not token:
            return render(request, 'hacker-news/login.html', {'client_id': settings.CLIENT_ID})

        user_obj = UserFieldAPIRequest(
            fields=[
                'id',
                'first_name',
                'last_name',
                'email',
                'username',
            ],
            access_token=token.access_token,
        ).get_oauth_user()

        user, created = User.objects.get_or_create(username=user_obj.username)  # type: Tuple[User, bool]
        user.set_unusable_password()

        user.first_name = user_obj.first_name
        user.last_name = user_obj.last_name
        user.email = user_obj.email
        user.is_staff = True
        user.save()

        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.nickname = user_obj.username
        user_profile.save()

        group = Group.objects.get(name__iexact='Content Developer')
        group.user_set.add(user)

        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth.login(request, user)

        if request.GET.get('state') != '' and request.GET.get('state') is not None:
            return redirect(request.GET.get('state'))
        else:
            return redirect(settings.LOGIN_REDIRECT_URL)
