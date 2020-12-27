from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__ (self):
        return self.question

class Choices(models.Model):
    Question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_txt = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__ (self):
        return self.choice_txt
