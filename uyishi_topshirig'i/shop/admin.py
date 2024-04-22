from django.contrib import admin
from .models import *
admin.site.register(User)
admin.site.register(CountriesModel)
admin.site.register(OrderModel)
admin.site.register(MerchantModel)
admin.site.register(OrderItemsModel)
admin.site.register(ProductsModel)

