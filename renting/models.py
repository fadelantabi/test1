import uuid
from django.db import models
from product.models import Product
from user.models import User
class Renting(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    created_at=models.DateTimeField(
        auto_now_add=True,
        verbose_name='order_time'

        )
    updated_at=models.DateTimeField(
        auto_now=True
    )
    
    is_deleted=models.BooleanField(
        default=False
        )
    start_at=models.DateTimeField()
    end_at=models.DateTimeField()
    is_payment_done=models.BooleanField(default=False)
    user=models.ForeignKey(
        User,on_delete=models.CASCADE
    )
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.IntegerField()   
    class Meta:
        db_table = 'rent'
        verbose_name = 'rent'
        verbose_name_plural = 'rents'