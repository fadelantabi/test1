import uuid
from django.db import models
from purchase.models import Purchase
from renting.models import Renting
class Currency(models.Model):
    id=models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
        )
    name=models.CharField(
        max_length=255
        )
    value_to_syrianpound=models.DecimalField(
        max_digits=8,
        decimal_places=4
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
        db_table = 'currency'
        verbose_name = 'currency'
        verbose_name_plural = 'currencies'    
class Payment(models.Model):
    id = models.UUIDField(
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
    renting=models.ForeignKey(
        Renting,
        on_delete=models.SET_NULL,
        null=True
        )
    purchase=models.ForeignKey(
        Purchase,
        on_delete=models.SET_NULL,
        null=True
        )
    amount=models.IntegerField()
    currency=models.ForeignKey(Currency,on_delete=models.CASCADE)
    class Meta:
        db_table = 'payment'
        verbose_name = 'payment'
        verbose_name_plural = 'payments'