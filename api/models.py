from django.db import models
import uuid
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from drf_yasg.generators import OpenAPISchemaGenerator

#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, first_name, last_name, password=None, password2=None):
      """
      Creates and saves a User with the given email, name, tc and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          first_name=first_name,
          last_name = last_name,
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email,first_name="admin", last_name="admin", password=None):
      """
      Creates and saves a superuser with the given email, name, tc and password.
      """
      user = self.create_user(
          email,
          first_name,
          last_name,
          password=password,
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

#  Custom User Model
class User(AbstractBaseUser):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  name = models.CharField(max_length=200)
  first_name = models.CharField(max_length=200, default = "eco" )
  last_name = models.CharField(max_length=200, default = "thaili")
#   tc = models.BooleanField(default= True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  def __str__(self):
      return self.email

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

  @property
  def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=20, null=False, blank = False)
    Description = models.TextField(blank = False, null = False)
    price = models.PositiveSmallIntegerField(blank = False, null = False)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f'{self.product_name}'   

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.email}'
    
class Careers(models.Model):
    email = models.EmailField(
      verbose_name='Email',
      max_length=255,
     )
    full_name = models.CharField(max_length=200)
    cover_letter = models.TextField()
    cv = models.FileField(upload_to="cv") 

class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema