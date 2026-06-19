from django.db import models

# Create your models here.

class Cloth(models.Model):
    image = models.ImageField(upload_to='clothes/')
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=255)
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.name or self.description


class Fruit(models.Model):
    image = models.ImageField(upload_to='fruits/')
    name= models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=255)
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.name or self.description
# Create your views here.
