from django.contrib import admin
from django.urls import path, include
from shop.views import greetings, cats
from django.urls import path
from .views import list_items
from .views import detail_item


urlpatterns = [
    path('greetings/', greetings),
    path('facts/', cats),
    path('shop/', list_items, name='list_items'),
    path('shop/<int:pk>/', detail_item, name='detail_item'),
]
