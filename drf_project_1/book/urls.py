from django.urls import path
from .views import BookListAPIView, AuthorListAPIView

urlpatterns = [
    path('list/', BookListAPIView.as_view()),
    path('list/<int:pk>/', BookListAPIView.as_view()),
    path('authorlist/', AuthorListAPIView.as_view()),
]