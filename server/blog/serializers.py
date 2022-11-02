from rest_framework import serializers
from category.serializer import CategorySerializer
from .models import Blog


class BlogSerializers(serializers.ModelSerializer):
    # image = serializers.ImageField(sourse='get_image', required=False)
    category = CategorySerializer(required=False)

    class Meta:
        model = Blog
        fields = [
            'uuid',
            'title',
            'content',
            'category',
            'published',
            'status'
        ]
