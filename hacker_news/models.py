from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile')
    nickname = models.CharField(max_length=24, unique=True)
    about = models.TextField(blank=True, null=True)
    picture = models.ImageField(null=True, blank=True)
    cover = models.ImageField(null=True, blank=True)

    # Social Accounts
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    google = models.URLField(null=True, blank=True)
    blogger = models.URLField(null=True, blank=True)
    homepage = models.URLField(null=True, blank=True)
    behance = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])


class News(models.Model):
    """
    News: Model class which holds all the shared links
    """

    title = models.CharField(max_length=300)
    description = models.TextField()
    link = models.URLField(max_length=200)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    link = models.ForeignKey(News)

    def __str__(self):
        return self.text