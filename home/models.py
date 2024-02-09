from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

gender = [
    ('Male' , 'male'),
    ('Female' , 'female')
]

# class UsersModel(AbstractUser):
#     is_admin = models.BooleanField(default = False)
#     ContactNo = models.CharField(max_length=100 , unique = True)
#     Address = models.CharField(max_length = 250)
#     State = models.CharField(max_length = 50)
#     Country = models.CharField(max_length = 50)
#     Gender = models.CharField(choices= gender , max_length = 6)
#     BirthDate = models.DateField()

class FeedbackModel(models.Model):

    FeedbackId = models.IntegerField()
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)
    Message = models.CharField(max_length=255)


class StaffModel(models.Model):

    Staff_ID = models.IntegerField()
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)
    Image = models.ImageField(upload_to= 'img' , null=True)
    Phone = models.CharField(max_length=100 , unique = True)
    Address = models.CharField(max_length=100)
    DOB = models.DateTimeField(null=True)
    Gender = models.CharField(max_length=10)
    Position = models.CharField(max_length=20)
    Salary = models.DecimalField(max_digits = 6 , decimal_places = 2)
    Startdate =models.DateTimeField(auto_now_add=True , null=True)
    Enddate =models.DateTimeField(auto_now_add=True , null=True)
    # Enddate = models.DateField(auto_now=False, auto_now_add=True)

# class RoomModel(models.Model):

#     RoomId = models.IntegerField()
#     # Users = models.ForeignKey(UsersModel , on_delete = models.CASCADE , default = 1 )
#     RoomType = models.ForeignKey(RoomTypeModel , on_delete = models.CASCADE , default = 1 )
#     Amenities = models.CharField(max_length=260)
#     RoomNo = models.IntegerField()

# class RoomTypeModel(models.Model):
#     TypeId = models.IntegerField()
#     Room = models.CharField(max_length = 20)
#     Description = models.CharField(max_length=250)
#     Price = models.DecimalField(max_digits=6 , decimal_places = 2)