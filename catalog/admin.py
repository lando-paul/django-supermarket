from django.contrib import admin
from .models import Item, Order, OrderItem


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title')}
    list_display = [
        'title',
        'price',
        'discount price'
    ]
    

# Register your models here.
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)