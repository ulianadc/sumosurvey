import datetime

from django.shortcuts import reverse
from django.test import TestCase
from django.utils import timezone

from survey.models import Question


def create_question(text, **kwargs) -> Question:
    return Question.objects.create(text=text, published_at=(timezone.now() + datetime.timedelta(**kwargs)))


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('survey:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No new surveys are available')
        self.assertQuerysetEqual(response.context['latest_questions'], [])

    def test_past_question(self):
        """
        Questions with published date in the past are displayed on the index page.
        """
        q = create_question(text='Past question.', days=-30)
        response = self.client.get(reverse('survey:index'))
        self.assertQuerysetEqual(response.context['latest_questions'], [q])

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on the index page.
        """
        create_question(text='Future question.', days=30)
        response = self.client.get(reverse('survey:index'))
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context['latest_questions'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions are displayed.
        """
        q1 = create_question(text='Past question.', days=-30)
        create_question(text='Future question.', days=30)
        response = self.client.get(reverse('survey:index'))
        self.assertQuerysetEqual(response.context['latest_questions'], [q1])

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions, ordered by updated time descending.
        """
        q1 = create_question(text='Past question 1.', days=-30)
        q2 = create_question(text='Past question 2.', days=-15)
        q3 = create_question(text='Past question 3.', days=-5)
        q2.text = 'Past question 2 (updated).'
        q2.save()
        response = self.client.get(reverse('survey:index'))
        self.assertQuerysetEqual(response.context['latest_questions'], [q2, q3, q1])


class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        q = create_question(text='Future question', days=1)
        response = self.client.get(reverse('survey:detail', args=(q.pk,)))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        q = create_question(text='Past question', days=-1)
        response = self.client.get(reverse('survey:detail', args=(q.pk,)))
        self.assertContains(response, q.text)
