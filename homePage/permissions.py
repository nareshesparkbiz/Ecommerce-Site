
from rest_framework.permissions import BasePermission
from django.contrib.auth.middleware import get_user

class productPermission(BasePermission):
     
     
     def has_permission(self, request, view):
        return bool(request.user.is_admin) if request.user.is_authenticated else False
     
    
     def has_object_permission(self,request,view, obj):
            return self.has_permission(request, view)
