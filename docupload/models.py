from django.conf import settings
from django.db import models


# Create your models here.

class Documentation(models.Model):
    '''
    Documentation: Model class which holds details of uploaded documentation file
    '''

    name = models.CharField(max_length=200)
    #doc_file = models.FilePathField('../static/docs/')
    doc_file = models.FileField(upload_to = '%s/media/' %settings.BASE_DIR)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
