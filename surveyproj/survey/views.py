from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.views import generic

from survey.models import Answer, Response, Question


class IndexView(generic.ListView):
    template_name = 'survey/index.html'
    context_object_name = 'latest_questions'

    def get_queryset(self):
        return Question.objects.filter(is_published=True).order_by('-updated_at')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'survey/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'survey/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        answer = question.answer_set.get(pk=request.POST['answer'])
        answer.votes += 1
        answer.save()
        rsp = Response(answer=answer)
        rsp.save()
        return HttpResponseRedirect(reverse('survey:results', args=(question.id,)))
    except (KeyError, Answer.DoesNotExist):
        return render(request, 'survey/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
