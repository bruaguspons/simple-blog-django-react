from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import BlogSerializers
from .models import Blog
from .pagination import SmallSetPagination, MediumSetPagination, LargeSetPagination
from rest_framework.parsers import MultiPartParser


class BlogListView(APIView):
    def get(self, request, format=None):
        if Blog.objects.all().exists():
            blog = Blog.objects.all()
            print(blog)
            pagination = SmallSetPagination()
            results = pagination.paginate_queryset(blog, request)
            serializer = BlogSerializers(results, many=True)

            return pagination.get_paginated_response(serializer.data)
        else:
            return Response({'error': 'Not blogs found'},
                            status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        new_blog = BlogSerializers(data=request.data)
        if new_blog.is_valid():
            new_blog.save()
            return Response(new_blog.data, status=status.HTTP_201_CREATED)
        return Response({'error': new_blog.error_messages}, status=status.HTTP_400_BAD_REQUEST)


class BlogDetail(APIView):
    def get(self, request, pk, format=None):
        blog = get_object_or_404(Blog, uuid=pk)
        serializer = BlogSerializers(blog)
        return Response({'blog': serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        blog = get_object_or_404(Blog, uuid=pk)
        blog.delete()
        return Response(status=status.HTTP_200_OK)
