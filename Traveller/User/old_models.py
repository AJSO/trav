from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 
from django.core.validators import RegexValidator


ACCOUNT_STATUS = (
    ("Active","Active"),
    ("Disabled","Disabled"),
) 

# creating a custom user model
class UserAccountManager():
    def create_user(self, email, name, phone, password=None):
        if not email:
            raise ValueError('Email Address is required')
        if not name:
            raise ValueError('Full name is required.')
        if not phone:
            raise ValueError('Mobile Phone required')

        email = self.normalize_email(email)
        # creating a normal user
        user = self.model(email=email, name=name,  phone=phone)

        user.set_password(password) #making the password encrypted
        user.save(using=self._db)
        return user
    
    #creating a staff user
    def create_staffuser(self, email, name, phone, password):
        user = self.create_user(
            email= self.normalize_email(email),
            password= password,
            name=name,
            phone=phone,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user
        
    #creating a superuser.
    def create_superuser(self, email, name, phone, password):
        user = self.create_user(
            email= self.normalize_email(email),
            password= password,
            name=name,
            phone=phone,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator( regex   =r'^\+?1?\d{9,14}$', message ="Phone number must be entered in the format: '+1111111111'. Up to 14 digits allowed.")
    email =  models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225)
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email
    
    #does the user has specific permissions
    def has_perm(self, perm, obj=None):
        return True #yes
    
    #Does the user have permissions to view the app `app_label`?
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
    
    #function to store the otp requests
class PhoneOTP(models.Model):
    phone_regex = RegexValidator( regex   =r'^\+?1?\d{9,14}$', message ="Phone number must be entered in the format: '+111111111'. Up to 14 digits allowed.")
    phone       = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    otp         = models.CharField(max_length = 9, blank = True, null= True)
    count       = models.IntegerField(default = 0, help_text = 'Number of otp sent')
    logged      = models.BooleanField(default = False, help_text = 'If otp verification got successful')
    forgot      = models.BooleanField(default = False, help_text = 'only true for forgot password')
    forgot_logged = models.BooleanField(default = False, help_text = 'Only true if validdate otp forgot get successful')


    def __str__(self):
        return str(self.phone) + ' is sent ' + str(self.otp)
