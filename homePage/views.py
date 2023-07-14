from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView,RetrieveAPIView,GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,CreateModelMixin,DestroyModelMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Product,CartItem,ShoppingSession,ShippingAddress,UserRating,Order,ProductCategory,ProductSubCategory,Favourites
from .serializers import ProductSerializer ,CartSerializer,SessionSerializer,ShippingSerializer,PaymentSerializer,UserRatingSerializer,ProductCategorySerializer,ProductSubCategorySerializer,FavouritesSerializer,OrderSerializer
from .permissions import productPermission
 



def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None





class ListProductView(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class RetriveProductView(RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class ListCategoryView(RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def get_queryset(self):
        queryset=Product.objects.all()
        
        c_id= self.kwargs['pk']

        
        if c_id is not None:
            
            queryset = Product.objects.filter(category_id=c_id)
    
        return queryset



# -----------Admin Side----------------------

class ProductView(GenericAPIView,CreateModelMixin,UpdateModelMixin,DestroyModelMixin):
    authentication_classes=[JWTAuthentication]
    permission_classes=[productPermission]

    queryset = Product.objects.all()
    serializer_class=ProductSerializer
 
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request, *args , **kwargs):
        return self.destroy(request, *args, **kwargs)





class ListProductCategoryView(ListAPIView):
    queryset=ProductCategory.objects.all()
    serializer_class=ProductCategorySerializer

class ProductCategoryView(GenericAPIView,CreateModelMixin,UpdateModelMixin,DestroyModelMixin):
    authentication_classes=[JWTAuthentication]
    permission_classes=[productPermission]

    queryset = ProductCategory.objects.all()
    serializer_class=ProductCategorySerializer
 
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request, *args , **kwargs):
        return self.destroy(request, *args, **kwargs)


class ListProductSubCategoryView(ListAPIView):
    queryset=ProductSubCategory.objects.all()
    serializer_class=ProductSubCategorySerializer


class ProductSubCategoryView(GenericAPIView,CreateModelMixin,UpdateModelMixin,DestroyModelMixin):
    authentication_classes=[JWTAuthentication]
    permission_classes=[productPermission]

    queryset = ProductSubCategory.objects.all()
    serializer_class=ProductSubCategorySerializer
 
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request, *args , **kwargs):
        return self.destroy(request, *args, **kwargs)



# -----------------------------------------------------



# class CartItemView(GenericAPIView,ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin):

#     queryset = CartItem.objects.all()
#     serializer_class=CartSerializer
 
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
    

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self,request, *args , **kwargs):
#         return self.destroy(request, *args, **kwargs)



class CartItemView(APIView):
    authentication_classes=[JWTAuthentication]

    def get(self,request):
        try:
            cart_data=CartItem.objects.all()
            serializer=CartSerializer(cart_data,many=True)
            return Response({
                "data":serializer.data,
                "status":status.HTTP_200_OK
            })
        
        except Exception as e:
            return Response({
                "message": "Backened Api Error",
                "data":str(e),
                "status":status.HTTP_400_BAD_REQUEST
            })
     
    def post(self,request,format=None):
        try:
            userId = request.user.id if request.user else None

            if userId is not None:
                print(request.user)
              
                sessioncart=get_or_none(ShoppingSession,user_id=userId)
                print(sessioncart,"joijoijoijoi")
               

                
                if sessioncart :
                    formData=request.data 
                    formData['session_id']=sessioncart.id

                    serializer=CartSerializer(data=formData)

                    if serializer.is_valid():
                        serializer.save()

                        return Response({
                                "message":"cart Item Added Succesfully",
                                "status":status.HTTP_200_OK
                        }
                        )
                    
                    return Response({
                        "message":serializer.errors,
                        "status":status.HTTP_404_NOT_FOUND
                    })
                    
                else:
                    createData={
                        "user_id":f"{userId}",
                        "total":"0"
                    }
                  
                    serializer=SessionSerializer(data=createData)
                    if serializer.is_valid():
                        serializer.save()
                  
                    return Response({
                        "message":"Session Cart not Available",
                        "status":status.HTTP_404_NOT_FOUND
                    })
        
        except Exception as e:
               return Response({
                "message": "Backened Api Error",
                "data":e,
                "status":status.HTTP_400_BAD_REQUEST
            })

    def put(self,request,pk=None):
        try:
            cartData=get_or_none(CartItem,id=pk)

            if cartData is not  None:
                serializer=CartSerializer(cartData,data=request.data,partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        "message":"Quantity Update Successfully"
                    })
                return Response(
                    {
                        "message":serializer.errors,
                        "status":status.HTTP_400_BAD_REQUEST
                    }
                )
            return Response({
                "message": f"Id {pk} doesn't Exists",
                
                "status":status.HTTP_400_BAD_REQUEST
            })
        except Exception as e:
            return Response({
                "message": "Backened Api Error",
                "data":e,
                "status":status.HTTP_400_BAD_REQUEST
            })

    def delete(self, request,pk=None):
        try:
            cartData=get_or_none(CartItem,id=pk)

            if cartData is not None:
                cartData.delete()
                return Response({
                    "message":"Cart Item Deleted Successfully ",
                    "status":status.HTTP_200_OK
                })
            return Response({
                "message": f"Id {pk} Doesnot Exists" ,
            
                "status":status.HTTP_400_BAD_REQUEST
            })
            
        
        except Exception as e:
             return Response({
                "message": "Backened Api Error",
                "data":e,
                "status":status.HTTP_400_BAD_REQUEST
            })



