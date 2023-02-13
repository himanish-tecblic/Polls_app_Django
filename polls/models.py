import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Questions(models.Model):
    questions_text = models.CharField(max_length=100)
    pub_text = models.DateTimeField('date published')

    def __str__(self):
        return self.questions_text

    def was_publisted_recntly(self):
        return self.pub_date >= timezone.now() -datetime.timedalta(days = 1)

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete = models.CASCADE)
    Choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 

    def __str__(self):
        return self.Choice_text