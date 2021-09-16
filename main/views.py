from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Question, Choice


# Create your views here.


class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'home.html'


class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question'

    def get_context_data(self, *args, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(*args, **kwargs)
        return context


def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'main/results.html', {'question': question})


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    print(question.pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'main/question_detail.html',
                      {'selected_choice': selected_choice, 'error_message': 'You did not select a choice', })
    else:
        selected_choice.no_votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('main:results', args=(question.pk, )))
