from django.db import models

# Create your models here.

class Questions(models.Model):
    questions_text = models.CharField(max_length=100)
    pub_text = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete = models.CASCADE)
    Choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 