from rest_framework import serializers
from .models import CountriesModel, OrderModel, MerchantModel, OrderItemsModel, ProductsModel


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountriesModel
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        exclude = ['id', 'created_at', 'updated_at']


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchantModel
        # fields = '__all__'
        exclude = ['id', 'created_at', 'updated_at']


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemsModel
        # fields = '__all__'
        exclude = ['id', 'created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        # fields = '__all__'
        exclude = ['id', 'created_at', 'updated_at']