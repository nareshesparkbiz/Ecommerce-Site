from django.contrib import admin
from authApp.models import MyUser,UserAddress,UserPayment
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin





# Register your models here.

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
   

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "firstname","lastname", "is_admin","contact","profile_img","last_login"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["firstname", "lastname"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "firstname","lastname", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)


class UserAddAdmin(admin.ModelAdmin):
    list_display=['id','user_id','address1','address2','zipcode','city','state','country']

admin.site.register(UserAddress,UserAddAdmin)




class UserPaymentAdmin(admin.ModelAdmin):
    list_display=['id','user_id','payment_type','account_no','expiry']

admin.site.register(UserPayment,UserPaymentAdmin)

