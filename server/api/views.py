from rest_framework.views import APIView
from rest_framework import parsers, serializers, permissions, generics, status, renderers
from api.serializers import TokenSerializer

class TokenView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class =  TokenSerializer

    