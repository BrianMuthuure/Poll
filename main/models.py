from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Question(models.Model):
    text = models.TextField()
    date_posted = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['date_posted', ]

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('main:question_detail', kwargs={'pk': self.pk})


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    no_votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'
