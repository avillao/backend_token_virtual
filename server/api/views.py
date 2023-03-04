from rest_framework.views import APIView
from rest_framework import parsers, permissions, status
from api.serializers import TokenUsageSerializer, TokenGenerateSerializer
from api.models import Token
from collections import OrderedDict
from rest_framework.response import Response
from django.contrib.auth.models import User

class GenerateTokenView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = (parsers.JSONParser,)

    def get(self, request):
        serializer = TokenGenerateSerializer(data = request.GET)
        
        if serializer.is_valid(raise_exception=True):

            authToken, expires = Token.objects.get_or_create(serializer.validated_data['user'])
            response = {
                "auth_token" : authToken,
                "expires": expires
            }

            return Response(response)
            

class UsageTokenView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = (parsers.JSONParser,)

    def post(self, request):
        serializer = TokenUsageSerializer(data = request.GET)
        
        if serializer.is_valid(raise_exception=True):
            user  = serializer.validated_data.get('user')
            token = Token.objects.filter(user = user, transaction = None)
            transaction = serializer.validated_data.get('transaction')

            if not token.exists():
                return Response({"detail":"Token no valido"},status=status.HTTP_400_BAD_REQUEST)
            
            token = token.get()
            if not token.is_valid() or not token.validate_token(serializer.validated_data.get('token')):
                return Response({"detail":"Token no válido"},status=status.HTTP_400_BAD_REQUEST)
            
            token.transaction = transaction
            token.save()

            return Response({"detail":f"Token válido para transacción de tipo '{transaction.name}'" })