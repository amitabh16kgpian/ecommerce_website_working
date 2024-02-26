from django.contrib import admin
from .models import Product, Customer, Order, Catergory
# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Catergory)
admin.site.register(Order)