from django.db import models
# Create your models here.


class MyObjects(models.Model):
    name = models.CharField(max_length=10)
