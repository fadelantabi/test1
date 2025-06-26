from rest_framework.decorators import api_view
from rest_framework.request import Request, HttpRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username= serializers.CharField(max_length= 250)
    password= serializers.CharField(max_length= 250)



@api_view(['POST'])
def login(request:Request|HttpRequest)->Response:

    ser = LoginSerializer(data= request.data)
    if ser.is_valid(raise_exception= True):
        user = authenticate(
            username= ser.validated_data['username'],
            password= ser.validated_data['password']
        )

        if user:

            token= Token.objects.create(user= user)
            return Response({
                "token": token.key,
                'user': user.username
            })
        
        return Response({
            'status': 'fail'
        })