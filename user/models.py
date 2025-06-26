from django.db import models
import uuid
from product.models import Product
class User(models.Model):
    id=models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    first_name=models.CharField(
        max_length=255
    )
    last_name=models.CharField(
        max_length=255
    )
    email= models.EmailField(
        max_length=255,
          null=True,
          unique=True
        )
    phone_number=models.CharField(
        max_length=13
        )
    created_at=models.DateTimeField(
        auto_now_add=True
        )
    updated_at=models.DateTimeField(
        auto_now=True
    )
    is_deleted=models.BooleanField(
        default=False
        )
    class Meta:
        db_table="user"
        unique_together=[
            ('first_name',
             'last_name'
             )
        ]
        verbose_name='user'
        verbose_name_plural='users'
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Userinfo(models.Model):
    id=models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    created_at=models.DateTimeField(
        auto_now_add=True
        )
    updated_at=models.DateTimeField(
        auto_now=True
    )
    is_deleted=models.BooleanField(
        default=False
        )
    address=models.TextField(
        blank=True,
        verbose_name="home address"
    )
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    birthdate=models.DateField(null=True)
    is_maried=models.BooleanField(default=False)
    class Meta:
        db_table="user_info"
        verbose_name='user_info'
        verbose_name_plural='user_info'
class Review(models.Model):
    id=models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    created_at=models.DateTimeField(
        auto_now_add=True
        )
    updated_at=models.DateTimeField(
        auto_now=True
    )
    is_deleted=models.BooleanField(
        default=False
        )
    review=models.TextField(
        blank=True,
    )
    rating=models.IntegerField(
    null=True
    )
    user=models.ForeignKey(
        User,on_delete=models.CASCADE
    )
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    is_positive=models.BooleanField(default=True)
    class Meta:
        db_table="user_review"
        verbose_name='user_review'
        verbose_name_plural='user_reviews'