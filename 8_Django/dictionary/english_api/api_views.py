from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Word
from .serializers import WordSerializer


class WordList(APIView):
    """View to list all words in database"""

    def get(self, request):
        words = Word.objects.all()
        data = WordSerializer(words, many=True).data
        return Response(data)
    
    def post(self, request):
        serializer = WordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)