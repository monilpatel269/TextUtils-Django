from django.db import models
from django.conf import settings

class ContactUs(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)