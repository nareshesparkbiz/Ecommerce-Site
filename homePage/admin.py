
from django.contrib import admin
from homePage.models import *

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','category_id','subcategory_id','stock','product_image','product_price','product_details','agegroup']

admin.site.register(Product,ProductAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','deleted_at']

admin.site.register(ProductCategory,ProductCategoryAdmin)


class ProductSubCategoryAdmin(admin.ModelAdmin):
    list_display=['id','name','category_id']


admin.site.register(ProductSubCategory,ProductSubCategoryAdmin)


class UserRatingAdmin(admin.ModelAdmin):
    list_display=['id','user_id','product_id','rating']
admin.site.register(UserRating,UserRatingAdmin)



class ShoppingSessionAdmin(admin.ModelAdmin):
    list_display=['id','user_id','total']

admin.site.register(ShoppingSession,ShoppingSessionAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display=['id','session_id','product_id','quantity']

admin.site.register(CartItem,CartAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display=['id','user_id','status','amount','provider','payment_uid']

admin.site.register(Payment,PaymentAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','user_id','product_id','shipping_id','total','payment_id','order_status','order_date']

admin.site.register(Order,OrderAdmin)

class ShippingAdmin(admin.ModelAdmin):
    list_display=['id','address','landmark','contact','email']

admin.site.register(ShippingAddress,ShippingAdmin)

class FavouritesAdmin(admin.ModelAdmin):
    list_display=['id','product_id','user_id']

admin.site.register(Favourites,FavouritesAdmin)