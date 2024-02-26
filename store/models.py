from django.db import models
import datetime

# Create your models here.
class Catergory(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name =  models.CharField(max_length = 50)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):
    name = models.CharField(max_length = 50)
    price = models.DecimalField(default = 0 , decimal_places = 2, max_digits = 6)
    category = models.ForeignKey(Catergory, on_delete = models.CASCADE, default =1)
    description = models.CharField(max_length = 500, default ='', blank = True, null = True)
    image = models.ImageField(upload_to = 'upload/product/')

    # adding sale logic
    on_sale = models.BooleanField(default = False)
    sale_price = models.DecimalField(default = 0, decimal_places  =2, max_digits = 6)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    address = models.CharField(max_length = 200, default = '',blank = True)
    quatity = models.IntegerField(default = 1)
    phone = models.CharField(max_length = 13, default= '')
    date = models.DateField(default = datetime.datetime.today)
    status = models.BooleanField(default = False)
