from rest_framework import serializers
from .models import Product,ProductCategory,ProductSubCategory,CartItem,ShoppingSession,ShippingAddress,Payment,UserRating,Favourites,Order



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductCategory
        fields='__all__'


class ProductSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductSubCategory
        fields='__all__'







class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields='__all__'

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShoppingSession
        fields='__all__'


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShippingAddress
        fields='__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'





class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserRating
        fields='__all__'





class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favourites
        fields='__all__'



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'





