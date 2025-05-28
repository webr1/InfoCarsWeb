from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from datetime import datetime,timezone
from django.contrib.auth.models import User

class Cars(models.Model):
    Model=models.CharField(max_length=50,null=False,blank=False)
    Marka=models.CharField(max_length=50,null=False,blank=False)
    Yil = models.PositiveIntegerField(null=False,blank=False,validators=[
        MinValueValidator(1900),
        MaxValueValidator(datetime.now().year)
    ])
    Narx=models.PositiveIntegerField(null=False,blank=False,validators=[
        MaxValueValidator(1000000),
        MinValueValidator(1000)
    ])
    InfoCar=models.TextField(max_length=1000,null=False,blank=False)
    PictureCar=models.ImageField(upload_to="cars_images",null=False,blank=False)
    Stars=models.PositiveIntegerField(null=False,blank=False,validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    def __str__(self):
        return f"{self.Model}, {self.Yil}, {self.Narx}$"


