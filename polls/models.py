import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # To return string instead of id
    def __str__(self):
        return self.question_text

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def was_published_recently(self):
        """
        docstring
        """
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    # Kind of change the True or False to an icon True or False
    was_published_recently.boolean = True
    was_published_recently.short_description = 'published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text


# We already know what the problem is: Question.was_published_recently() in tests.py should return False if its pub_date is in the future. Amend the method in models.py, so that it will only return True if the date is also in the past:

