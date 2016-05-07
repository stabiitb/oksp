from django.db import models


class New(models.Model):
    '''
    News: Model class which holds all the shared links
    '''

    title = models.CharField(max_length=300)
    description = models.TextField()
    link = models.URLField(max_length=200)
    upvotes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class comment(models.Model):
    text = models.TextField()
    link = models.ForeignKey(New)
    def __unicode__(self):
        return self.text
