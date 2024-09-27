from django.db import models

class MainMenu(models.Model):
    sku = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    price = models.FloatField(max_digits=20, decimal_places=2, default=float(0.00))
    qty = models.IntegerField(max_length=5)
    status = models.SmallIntegerField(max_length=5)
