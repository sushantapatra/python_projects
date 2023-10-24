from django.db import models
from .category import Category


class Subcategory(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name