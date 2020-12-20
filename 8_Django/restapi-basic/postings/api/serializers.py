from rest_framework import serializers

from postings.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer): # forms.ModelForm
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BlogPost
        fields = [
            'url',
            'pk',
            'user',
            'title',
            'content',
            'timestamp',
        ]
    
    # Converts to JSON
    # Validation for data passed

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)