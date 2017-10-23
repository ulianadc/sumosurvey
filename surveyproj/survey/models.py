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
    published_at = models.DateTimeField('datetime published', blank=True, null=True)
    text = models.CharField('question text', max_length=500)

    def is_published(self):
        return self.published_at and self.published_at < timezone.now()

    def total_votes(self):
        return sum([a.votes for a in self.answer_set.all()])

    def __str__(self):
        return self.text


class Answer(BaseModel):
    """
    One of multiple-choice answers to a survey question.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField('answer text', max_length=500)
    votes = models.IntegerField(default=0)

    def percent_vote(self):
        return 100 * self.votes / self.question.total_votes()

    def __str__(self):
        return self.text


class Response(BaseModel):
    """
    Survey answer
    """
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer.text