class ShippingAdderess(APIView):
    authentication_classes=[JWTAuthentication]
    def get(self, request):
        try:
            userId=request.user.id

            print(userId,"sdasdasd")
            shippingData=ShippingAddress.objects.filter(user_id=userId)
            serializer=ShippingSerializer(shippingData,many=True)
            return Response({
                "data":serializer.data,
                "status":status.HTTP_200_OK
            })
        
            
        
        except Exception as e:
               return Response({
                "message": "Backened Api Error",
                "data":e,
                "status":status.HTTP_400_BAD_REQUEST
            })

    def post(self,request,format=None):
        try:
            formData=request.data 
            formData['user_id']=request.user.id

            serializer=ShippingSerializer(data=formData)
            if serializer.is_valid():
                serializer.save()
                return Response({
                "message": "Shipping Address Added Successfully",
                
                "status":status.HTTP_201_CREATED
            })

            return Response({
                "message": serializer.errors,
                
                "status":status.HTTP_400_BAD_REQUEST
            })


        except Exception as e:
               return Response({
                "message": "Backened Api Error",
                "data":e,
                "status":status.HTTP_400_BAD_REQUEST
            })

    def put(self,request,pk=None):
        try:

            shippingData=get_or_none(ShippingAddress,id=pk)

            if shippingData is not None:
                serializer=ShippingSerializer(shippingData,data=request.data,partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response({
                "message": "Shipping Address Update Succesfully",
                
                "status":status.HTTP_200_OK
                      })
                return Response({
                    "message":serializer.errors,
                    "status":status.HTTP_400_BAD_REQUEST
                })
            return Response({
                "message": f"Id {pk} doen't Exists",
                
                "status":status.HTTP_404_NOT_FOUND
            })
                    
        
        except Exception as e:
               return Response({
                "message": "Backened Api Error",
                "data":e,
                "status":status.HTTP_400_BAD_REQUEST
            })
    
    def delete(self,request,pk=None):
        try:
            shippingData=get_or_none(ShippingAddress,id=pk)

            if shippingData is not None:
                shippingData.delete()
                return Response({
                "message": "Shipping Address Deleted Succesfully",
                "status":status.HTTP_200_OK
                })
            return Response({
                "message": f"Id {pk} doen't Exists",
                
                "status":status.HTTP_404_NOT_FOUND
            })
        
        except Exception as e:
               return Response({
                "message": "Backened Api Error",
                "data":e,
                "status":status.HTTP_400_BAD_REQUEST
            })



class PaymentView(APIView):
    authentication_classes=[JWTAuthentication]

  

    def post(self,request,format=None):
        try:
            formData=request.data 
            formData['user_id']=request.user.id

            serializer=PaymentSerializer(data=formData)
            if serializer.is_valid():
                serializer.save()
                return Response({
                "message": "Payment Done Successfully",
                
                "status":status.HTTP_201_CREATED
            })

            return Response({
                "message": serializer.errors,
                
                "status":status.HTTP_400_BAD_REQUEST
            })


        except Exception as e:
               return Response({
                "message": "Backened Api Error",
                "data":e,
                "status":status.HTTP_400_BAD_REQUEST
            })



class UserRatingView(APIView):
    authentication_classes=[JWTAuthentication]
    
    def post(self,request,format=None):
        try:
            formData=request.data 
            print(formData)
            check_user=Order.objects.filter(user_id=request.user.id,product_id=formData['product_id'])
       

            if check_user :

                formData['user_id']=request.user.id
                ratingData=UserRating.objects.filter(user_id=request.user.id,product_id=formData['product_id']).first()
              


                if ratingData :
                        serializer=UserRatingSerializer(ratingData,data=formData,partial=True)

                else:
                 
                        serializer=UserRatingSerializer(data=formData)

                if serializer.is_valid():
                    serializer.save()
                    return Response({
                    "message": "User Rating Added Successfully",
                    
                    "status":status.HTTP_201_CREATED
                })

                return Response({
                    "message": serializer.errors,
                    
                    "status":status.HTTP_400_BAD_REQUEST
                })
               
            else:
                 
                 return Response(
                    {
                        "message":"You Didn't Purchase this product !",
                        "status": status.HTTP_200_OK
                    }
                )

             



        except Exception as e:
               return Response({
                "message": "Backened Api Error",
                "data":e,
                "status":status.HTTP_400_BAD_REQUEST
            })



class ListUserRating(ListAPIView):
    authentication_classes=[JWTAuthentication]

    queryset=UserRating.objects.all()
    serializer_class=UserRatingSerializer

    def get_queryset(self):
        queryset=UserRating.objects.all()
        
        c_id= self.kwargs['pk']
        print(c_id,"cid")

        
        if c_id is not None:
            
            queryset = UserRating.objects.filter(product_id=c_id)
            print(queryset,"data")
    
        return queryset







class FavouriteView(APIView):
    authentication_classes=[JWTAuthentication]

    def post(self, request):
        try:
            formData=request.data 
            userId=request.user.id 
            formData['user_id']=userId
            check_fav=Favourites.objects.filter(user_id=userId,product_id=formData['product_id'])

        
            if check_fav:
                return Response(
                    {
                        "message":"This product is already in your favourites",
                        "status": status.HTTP_200_OK
                    }
                )
            
            serializer=FavouritesSerializer(data=formData)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "User Favourites  Added Successfully",
                    
                    "status":status.HTTP_201_CREATED
                })
            return Response({
                    "message": serializer.errors,
                    
                    "status":status.HTTP_201_CREATED
                })



        
        except Exception as e:
               return Response(
                    {
                        "message":"Backened API Error",
                        "data":e,
                        "status": status.HTTP_400_BAD_REQUEST
                    }
                )

    def get(self, request):
        try:
            userId=request.user.id
            favData=Favourites.objects.filter(user_id=userId)
            serializer=FavouritesSerializer(favData,many=True)
              
            return Response(
                    {
                        "data":serializer.data,
                        "status": status.HTTP_200_OK
                    }
                )

             

        except  Exception as e:
             return Response({
                "message": "Backened Api Error",
                "data":e,
                "status":status.HTTP_400_BAD_REQUEST
            })

    def delete(self,request,pk=None):
        try:
            userId=request.user.id
            favData=Favourites.objects.filter(product_id=pk,user_id=userId).first()
        

            if favData is None:
             

                return Response({
                    "message":"Product is not in your favourites",
                    "status":status.HTTP_400_BAD_REQUEST
                })
            
        
            favData.delete()

            return Response({
                "message":"Product remove Successfully from your favourites",
                "status":status.HTTP_200_OK
            })

        
        except Exception as e:
            return Response({
                "message": "Backened Api Error",
                "data":e,
                "status":status.HTTP_400_BAD_REQUEST
            })



