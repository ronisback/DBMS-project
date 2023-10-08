from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget

# Create your models here.

class Incomes(models.Model):
    date = models.DateField(default=now)
    description = models.TextField()
    amount = models.FloatField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category =  models.CharField(max_length=266)

    def __str__(self):
        return self.amount

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Income(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return self.category   
    