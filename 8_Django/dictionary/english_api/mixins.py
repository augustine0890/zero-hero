from rest_framework import mixins
from rest_framework import viewsets

from . import models
from . import serializers


class WordViewSet(mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.ListModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    queryset = models.Word.objects.all()
    serializer_class = serializers.WordSerializer