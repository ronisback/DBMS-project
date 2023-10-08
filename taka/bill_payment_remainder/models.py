from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bill(models.Model):
    bill_name = models.CharField(max_length=100)
    payee = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    status = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return self.bill_name  