from django.db import models


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

    def __str__(self):
        return f'{self.pk}: {self.text}'


class Answer(BaseModel):
    """
    One of multiple-choice answers to a survey question.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField('answer text', max_length=500)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.pk}: {self.text}'


class Response(BaseModel):
    """
    Survey answer
    """
    choice = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk}: {self.choice.text}'
