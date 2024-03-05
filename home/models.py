from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    contactno = models.CharField(max_length=10 ,  blank=True,null = True)
    gender = models.CharField(max_length = 10 ,default="", blank=True)

    def save(self ,*args, **kwargs):
        super().save()

    def __str__(self):
        return self.first_name

class RoomType(models.Model):
    RoomName = models.CharField(max_length = 20)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6 , decimal_places = 2)

    def __str__(self):
        return self.RoomName


class Room(models.Model):
    RoomType = models.ForeignKey(RoomType , on_delete= models.CASCADE)
    amenities = models.CharField(max_length=260)
    
    def __str__(self):
        return self.RoomType.RoomName



class Book(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    room = models.ForeignKey(Room , on_delete= models.CASCADE)
    checkin =models.DateTimeField()
    checkout =models.DateTimeField()
    totalprice = models.DecimalField(max_digits=6 , decimal_places=2)

    def __str__(self):
        return self.user.first_name
     
class Bill(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    book = models.ForeignKey(Book , on_delete= models.CASCADE)
    amount = models.DecimalField(max_digits=6 , decimal_places=2)
    paymentdate =models.DateTimeField()
    paymentmethod =models.CharField(max_length=8 ,null = True)
    
    def __str__(self):
        return self.user.first_name


class Contact(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName


class Staff(models.Model):
    id = models.AutoField(primary_key= True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    image = models.ImageField(upload_to= 'img' , null = True)
    phone = models.CharField(max_length=100 , unique = True)
    address = models.CharField(max_length=100)
    DOB = models.DateTimeField(null=True)  # Format: 2024-02-11
    gender = models.CharField(max_length=10)
    position = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits = 6 , decimal_places = 2)
    startdate =models.DateTimeField(null=True)
    enddate =models.DateTimeField(null=True)

    def __str__(self):
        return self.firstName

class Feedback(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName
