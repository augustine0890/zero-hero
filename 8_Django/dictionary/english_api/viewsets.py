from rest_framework import viewsets

from . import models
from . import serializers


class WordViewSet(viewsets.ModelViewSet):
    queryset = models.Word.objects.all()
    serializer_class = serializers.WordSerializer