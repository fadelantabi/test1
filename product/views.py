from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

from rest_framework.request import Request, HttpRequest
from rest_framework.response import Response
from rest_framework import status

from .models import Color
from .models import Car_Model
from .models import Product
from .serializers.color_serializer  import ColorSerializer
from .serializers.model_serializer  import ModelSerializer
from .serializers.product_serializer  import ProductSerializer
from uuid import UUID

from django.db.models import Q


@api_view(['GET', 'POST','PUT','DELETE'])
def color(request: Request | HttpRequest, id: UUID = None):
    if request.method == 'GET':
        if id is None:
            query = Color.objects.all()
            serializer = ColorSerializer(query, many=True)
            return Response(serializer.data)
        else:
            try:
                query = Color.objects.get(pk=id)
                serializer = ColorSerializer(query)
                return Response(serializer.data)
            except Color.DoesNotExist:
                return Response(
                     data={"message": "this Color does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = ColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == 'PUT':
            try:
                query = Color.objects.get(pk=id)
                serializer = ColorSerializer(instance=query,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data= serializer.data)
                return Response(serializer.data)
            except Color.DoesNotExist:
                return Response(
                     data={"message": "this Color does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    else:
            try:
                query = Color.objects.get(pk=id)
                query.is_deleted=True
                query.save()
                return Response({
                     "message":"successfully deleted"
                })
            except Color.DoesNotExist:
                return Response(
                     data={"message": "this Color does not exist"},
                     status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST','PUT','DELETE'])
def model(request: Request | HttpRequest, id: UUID = None):
    if request.method == 'GET':
        if id is None:
            query = Car_Model.objects.all()
            serializer = ModelSerializer(query, many=True)
            return Response(serializer.data)
        else:
            try:
                query = Car_Model.objects.get(pk=id)
                serializer = ModelSerializer(query)
                return Response(serializer.data)
            except Car_Model.DoesNotExist:
                return Response(
                     data={"message": "this Model does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = ModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == 'PUT':
            try:
                query = Car_Model.objects.get(pk=id)
                serializer = ModelSerializer(instance=query,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data= serializer.data)
                return Response(serializer.data)
            except Car_Model.DoesNotExist:
                return Response(
                     data={"message": "this Model does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    else:
            try:
                query = Car_Model.objects.get(pk=id)
                query.is_deleted=True
                query.save()
                return Response({
                     "message":"successfully deleted"
                })
            except Car_Model.DoesNotExist:
                return Response(
                     data={"message": "this Model does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
            
@api_view(['GET', 'POST','PUT','DELETE'])   
def product(request: Request | HttpRequest, id: UUID = None):
    
    if request.method == 'GET':
        if request.version == '2.0':
             return Response({
                  "statuse": "i am version 2"
             })
        if id is None:
            query = Product.objects.all()
            print(query.query)
            serializer = ProductSerializer(query, many=True)
            return Response(serializer.data)
        else:
            try:
                query = Product.objects.get(pk=id)
                serializer = ProductSerializer(query)
                return Response(serializer.data)
            except Product.DoesNotExist:
                return Response(
                     data={"message": "this Product does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == 'PUT':
            try:
                query = Product.objects.get(pk=id)
                serializer = ProductSerializer(instance=query,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data= serializer.data)
                return Response(serializer.data)
            except Product.DoesNotExist:
                return Response(
                     data={"message": "this Product does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    else:
            try:
                query = Product.objects.get(pk=id)
                query.is_deleted=True
                query.save()
                return Response({
                     "message":"successfully deleted"
                })
            except Product.DoesNotExist:
                return Response(
                     data={"message": "this Product does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
            
@api_view(['GET'])
def filterApi(request:HttpRequest|Request)->Response:
     query= Product.objects.filter(
     ).order_by('-price')

     print(query.query)

     #serializer= ModelSerializer(query, many= True)
     serializer= ProductSerializer(query, many= True)


     return Response(serializer.data)


