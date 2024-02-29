from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class UserMessage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    line_id = models.CharField(max_length=500, null=True, blank=True)


