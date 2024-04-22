from django.shortcuts import render
from drf_yasg.openapi import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from .models import AuthorsModel, BooksModel
from .serializers import BooksSerializer, AuthorSerializer, BookSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class BookModelViewSet(ModelViewSet):
    serializer_class = BooksSerializer
    queryset = BooksModel.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class BookAPIView(APIView):
    def get(self, request):
        books = BooksModel.objects.all()
        return Response({'books': BookSerializer(books, many=True).data})

    # def post(self, request):
    #     serializer = BookSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     post_new = BooksModel.objects.create(
    #         name=request.data['name'],
    #         pages=request.data['pages'],
    #         price=request.data['price'],
    #         authors=request.data['authors']
    #     )
    #
    #     return Response({'post': BookSerializer(post_new).data})


# class AuthorViewSet(generics.ListAPIView):
#     serializer_class = AuthorSerializer
#     def get_queryset(self):
#         name = self.request.query_params.get('name')
#         return AuthorsModel.objects.filter(name=name)


class AuthorsModelViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = AuthorsModel.objects.all()
    filter_backends = [filters.OrderingFilter]
    search_fields = ['name', 'id']

    # permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     name = self.request.query_params.get('name')
    #     return AuthorsModel.objects.filter(name=name)
