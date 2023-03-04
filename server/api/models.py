from django.db import models
from django.contrib.auth.models import User
from random import randint
from rest_framework.authtoken.models import Token
from django.utils import timezone
from datetime import timedelta

class Transaction(models.Model):
    name = models.CharField(max_length=250, null=True)

class TokenManager(models.Manager):
    
    def _get_or_create(self, user, instance = None):
        
        auth_token = randint(0, 999999)
        auth_token = f'{auth_token:06}'

        while Token.objects.filter(user = user, token = auth_token).exists():
            auth_token = randint(0, 999999)
            auth_token = f'{auth_token:06}'
    
        expires = timezone.now() + timedelta(seconds=60)

        if instance is None:
            Token.objects.create(
                user = user, 
                token = auth_token,
                expires = expires
            )

        else:
            instance.token = auth_token
            instance.expires = expires
            instance.save()

        return auth_token, expires
    
    
    def get_or_create(self, user):
        token:Token = None
        auth_token = None
        expires = None

        query = Token.objects.filter(user = user, transaction = None)
        
        if query.exists():
            token = query.get()
            auth_token = token.token
            expires = token.expires
        
        if token is not None and not token.is_valid():
            auth_token, expires = Token.objects._get_or_create(user, token)
        
        if not query.exists() :
            auth_token, expires = Token.objects._get_or_create(user)
            
        
        return auth_token, expires

class Token(models.Model):
    token = models.CharField(max_length=6, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    expires = models.DateTimeField(null=True)
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE, null = True)

    objects = TokenManager()

    def is_valid(self):
        
        if self.token is None:
            return False
        
        if self.expires is None or timezone.now() >= self.expires:
            return False
        
        return True
    
    def validate_token(self, token):
        if not self.is_valid():
            return False

        return self.token == token





        

        

        

        


    

        


