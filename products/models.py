from django.db import models

class product(models.Model):
    product_company=models.CharField( max_length=200) 
    product_name=models.CharField( max_length=200)  
    product_description=models.TextField( )
    product_price=models.IntegerField( )
    product_rating=models.IntegerField( )
    prouduct_img = models.ImageField(upload_to='product_images', default="blank.png",height_field=None, width_field=None, max_length=None)
# Create your models here.

    def __str__(self):
        return self.product_name