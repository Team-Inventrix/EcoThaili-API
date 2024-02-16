from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=20, null=False, blank = False)
    Description = models.TextField(blank = False, null = False)
    price = models.PositiveSmallIntegerField(blank = False, null = False)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f'{self.product_name}'   