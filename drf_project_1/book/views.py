from django.forms import model_to_dict
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from book.models import BookModel, AuthorModel
from .serializers import BookModelSerializer, AuthorModelSerializer, BookListSerializer


class BookListAPIView(APIView):
    def get(self, request, format=None):
        qs = BookModel.objects.all()
        serializer = BookListSerializer(qs, many=True)
        # print(serializer.data)
        # return Response(serializer.data)
        return Response({'status':200, 'data': serializer.data})

    def post(self, request):
        serializer = BookListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'data': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method put not allowed"}, status=405)

        try:
            instance = BookModel.objects.get(pk=pk)
        except:
            return Response({"error": "Object doesnot exist"})

        serializer = BookListSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method delete not allowed"})

        return Response({"post": "delete post" + str(pk)})



class AuthorListAPIView(APIView):
    def get(self, request, format=None):
        author = AuthorModel.objects.all()
        serializer = AuthorModelSerializer(author, many=True)
        return Response({'status': 200, 'data': serializer.data})