class OrderAdminView(GenericAPIView,ListModelMixin,UpdateModelMixin):
    authentication_classes=[JWTAuthentication]
    permission_classes=[productPermission]
    queryset=Order.objects.all()
    serializer_class=OrderSerializer




class OrderView(APIView):
    authentication_classes=[JWTAuthentication]
    def post(self, request,format=None):
        try:
            userId=request.user.id 
            formData=request.data 
            formData['user_id']=userId
          
            serializer=OrderSerializer(data=formData)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message":"Order Purchase Successfully",
                        "status":status.HTTP_200_OK
                    }

                )
            return Response({
                "message": serializer.errors,
                
                "status":status.HTTP_400_BAD_REQUEST
            })
        

            


        except Exception as e:
             return Response({
                "message": "Backened Api Error",
                "data":e,
                "status":status.HTTP_400_BAD_REQUEST
            })


    def get(self,request):
        try:
            print("er",request.user.id)
            orderData=Order.objects.filter(user_id=2)
            print("erasda",orderData)

            serializer=OrderSerializer(orderData,many=True)
            print(serializer.data)

            return Response(
                {
                    "data":serializer.data,
                    "status":status.HTTP_200_OK
                }
            )

        except Exception as e:
             return Response(
                    {
                        "message":"Backened API Error",
                        "data":str(e),
                        "status": status.HTTP_400_BAD_REQUEST
                    }
                )

    def delete(self,request,pk=None):
        try:
            orderData=get_or_none(Order,id=pk)

            if orderData is not  None:
                orderData.delete()
                return Response(
                    {
                        "message":"Order cancel Succesfully",
                        "status":status.HTTP_200_OK
                    }
                )
            return Response({
                "message":f"Id {pk} doesnot exisits",
                "status":status.HTTP_404_NOT_FOUND
            })

            

        except Exception as e:

             return Response(
                    {
                        "message":"Backened API Error",
                        "data":e,
                        "status": status.HTTP_400_BAD_REQUEST
                    }
                )







