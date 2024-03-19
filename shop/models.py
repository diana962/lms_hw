from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}: {self.price}'

self
class Client(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    date_purchase = models.DateField()

    def __str__(self):
        return f'{self.name}'

