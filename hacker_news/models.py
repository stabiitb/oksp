from django.db import models


class New(models.Model):
    '''
    News: Model class which holds all the shared links
    '''

    title = models.CharField(max_length=300)
    link = models.URLField(max_length=200)
    comments = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
