from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime    


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=80)
    description = models.TextField()
    category = models.TextField()
    rating = models.FloatField(default=0)
    g_rating = models.FloatField(default=0)
    # photo

class Reviewer(models.Model):
    name = models.CharField(max_length=30)
    like = models.IntegerField()
    clas = models.TextField()
    description = models.TextField()
    contact = models.CharField(max_length=80)
    hours = models.IntegerField()
    username = models.TextField()
    Hpassword = models.TextField()
    salt = models.TextField()
    last_login = models.DateTimeField()
    # photo
class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    owner = models.ForeignKey(Reviewer,on_delete=models.CASCADE)
    like = models.IntegerField()
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],)
    comment = models.TextField()
