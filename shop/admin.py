from django.contrib import admin
from shop.models import Item, Client, Purchase
# Register your models here.
admin.site.register(Item)
admin.site.register(Client)
admin.site.register(Purchase)