from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    '''Manager for user profile'''

    def create_user(self, email,name,password=None):
        if not email:
            raise ValueError('User must have an email adress')
        
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)
    
    def create_superuser(self,email,name,password):
        user=self.create_user(email,name,password)
        
        user.is_superuser=True
        user.is_staff=True

        user.set_password=(password)
        user.save(using=self._db)

        return user
    
class UserProfile(AbstractBaseUser,BaseUserManager):
    email=models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255, blank=True, null=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)


    objects=UserProfileManager()

    USERNAME_FIELD='email'
    #REQUIRED_FIELDS=['name']


    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='UserProfile'
        verbose_name_plural='UserProfile'



