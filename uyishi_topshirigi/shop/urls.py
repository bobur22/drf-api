from django.urls import path
from .views import *


urlpatterns = [
    path('country/', CountryList.as_view()),
    path('product/', ProductList.as_view()),
    path('order/', OrderList.as_view()),
    path('merchant/', MerchantList.as_view()),
    path('order_list/', OrderItemList.as_view()),
]