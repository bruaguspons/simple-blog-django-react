from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CategorySerializer
from .models import Category


class CategroryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
# Create your views here.
