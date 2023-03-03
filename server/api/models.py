from django.db import models
from django.contrib.auth.models import User
from random import randint

class Token(models.model):
    token = models.CharField(max_length=128, null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    expires = models.DateTimeField(null=True)

    def save_token(self,user,raw_token):
        return

    
    def generate_token(self, user):
        token = randint(0, 999999)
        while self.model.objects.filter(user= user, token=token ).exists():
            token = randint(0, 999999)
        return f'{token:06}'
        


