from django.contrib import admin
from .models import itemcatalog
from .models import orderhistory


# Register your models here.
admin.site.register(itemcatalog)
admin.site.register(orderhistory)
