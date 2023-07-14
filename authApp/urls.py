from django.urls import path
from authApp import views



urlpatterns = [


    # path('accounts/', include('allauth.urls')),
    path('api/register/',views.RegisterView.as_view(),name='register'),
    path('api/login/',views.LoginView.as_view(),name='login'),
    path('api/change_password/',views.ForgotPasswordView.as_view(),name='forgot_password'),

    path('api/profile/',views.ProfileView.as_view(),name='profile'),
    path('api/profile/<int:pk>',views.ProfileView.as_view(),name='profile_update'),
    path('api/update-address/<int:pk>',views.UpdateAddress.as_view(),name='address_update'),
    path('api/update-address/',views.UpdateAddress.as_view(),name='address_Add'),
    path('api/update-payment/',views.UserpaymentView.as_view(),name='payment_Add'),
    path('api/update-payment/<int:pk>',views.UserpaymentView.as_view(),name='payment_put_delete'),





]