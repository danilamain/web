from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionManager(models.Manager):
    def new(self, *args, **kwargs):
        return self.order_by('-added_at')

    def popular(self, *args, **kwargs):
        return self.order_by('-likes')


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True, blank=False)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="likes_set")

    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
