from rest_framework.decorators import api_view
from rest_framework.request import Request, HttpRequest
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .models import User
from .models import Userinfo
from .serializers.review_serializer  import ReviewSerializer
from .serializers.user_serializer  import UserSerializer
from .serializers.userinfo_serializer  import UserinfoSerializer
from uuid import UUID


@api_view(['GET', 'POST','PUT','DELETE'])
def review(request: Request | HttpRequest, id: UUID = None):
    if request.method == 'GET':
        if id is None:
            query = Review.objects.all()
            serializer = ReviewSerializer(query, many=True)
            return Response(serializer.data)
        else:
            try:
                query = Review.objects.get(pk=id)
                serializer = ReviewSerializer(query)
                return Response(serializer.data)
            except Review.DoesNotExist:
                return Response(
                     data={"message": "this Review does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
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
                query = Review.objects.get(pk=id)
                serializer = ReviewSerializer(instance=query,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data= serializer.data)
                return Response(serializer.data)
            except Review.DoesNotExist:
                return Response(
                     data={"message": "this Review does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    else:
            try:
                query = Review.objects.get(pk=id)
                query.is_deleted=True
                query.save()
                return Response({
                     "message":"successfully deleted"
                })
            except Review.DoesNotExist:
                return Response(
                     data={"message": "this Review does not exist"},
                     status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST','PUT','DELETE'])
def user(request: Request | HttpRequest, id: UUID = None):
    if request.method == 'GET':
        if id is None:
            query = User.objects.all()
            serializer = UserSerializer(query, many=True)
            return Response(serializer.data)
        else:
            try:
                query = User.objects.get(pk=id)
                serializer = UserSerializer(query)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response(
                     data={"message": "this User does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
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
                query = User.objects.get(pk=id)
                serializer = UserSerializer(instance=query,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data= serializer.data)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response(
                     data={"message": "this User does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    else:
            try:
                query = User.objects.get(pk=id)
                query.is_deleted=True
                query.save()
                return Response({
                     "message":"successfully deleted"
                })
            except User.DoesNotExist:
                return Response(
                     data={"message": "this User does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
            
@api_view(['GET', 'POST','PUT','DELETE'])
def userinfo(request: Request | HttpRequest, id: UUID = None):
    if request.method == 'GET':
        if id is None:
            query = Userinfo.objects.all()
            serializer = UserinfoSerializer(query, many=True)
            return Response(serializer.data)
        else:
            try:
                query = Userinfo.objects.get(pk=id)
                serializer = UserinfoSerializer(query)
                return Response(serializer.data)
            except Userinfo.DoesNotExist:
                return Response(
                     data={"message": "this Userinfo does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = UserinfoSerializer(data=request.data)
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
                query = Userinfo.objects.get(pk=id)
                serializer = UserinfoSerializer(instance=query,data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(data= serializer.data)
                return Response(serializer.data)
            except Userinfo.DoesNotExist:
                return Response(
                     data={"message": "this Userinfo does not exist"},
                     status=status.HTTP_404_NOT_FOUND)
    else:
            try:
                query = Userinfo.objects.get(pk=id)
                query.is_deleted=True
                query.save()
                return Response({
                     "message":"successfully deleted"
                })
            except Userinfo.DoesNotExist:
                return Response(
                     data={"message": "this Userinfo does not exist"},
                     status=status.HTTP_404_NOT_FOUND)


