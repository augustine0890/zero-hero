from rest_framework import generics

from . import models
from . import serializers


class ListCreateWord(generics.ListCreateAPIView):
    queryset = models.Word.objects.all()
    serializer_class = serializers.WordSerializer


class RetrieveUpdateDestroyWord(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Word.objects.all()
    serializer_class = serializers.WordSerializer