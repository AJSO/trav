from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 


ACCOUNT_STATUS = (
    ("Active","Active"),
    ("Disabled","Disabled"),
) 

# creating a custom user model
class UserAccountManager():
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Email Address is required')
        if not name:
            raise ValueError('Full name is required.')

        email = self.normalize_email(email)
        # creating a normal user
        user = self.model(email=email, name=name)

        user.set_password(password) #making the password encrypted
        user.save(using=self._db)

        return user

#creating a superuser.
    def create_superuser(self, email, name, password):
        user = self.create_user(
            email= self.normalize_email(email),
            password= password,
            name=name
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email =  models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email
