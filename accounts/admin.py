from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(CustomerMod)
admin.site.register(ProductMod)
admin.site.register(OrderMod)
admin.site.register(Tag)