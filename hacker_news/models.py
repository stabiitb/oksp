from django.db import models


class News(models.Model):
    '''
    News: Model class which holds all the shared links
    '''

    title = models.CharField(max_length=300)
    link = models.URLField(max_length=200)
    comments = models.IntegerField
    upvotes = models.IntegerField
