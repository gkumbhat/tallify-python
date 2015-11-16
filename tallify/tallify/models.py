__author__ = 'nicolette'
from django.db import models


class Analysis(models.Model):
    userid = models.CharField(max_length=50)
    words = models.CharField(max_length=100)
    texts = models.CharField(max_length=400)
    count = models.IntegerField(default=0)
    compoundNouns = models.CharField(max_length=100)
    stopWords = models.CharField(max_length=400)
    date = models.DateField()


