from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

# Custom User Model

class TimeStampModel(models.Model):
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        abstract=True

# class Role(models.Model):
#     id=models.IntegerField(primary_key=True)
#     role_name=models.CharField(max_length=30)
#     permission=models.TextField()

    # def __str__(self):
    #     return self.role_name






#Custom  User Manager
class MyUserManager(BaseUserManager):
    def create_user(self, email,firstname,lastname, password=None,password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstname,lastname, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            firstname=firstname,
            lastname=lastname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser,TimeStampModel):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    
    contact=models.CharField(max_length=12)
    profile_img=models.ImageField()
    last_login=models.DateTimeField(auto_now=True)


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname", "lastname"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin






# ----UserAddress---------
class UserAddress(TimeStampModel):

    user_id=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    address1=models.TextField(blank=True,null=True)
    address2=models.TextField(blank=True,null=True)
    zipcode=models.CharField(max_length=6)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)

    def __str__(self):
        return self.address1+self.address2+self.zipcode+self.city+self.state+self.country


class UserPayment(models.Model):

    user_id=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    payment_type=models.CharField(max_length=50)
    account_no=models.CharField(max_length=20)
    expiry=models.DateField()

    def __str__(self) :
        return self.payment_type
    
