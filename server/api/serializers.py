from rest_framework import serializers,exceptions
from api.models import Token
from django.contrib.auth.models import User

class TokenSerializer(serializers.Serializer):
    user =  serializers.EmailField(min_length=7,max_length=150, write_only=True)
    expires = serializers.DateTimeField(read_only = True)
    token = serializers.RegexField("^[0-9]+$",max_length=6, required= False)

    def validate(self, attrs):
        user = None
        
        if User.objects.filter(email = attrs['user']).exists():
            user = User.objects.get(email=attrs['user'])
        else:
            raise exceptions.NotFound("Usuario no encontrado")
        
        attrs['user'] = user

        return attrs


