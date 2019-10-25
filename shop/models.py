from django.db import models

# Create your models here.
class CustomerQueries(models.Model):
    query_count=models.AutoField
    name=models.CharField(max_length=100,default="")
    phone=models.CharField(max_length=13,default="")
    email=models.CharField(max_length=100,default="")
    query=models.CharField(max_length=5000,default="")
    def __str__(self):
        return self.name
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=150,default="")
    product_price=models.IntegerField(default=0)
    product_type=models.CharField(max_length=30,default="")
    product_brand=models.CharField(max_length=30,default="")
    product_sub_brand=models.CharField(max_length=30,default="")
    product_size=models.CharField(max_length=30,default="")
    product_color=models.CharField(max_length=20,default="")
    product_desc=models.TextField()
    proudct_image=models.ImageField(upload_to="shop/images")

    def __str__(self):
        return self.product_name
        
class CustomerOrder(models.Model):
    order_id=models.AutoField(primary_key=True)
    itemJson=models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    order_name=models.CharField(max_length=50)
    order_address=models.CharField(max_length=500)
    order_email=models.CharField(max_length=50,default="")
    order_phone=models.CharField(max_length=13,default="")
    order_zip=models.CharField(max_length=6,default="")
    order_city=models.CharField(max_length=50,default="")
    order_state=models.CharField(max_length=25,default="")
    
    def __str__(self):
        return self.order_name

class order_update(models.Model):
    update_id=models.AutoField(primary_key=True)
    update_order_id=models.IntegerField(default=0)
    update_desc=models.CharField(max_length=5000)
    update_time=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.update_desc[0:20]+"..."

