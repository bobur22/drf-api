from rest_framework import serializers
from .models import AuthorsModel, BooksModel


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorsModel
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = '__all__'

class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    pages = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    # authors = AuthorSerializer(read_only=True)

    # def create(self, validated_data):
    #     return BooksModel.objects.create(**validated_data)




