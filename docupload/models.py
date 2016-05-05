from django.db import models

class Documentation(models.Model):
    '''
    Documentation: Model class which holds details of uploaded documentation file
    '''

    name = models.CharField(max_length=200)
    doc_file = models.FilePathField('../static/docs/')
    pub_date = models.DateTimeField('date published')
