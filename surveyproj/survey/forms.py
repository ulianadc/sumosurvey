from django import forms
from django.utils import timezone


class QuestionForm(forms.Form):
    question_text = forms.CharField()
    published_at = forms.DateTimeField(initial=timezone.now)


class AnswerForm(forms.Form):
    answer_text = forms.CharField()
