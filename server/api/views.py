from rest_framework.views import APIView
from rest_framework import parsers, serializers, permissions, generics, status, renderers
from api.serializers import TokenSerializer
from api.models import Token
from collections import OrderedDict
from rest_framework.response import Response
from django.contrib.auth.models import User

class TokenView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = (parsers.JSONParser,)

    def get(self, request):
        serializer = TokenSerializer(data = request.GET)
        
        if serializer.is_valid(raise_exception=True):

            authToken, expires = Token.objects.get_or_create(serializer.validated_data['user'])
            response = {
                "auth_token" : authToken,
                "expires": expires
            }

            return Response(response)