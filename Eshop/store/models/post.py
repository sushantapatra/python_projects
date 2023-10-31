from django.db import models
from .category import Category
from .subcategory import Subcategory
from tinymce import models as tinymce_models


class Post(models.Model):
    title       = models.CharField(max_length=255)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, default=1)
    content     =tinymce_models.HTMLField()

    @staticmethod
    def getAllPosts():
        return Post.objects.all()
    

    def __str__(self):
        return self.title
    
