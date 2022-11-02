from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='get_image')

    class Meta:
        model = Category
        fields = [
            'name',
            'image'
        ]
