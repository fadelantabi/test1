from rest_framework.decorators import api_view
from rest_framework.request import Request, HttpRequest
from rest_framework.response import Response
from rest_framework import status
from .models import Renting
from .serializers import RentingSerializer
from uuid import UUID


@api_view(['GET', 'POST','PUT','DELETE'])
def renting(request: Request | HttpRequest, id: UUID = None):
    if request.method == 'GET':
        if id is None:
            query = Renting.objects.all()
            serializer = RentingSerializer(query, many=True)
            return Response(serializer.data)
        else:
            try:
                query = Renting.objects.get(pk=id)
                serializer = RentingSerializer(query)
                return Response(serializer.data)
            except Renting.DoesNotExist:
                return Response(
                     data={"message": "this Renting does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = RentingSerializer(data=request.data)
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
                query = Renting.objects.get(pk=id)
                serializer = RentingSerializer(instance=query,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data= serializer.data)
                return Response(serializer.data)
            except Renting.DoesNotExist:
                return Response(
                     data={"message": "this Renting does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    else:
            try:
                query = Renting.objects.get(pk=id)
                query.is_deleted=True
                query.save()
                return Response({
                     "message":"successfully deleted"
                })
            except Renting.DoesNotExist:
                return Response(
                     data={"message": "this Renting does not exist"},
                     status=status.HTTP_404_NOT_FOUND)