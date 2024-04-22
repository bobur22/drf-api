from django.shortcuts import render
from drf_yasg.openapi import Response
from rest_framework import status, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, \
    RetrieveUpdateDestroyAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateAPIView
from .models import SponsorModel, UniversitiesModel, StudentModel, SponsorStudentModel, Overall
from .serializers import SponsorSerializer, UniversitySerializer, StudentSerializer, StudentAddSponsorSerializer, \
    StudentCreateSerializer, SponsorCreateSerializer, OverallSerializer, StudentsSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter


# class StudentCustomOrderFilter(OrderingFilter):
#     allowed_custom_filters = ['event', 'payment_q', 'created_at']
    # fields_related = {
    #     'user_city': 'user__city__name', # ForeignKey Field lookup for ordering
    #     'user_country': 'user__country__name'
    # }
    # def get_ordering(self, request, queryset, view):
    #     params = request.query_params.get(self.ordering_param)
    #     if params:
    #         fields = [param.strip() for param in params.split(',')]
    #         ordering = [f for f in fields if f.lstrip('-') in self.allowed_custom_filters]
    #         if ordering:
    #             return ordering
    #
    #     return self.get_default_ordering(view)
    #
    # def filter_queryset(self, request, queryset, view):
    #     order_fields = []
    #     ordering = self.get_ordering(request, queryset, view)
    #     if ordering:
    #         for field in ordering:
    #             symbol = "-" if "-" in field else ""
    #             order_fields.append(symbol+self.fields_related[field.lstrip('-')])
    #     if order_fields:
    #         return queryset.order_by(*order_fields)
    #
    #     return queryset


class SponsorCreate(generics.CreateAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorCreateSerializer


class SponsorModelGenerics(ListAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'full_name', 'phone_n']
    ordering_fields = ['event', 'payment_q', 'created_at']
    ordering = ['full_name']
    # permission_classes = [IsAdminUser]


class SponsorDetailGenerics(RetrieveUpdateDestroyAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer
    http_method_names = ['get', 'put', 'delete', 'head', 'options']
    # permission_classes = [IsAdminUser]


class UniversityModelViewSet(ModelViewSet):
    queryset = UniversitiesModel.objects.all()
    serializer_class = UniversitySerializer
    # permission_classes = [IsAdminUser]


class StudentModelGenerics(ListAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentsSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['full_name', 'email', 'contract_q']
    ordering_fields = ['degree', 'university']
    # permission_classes = [IsAdminUser]


class StudentCreateModelGenerics(CreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentCreateSerializer
    # permission_classes = [IsAdminUser]


class StudentUpdateModelGenerics(RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get', 'put', 'delete', 'head', 'options']
    # permission_classes = [IsAdminUser]


class StudentAddSponsorModelGenerics(CreateAPIView):
    queryset = SponsorStudentModel.objects.all()
    serializer_class = StudentAddSponsorSerializer

class StudentSponsorView(ListAPIView):
    queryset = Overall.objects.all()
    serializer_class = OverallSerializer

    # @api_view(['POST'])
    # def endpoint(request):
    #     if request.method == 'POST':
    #         # AttributeError: This QueryDict instance is immutable
    #         # request.data['object_value'] = int(request.data['object_value']) / 100.0
    #         serializer = (data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def money_checker(request):
#     serializer = StudentAddSponsorSerializer(data=request.data)
#
#     if request.data['given_q'] > request.data['payment_q']:
#         upmoney = request.data['given_q'] - request.data['payment_q']
#         print(upmoney)
#         raise ValidationError(
#             f'You are using too much money in this {sponsor} have only {payment_q} so you can use up to {upmoney}')
#         return Response({'status': 403, 'message': f'You are using too much money in this {request.data['sponsor']} have only {request.data['payment_q']} so you can use up to {upmoney}'})
#
#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response(
#             {'status': 403, 'errors': serializer.errors, 'message': 'Not enough money'}
#         )
#
#     serializer.save()
#     return Response(
#             {'status': 200, 'payload': serializer.data, 'message': 'Not enough money'}
#         )
