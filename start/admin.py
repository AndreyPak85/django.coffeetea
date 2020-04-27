from django.contrib import admin
from start.models import Coffee, Brand, Tea, Order

# Register your models here.

admin.site.register(Coffee)
admin.site.register(Brand)
admin.site.register(Tea)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_name', 'name', 'phone', "date"]

