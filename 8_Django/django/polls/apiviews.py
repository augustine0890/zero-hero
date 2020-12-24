# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer, VoteSerializer


# class QuestionList(APIView):
    # def get(self, request):
        # questions = Question.objects.all()[:10]
        # data = QuestionSerializer(questions, many=True).data
        # return Response(data)

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# class QuestionDetail(APIView):
    # def get(self, request, pk):
        # question = get_object_or_404(Question, pk=pk)
        # data = QuestionSerializer(question).data
        # return Response(data)

class QuestionDetail(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer

