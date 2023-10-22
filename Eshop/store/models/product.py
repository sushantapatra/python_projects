from django.db import models
from .category import Category


class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=1)

    @staticmethod
    def getProductsByIds(ids):
        # id__in => like in operators
        return Products.objects.filter(id__in=ids)

    @staticmethod
    def getAllProducts():
        return Products.objects.all()

    @staticmethod
    def getAllProductsById(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.getAllProducts()

    def __str__(self):
        return f"{self.name} - $ {self.price}"
