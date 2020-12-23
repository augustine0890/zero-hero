import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.question_text

    # def was_published_recently(self):
        # now = timezone.now()
        # return now >= self.pub_date >= now - datetime.timedelta(days=1)
    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    # votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    choice =  models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("question", "voted_by")


# class Author(models.Model):
    # name = models.CharField(max_length=100)
    # age = models.IntegerField()


# class Publisher(models.Model):
    # name = models.CharField(max_length=300)


# class Book(models.Model):
    # name = models.CharField(max_length=300)
    # pages = models.IntegerField()
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # rating = models.FloatField()
    # authors = models.ManyToManyField(Author)
    # publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    # pubdate = models.DateField()


# class Store(models.Model):
    # name = models.CharField(max_length=300)
    # books = models.ManyToManyField(Book)