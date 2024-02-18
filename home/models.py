from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class UsersModel(AbstractUser):
    ContactNo = models.CharField(max_length=10 , unique = True ,null = True)
    Address = models.CharField(max_length = 250 , null = True)
    Country = models.CharField(max_length = 50 , null = True)
    Gender = models.CharField( max_length = 10, default = "")
    BirthDate = models.DateField(null = True)


# class RoomTypeModel(models.Model):
#     Room = models.CharField(max_length = 20)
#     Description = models.CharField(max_length=250)
#     Price = models.DecimalField(max_digits=6 , decimal_places = 2)


# class RoomModel(models.Model):
#     Users = models.OneToOneField(UsersModel , on_delete= models.CASCADE )
#     RoomType = models.OneToOneField(RoomTypeModel , on_delete= models.CASCADE)
#     Amenities = models.CharField(max_length=260)
     

class FeedbackModel(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)
    Message = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName


class StaffModel(models.Model):
    id = models.AutoField(primary_key= True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)
    Image = models.ImageField(upload_to= 'img' , null = True)
    Phone = models.CharField(max_length=100 , unique = True)
    Address = models.CharField(max_length=100)
    DOB = models.DateTimeField(null=True)  # Format: 2024-02-11
    Gender = models.CharField(max_length=10)
    Position = models.CharField(max_length=20)
    Salary = models.DecimalField(max_digits = 6 , decimal_places = 2)
    Startdate =models.DateTimeField(null=True)
    Enddate =models.DateTimeField(null=True)

    def __str__(self):
        return self.firstName


