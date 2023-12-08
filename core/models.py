from django.db import models

# Create your models here.
from django.db import models

class product(models.Model):
    product_company=models.CharField( max_length=200) 
    product_name=models.CharField( max_length=200)  
    product_description=models.TextField( )
    product_price=models.IntegerField( )
    product_rating=models.IntegerField( )
    product_img = models.FileField(upload_to="product_images/", max_length=250, null=True, default=None)
# Create your models here.

    def __str__(self):
        return self.product_name
    
class newarrival(models.Model):
    new_company=models.CharField( max_length=200) 
    new_name=models.CharField( max_length=200)  
    new_description=models.TextField( )
    new_price=models.IntegerField( )
    new_rating=models.IntegerField( )
    new_img = models.FileField(upload_to="new_images/", max_length=250, null=True, default=None)
# Create your models here.

    def __str__(self):
        return self.new_name