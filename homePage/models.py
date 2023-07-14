from django.db import models
from authApp.models import TimeStampModel,MyUser

# Create your models here.
class ProductCategory(TimeStampModel):

    category_name=models.CharField(max_length=50)
    deleted_at=models.DateField(null=True)

    def __str__(self):
        return self.category_name
    
class ProductSubCategory(TimeStampModel):

    name=models.CharField(max_length=30)
    category_id=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    

class Product(TimeStampModel):
   
    product_name=models.CharField(max_length=30)
    category_id=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    subcategory_id=models.ForeignKey(ProductSubCategory,on_delete=models.CASCADE)
    stock=models.IntegerField()
    product_image=models.ImageField()
    product_price=models.FloatField()
    product_details=models.TextField()
    agegroup=models.CharField(max_length=30)

    def __str__(self) :
        return self.product_name
    


class UserRating(TimeStampModel):
  
    user_id=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    rating=models.IntegerField()




# -----cart Items---------------
class ShoppingSession(TimeStampModel):
  
    user_id=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    total=models.IntegerField()

  
    




class CartItem(TimeStampModel):
 
    session_id=models.ForeignKey(ShoppingSession,on_delete=models.CASCADE)
    product_id=models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()

 


class Payment(TimeStampModel):
    
    user_id=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    status=models.CharField(max_length=10)
    amount=models.FloatField()
    provider=models.CharField(max_length=20)
    payment_uid=models.CharField(max_length=50)

    def __str__(self):
        return self.status+str(self.amount)
    

class ShippingAddress(models.Model):
    user_id=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    address=models.TextField()
    landmark=models.CharField(max_length=50)
    contact=models.CharField(max_length=15)
    email=models.EmailField()


class Order(TimeStampModel):

    user_id=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product, on_delete=models.CASCADE)
    shipping_id=models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    total=models.FloatField()
    payment_id=models.ForeignKey(Payment, on_delete=models.CASCADE)
    order_status=models.CharField(max_length=20)
    order_date=models.DateTimeField(auto_now_add=True)





class Favourites(TimeStampModel):
    user_id = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)











    

     
