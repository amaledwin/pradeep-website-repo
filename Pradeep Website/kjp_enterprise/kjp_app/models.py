from django.db import models
from django.core import validators

# Create your models here.

class AddClientsModel(models.Model):
    client_name = models.CharField(max_length=100)
    client_designation = models.CharField(max_length=100)
    client_job_location = models.CharField(max_length=100)
    client_phone_num = models.CharField(max_length=100,unique=True)
