from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Categories(models.Model):
    name=models.CharField(max_length=250)


    def __str__(self):
        return self.name


class Filter_Price(models.Model):
    filter_price=(
        ('100 to 1000','100 to 1000'),
        ('1000 to 2000','1000 to 2000'),
        ('2000 to 3000','2000 to 3000'),
        ('3000 to 4000','3000 to 4000'),
        ('4000 to 5000','4000 to 5000'),
    )
    price=models.CharField(choices=filter_price,max_length=200)

    
    def __str__(self):
        return self.price


class Product(models.Model):
    CONDITION=(('new','new'),('old','old'))
    STOCK=(('in stock','in stock'),('out stock','out stock'))
    STATUS=(('published','published'),('draft','draft'))

    
    unique_id=models.CharField(unique=True,max_length=250,null=True,blank=True)
    image=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    condition=models.CharField(choices=CONDITION,max_length=250)
    information=models.TextField()
    description=models.TextField()
    stock=models.CharField(choices=STOCK,max_length=200)
    status=models.CharField(choices=STATUS,max_length=250)
    created_date=models.DateTimeField(default=timezone.now)



    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)
    filter_price=models.ForeignKey(Filter_Price,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args, **kwargs)
    
class Images(models.Model):
    image=models.ImageField(upload_to='img')
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)

class Tag(models.Model):
    name=models.CharField(max_length=250)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)

class Contact(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=250)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    country=models.CharField(max_length=250)
    address=models.TextField()
    city=models.CharField(max_length=250)
    state=models.CharField(max_length=250)
    postcode=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField(max_length=250)
    amount=models.CharField(max_length=250)
    payment_id=models.CharField(max_length=200,null=True,blank=True)
    paid=models.BooleanField(default=False,null=True)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.CharField(max_length=250)
    Images=models.ImageField(upload_to='orderimg')
    quantity=models.CharField(max_length=250)
    price=models.CharField(max_length=50)
    total=models.CharField(max_length=50)

    def __str__(self):
        return self.order.user.username



       
# Create your models here.
