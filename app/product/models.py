from django.db import models
from category.models import Category,SubCategory

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_cat = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
