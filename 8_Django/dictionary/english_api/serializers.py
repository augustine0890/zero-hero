from rest_framework import serializers

from .models import Word


class WordSerializer(serializers.ModelSerializer):
    """Serializes the Word"""

    class Meta:
        model = Word
        fields = '__all__'