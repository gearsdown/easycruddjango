from django.db import models

class MainMenu(models.Model):
    sku = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    qty = models.IntegerField()
    status = models.SmallIntegerField()
    class Meta:
            db_table = 'mainmenu'