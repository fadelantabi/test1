from rest_framework import serializers
from ..models import Car_Model
from ..models import Product
from .product_serializer import ProductSerializer

class ModelSerializer(serializers.ModelSerializer):
    #products = ProductSerializer(many= True)
    class Meta:
        model= Car_Model
        fields='__all__'
    def create(self, validated_data):
        products = validated_data.pop('products')
        model = Car_Model.objects.create(**validated_data)
        for product in products:
            Product.objects.create(car_model=model, **product)
        return model