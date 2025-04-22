from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    barcode = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    class Meta:
        permissions = [
            ('view_product_public', 'Can view product as public'),
            ('add_product_user', 'Can add product as user'),
        ]

    def __str__(self):
        return self.name