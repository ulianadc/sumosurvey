from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, reverse
from django.utils import timezone
import random

from survey.forms import AnswerForm, QuestionForm
from survey.models import Answer, Response, Question


def index(request):
    """
    Return random survey question not answered by the requesting session.
    """
    answered = request.session.get('answered_questions', [])
    qry = Question.objects.filter(published_at__lte=timezone.now()).exclude(id__in=answered)
    return render(request, 'survey/index.html', {
        'question': qry.all()[random.randrange(qry.count())] if qry.count() else None,
        # 'error_message': 'Hold your horses..!'
    })


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if not question.is_published() and request.user.is_superuser:
        raise Http404('Unable to find this question.')
    ctx = {
        'question': question,
        'recent_responses': Response.objects.select_related('answer').filter(answer__question=question_id)
                                            .order_by('-created_at')[:20],
    }
    return render(request, 'survey/results.html', ctx)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        answer = question.answer_set.get(pk=request.POST['answer'])
        answer.votes += 1
        answer.save()
        rsp = Response(answer=answer)
        rsp.save()
        answered = request.session.get('answered_questions', [])
        answered += [question.id]
        request.session['answered_questions'] = answered
        return HttpResponseRedirect(reverse('survey:results', args=(question.id,)))
    except (KeyError, Answer.DoesNotExist):
        return render(request, 'survey/detail.html', {
            'question': question,
            'error_message': 'You didn\'t select a choice.',
        })


@login_required
def manage_index(request):
    return render(request, 'survey/manage/index.html', {
        'questions': Question.objects.order_by('-updated_at').all()[:50],
    })


@login_required
def manage_new(request):
    answer_formset = formset_factory(AnswerForm, extra=3, max_num=10)
    if request.method == 'POST':
        qf = QuestionForm(request.POST)
        afs = answer_formset(request.POST)
        if qf.is_valid() and afs.is_valid():
            q = Question(text=qf.cleaned_data['question_text'], published_at=qf.cleaned_data['published_at'])
            q.save()
            for f in afs:
                ans = Answer(text=f.cleaned_data['answer_text'], question=q)
                ans.save()
            return HttpResponseRedirect(reverse('survey:manage/index'))
    else:
        fs = answer_formset()
    return render(request, 'survey/manage/new.html', {
        'question_form': QuestionForm(),
        'answer_formset': fs,
    })


# @login_required
# def manage_edit(request, question_id):
#     return render(request, 'survey/manage/edit.html', {
#         'question': Question.objects.get(pk=question_id),
#     })
