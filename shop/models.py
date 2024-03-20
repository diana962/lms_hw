from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}'

class Client(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    date_purchase = models.DateField()

    def __str__(self):
        return f'{self.name}'

class Purchase(models.Model):
    # buyer = models.OneToOneField(Client, on_delete=models.CASCADE)
    # quantity = models.IntegerField()
    # date = models.DateField()
    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name='purchases')
    item = models.ForeignKey(Item,on_delete=models.CASCADE,related_name='purchases')
