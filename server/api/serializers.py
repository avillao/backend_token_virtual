from rest_framework import serializers
from api.models import Token

class TokenSerializer(serializers.ModelSerializer):
    user =  serializers.EmailField(min_length=7,max_length=150)
    expires = serializers.DateTimeField()
    token = serializers.CharField(max_length=6)

    class Meta:
        model = Token
        fields = ['user','token','expires']

