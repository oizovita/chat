from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Model for save chats
class NameChat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chat_name = models.CharField(max_length=20)


# Model for save color user
class UserColor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=30, default='#00000')
