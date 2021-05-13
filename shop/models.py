from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default="")
    description = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=300)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.IntegerField(default="")
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zip_code = models.IntegerField(default="")

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_description = models.CharField(max_length=1000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_description[0:7] + "..."

