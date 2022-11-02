from django.urls import path, include
from .views import BlogListView, BlogDetail
urlpatterns = [
    path('', BlogListView.as_view()),
    path('<uuid:pk>/', BlogDetail.as_view())
]
