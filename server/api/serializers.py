from rest_framework import serializers,exceptions
from api.models import Transaction
from django.contrib.auth.models import User

class TokenBaseSerializer(serializers.Serializer):
    user =  serializers.EmailField(min_length=7,max_length=150, write_only=True)
    
    def validate_user(self, value):
        user = None
        
        if User.objects.filter(email = value).exists():
            user = User.objects.get(email= value)
        else:
            raise exceptions.NotFound(f"Usuario '{value}' no encontrado")

        return user
        
class TokenGenerateSerializer(TokenBaseSerializer):
    expires = serializers.DateTimeField(read_only = True)
    token = serializers.RegexField("^[0-9]+$",max_length=6, read_only = True)


class TokenUsageSerializer(TokenBaseSerializer):
    token = serializers.RegexField("^[0-9]+$",max_length=6, write_only = True)
    transaction = serializers.PrimaryKeyRelatedField(queryset = Transaction.objects.all(), write_only = True)


