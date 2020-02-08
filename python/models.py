from django.db import models

# Create your models here.
class Python_Interview_Question_Answer(models.Model):
    question = models.CharField(max_length=254,null=True,blank=True)
    answer = models.TextField()
    def __str__(self):
        return self.question

class Quiz(models.Model):
    quiz_question = models.CharField(max_length=254)
    option_a = models.CharField(max_length=254)
    option_b = models.CharField(max_length=254)
    option_c = models.CharField(max_length=254)
    option_d = models.CharField(max_length=254)
    answer = models.CharField(max_length=254)
    def __str__(self):
        return self.quiz_question
