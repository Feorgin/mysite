from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice

from rest_framework import generics
from polls.serializers import QuestionSerializer, ChoiceSerializer


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse("You're looking at question %s." % question)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choices.all()
    output = ', '.join([str(c) for c in choices])
    return HttpResponse(output)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def vote_user(request, question_id, user_id):
    return HttpResponse("You're voting on question {}. for user {}".format(question_id, user_id))


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer

    def get_object(self):
        obj = get_object_or_404(Question, pk=self.kwargs.get('question_id'))
        return obj


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChoiceSerializer

    def get_object(self):
        obj = get_object_or_404(Choice, pk=self.kwargs.get('choice_id'))
        return obj
