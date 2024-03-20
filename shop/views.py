import requests
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from shop.models import Item
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Item, Purchase


def greetings(requests):
    return HttpResponse('Добро пожаловать в наш магазин!')

def cats(requests):
    API = 'https://catfact.ninja/fact'
    return HttpResponseRedirect(API)


def list_items(request):
    items = Item.objects.all()
    return render(request, 'list_items.html', {'items': items})


def detail_item(request, pk, *args, **kwargs):
    item = get_object_or_404(Item, pk=pk)  # Получаем товар по ID
    purchases = Purchase.objects.filter(item=item)  # Получаем все покупки этого товара
    return render(request, 'detail_item.html', {'item': item, 'purchase': purchases})
