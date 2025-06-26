import uuid
from django.db import models
class Car_Model(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    manufacturer = models.CharField(
        max_length=255
        )
    name = models.CharField(max_length=255)
    year = models.DateField()
    created_at=models.DateTimeField(
        auto_now_add=True
        )
    specs = models.TextField(
        blank=True
    )
    img=models.ImageField(
        null=True,
        upload_to='imgs/car_model',
        max_length=500
    )
    updated_at=models.DateTimeField(
        auto_now=True
     )
    is_deleted=models.BooleanField(
        default=False
        )
    #products = list()
    class Meta:
        db_table = 'model'
        verbose_name = 'model'
        verbose_name_plural = 'models'

class Color(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=255)
    created_at=models.DateTimeField(
        auto_now_add=True
        )
    red_value=models.IntegerField(default=0)
    green_value=models.IntegerField(default=0)
    blue_value=models.IntegerField(default=0)
    updated_at=models.DateTimeField(
        auto_now=True
     )
    is_deleted=models.BooleanField(
        default=False
        )
    class Meta:
        db_table = 'color'
        verbose_name = 'color'
        verbose_name_plural = 'colors'

class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    license_plate = models.CharField(max_length=30)
    color = models.ForeignKey(
        Color,
        on_delete=models.SET_NULL,
        null=True
    )
    features = models.TextField(blank=True)
    is_new=models.BooleanField(default=True)
    current_kilometer = models.IntegerField(default=0)
    created_at=models.DateTimeField(
        auto_now_add=True
        )
    engine = models.IntegerField(null =True)

    updated_at=models.DateTimeField(
        auto_now=True
     )
    is_deleted=models.BooleanField(
        default=False
        )
    car_model = models.ForeignKey(
        Car_Model,
        on_delete=models.SET_NULL,
        null=True,
        default= None,
        related_name= 'products',
        related_query_name= 'product'
  )
    price=models.IntegerField(
        )
    rent_per_day = models.IntegerField(
    )
    is_rented=models.BooleanField(default=False)
    is_sold=models.BooleanField(default=False)
    rent_per_week =models.IntegerField()
    rent_per_month=models.IntegerField()
    img=models.ImageField(
        upload_to='imgs/product',
        max_length=500,
        null= True,
        default= None
        )
    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'        