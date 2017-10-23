from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """
    Mixin with created-, updated-at datetimes.
    """
    class Meta:
        abstract = True

    created_at = models.DateTimeField('datetime created', auto_now_add=True)
    updated_at = models.DateTimeField('datetime updated', auto_now=True)


class Question(BaseModel):
    """
    Survey question.
    """
    is_published = models.BooleanField('is published', default=False)
    published_at = models.DateTimeField('datetime published', null=True)
    text = models.CharField('question text', max_length=500)


class Choice(BaseModel):
    """
    Survey answer choice.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField('answer text', max_length=500)
    votes = models.IntegerField(default=0)


class Answer(BaseModel):
    """
    Survey answer
    """
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
