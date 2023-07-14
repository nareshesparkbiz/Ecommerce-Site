from django.urls import path
from homePage import views


urlpatterns = [

    # --------Products Api ---------------------
    path('api/products/',views.ListProductView.as_view(),name="AllProducts"),
    path('api/products/<int:pk>',views.RetriveProductView.as_view(),name="Product"),


    path('api/products/category/<int:pk>',views.ListCategoryView.as_view(),name="Product_category"),

# ---------------Products categories Api---------------------

    path('api/category-list/',views.ListProductCategoryView.as_view(),name="category-list"),
    path('api/category/',views.ProductCategoryView.as_view(),name="category_Add"),
    path('api/category/<int:pk>',views.ProductCategoryView.as_view(),name="category_Put_delete"),

    
# ---------------Products SubCategories Api---------------------

    path('api/sub-category-list/',views.ListProductSubCategoryView.as_view(),name="subcategory-list"),
    path('api/categories/sub-category/',views.ProductSubCategoryView.as_view(),name="sub-category_add"),
    path('api/categories/sub-category/<int:pk>',views.ProductSubCategoryView.as_view(),name="sub-category_put_delete"),


# ---------------Products Admin Side Api---------------------
    
    path('api/all-products/',views.ProductView.as_view(),name="Products"),
    path('api/all-products/<int:pk>',views.ProductView.as_view(),name="Products")
    
    
    ,

# ---------------Cart items  Api---------------------

    path('api/cart-items/',views.CartItemView.as_view(),name="cart"),
    path('api/cart-items/<int:pk>',views.CartItemView.as_view(),name="cart"),


# ---------------Shipping Address Api---------------------


    path('api/shipping-address/',views.ShippingAdderess.as_view(),name="shipping-address"),
    path('api/shipping-address/<int:pk>',views.ShippingAdderess.as_view(),name="shipping-address"),



# ---------------Products Payment  Api---------------------


    path('api/order/order-payment/',views.PaymentView.as_view(),name="order-payment"),


# ---------------Products rating  Api---------------------


    path('api/products/product-rating/',views.UserRatingView.as_view(),name="user-rating"),
    path('api/products/product-rating/listing/<int:pk>',views.ListUserRating.as_view(),name="userlist-rating"),



# ------------Favourites API---------------------
    path('api/products/favourites/',views.FavouriteView.as_view(),name="product-favourites"),
    path('api/products/favourites/<int:pk>',views.FavouriteView.as_view(),name="product-favourites-delete"),


# ------------Order APi----------

    path('api/products/order-product/',views.OrderView.as_view(),name="order-product"),
    path('api/products/order-product/<int:pk>',views.OrderView.as_view(),name="cancel-order"),

    path('api/admin/order-list/',views.OrderAdminView.as_view(),name="admin-order-list"),
    path('api/admin/order-list/<int:pk>',views.OrderAdminView.as_view(),name="admin-order-list-update"),


















]