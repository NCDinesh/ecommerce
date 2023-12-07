from django.contrib import admin

from django.contrib import admin
from .models import product

class productAdmin(admin.ModelAdmin):
    list_display=('product_company','product_name','product_description','product_price','product_img','product_rating')
# Register your models here.
admin.site.register(product)

# Register your models here.
