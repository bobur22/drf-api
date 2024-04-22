from rest_framework import serializers
from .models import AuthorModel, BookModel


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        # fields = '__all__'
        exclude = ['id']

class BookModelSerializer(serializers.ModelSerializer):
    author = AuthorModelSerializer()
    class Meta:
        model = BookModel
        # fields = '__all__'
        exclude = ['id', 'created_at']

class BookListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    page_n = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        if validated_data['page_n'] >= 100:
            return BookModel.objects.create(**validated_data)
        else:
            return serializers.ValidationError('Page number is not 100')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.page_n = validated_data.get('page_n', instance.page_n)
        instance.price = validated_data.get('price', instance.price)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance

# class BookListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookModel
#         fields = ('name', 'page_n', 'author')