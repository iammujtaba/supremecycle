from django.contrib import admin
from .models import CustomerQueries,Product,CustomerOrder,order_update
# Register your models here.
admin.site.register(CustomerQueries)
admin.site.register(Product)
admin.site.register(CustomerOrder)
admin.site.register(order_update)
