from django.utils import timezone

# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models
from django.db.models import ForeignKey
from django.contrib.auth import get_user_model

User = get_user_model()

# class CustomUserManager(UserManager):
#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('You must provide a valid email address')
#
#         email = self.normalize_email(email).lower()
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#     def create_user(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', True)
#         return self._create_user(email, password, **extra_fields)

class CountriesModel(models.Model):
    name = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.country_name}'

    class Meta:
        db_table = 'countries'
        verbose_name = 'country'
        verbose_name_plural = 'countries'


# class User(AbstractBaseUser, PermissionsMixin):
#
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#
#     full_name = models.CharField(max_length=100)
#     email = models.EmailField(blank=True, unique=True, default='')
#     gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
#     date_of_birth = models.DateField()
#     # country_code = ForeignKey(CountriesModel, on_delete=models.CASCADE, related_name='countrycode')
#
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#
#     date_joined = models.DateTimeField(default=timezone.now)
#     last_login = models.DateTimeField(blank=True, null=True)
#
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = ['full_name', 'email', 'gender', 'date_of_birth']
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f'{self.full_name}'
#
#     class Meta:
#         db_table = 'users'
#         verbose_name = 'user'
#         verbose_name_plural = 'users'
#
#     def get_full_name(self):
#         return self.full_name
#
#     def get_short_name(self):
#         return self.full_name or self.email.split('@')[0]

class User(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, unique=True, default='')
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    country_code = ForeignKey(CountriesModel, on_delete=models.CASCADE, related_name='country_code')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'

class OrderModel(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.status}'

    class Meta:
        db_table = 'orders'
        verbose_name = 'order'
        verbose_name_plural = 'orders'


class MerchantModel(models.Model):
    merchant_name = models.CharField(max_length=100)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_id')
    country_code = models.ForeignKey(CountriesModel, on_delete=models.CASCADE, related_name='merchant_ccode')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.merchant_name}'

    class Meta:
        db_table = 'merchants'
        verbose_name = 'merchant'
        verbose_name_plural = 'merchants'


class ProductsModel(models.Model):
    merchant_id = models.ForeignKey(MerchantModel, on_delete=models.CASCADE, related_name='merchant_id')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'


class OrderItemsModel(models.Model):
    order_id = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='order_id')
    product_id = models.ForeignKey(ProductsModel, on_delete=models.CASCADE, related_name='product_id')
    quantity = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quantity}'

    class Meta:
        db_table = 'order_items'
        verbose_name = 'order_item'
        verbose_name_plural = 'order_items'
