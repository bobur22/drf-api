from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from shop.models import CountriesModel, ProductsModel, OrderModel, OrderItemsModel, MerchantModel
from .serializers import CountrySerializer, ProductSerializer, OrderSerializer, OrderItemsSerializer, MerchantSerializer


class CountryList(generics.ListCreateAPIView):
    queryset = CountriesModel.objects.all()
    serializer_class = CountrySerializer


class ProductList(generics.ListCreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer


class MerchantList(generics.ListCreateAPIView):
    queryset = MerchantModel.objects.all()
    serializer_class = MerchantSerializer


class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItemsModel.objects.all()
    serializer_class = OrderItemsSerializer
