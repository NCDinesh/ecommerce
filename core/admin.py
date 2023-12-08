from django.contrib import admin

from django.contrib import admin
from .models import product,newarrival

class productAdmin(admin.ModelAdmin):
    list_display=('product_company','product_name','product_description','product_price','product_img','product_rating')


admin.site.register(product)
admin.site.register(newarrival)

# Register your models here.
