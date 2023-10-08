from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Debt(models.Model):
    debtor = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return self.debtor