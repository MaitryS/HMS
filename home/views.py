from django.shortcuts import render
from .Forms import  *
from .models import *
# Create your views here.

def index(request):
    return render(request , "index.html")


def Feedback(request):
    if request.method=="POST":
        post= FeedbackModel()
        post.FeedbackId=request.POST['FeedbackId']
        post.firstName=request.POST['firstName']
        post.lastName=request.POST['lastName']
        post.Email=request.POST['Email']
        post.Message=request.POST['Message']
        post.save()
        context = {'form': FeedbackForm()}
        return render(request , "Feedback.html" , context)
    else:
        # If it's a GET request or any other method, render the form
        context = {'form': FeedbackForm()}
        return render(request, "Feedback.html", context)

def Staff(request):
    if request.method=="POST":
        post= StaffModel(request.POST)
        post.Staff_ID =request.POST['Staff_ID']
        post.firstName=request.POST['firstName']
        post.lastName=request.POST['lastName']
        post.Email=request.POST['Email']
        post.Image=request.POST['Image']
        post.Phone=request.POST['Phone']
        post.Address=request.POST['Address']
        post.DOB =request.POST['DOB']
        post.Gender=request.POST['Gender']
        post.Position=request.POST['Position']
        post.Salary=request.POST['Salary']
        post.Startdate=request.POST['Startdate']
        post.Enddate=request.POST['Enddate']
        post.save()
        params = {'staffData': StaffForm()} 
        return render(request , "Staff.html" , params)
    
    else:
        params = {'form': StaffForm()}
        return render(request, "Staff.html", params)


# def Room(request):
#     if request.method=="POST":
#         post= RoomModel()
#         post.RoomId=request.POST['RoomId']
#         post.Users=request.POST['Users']
#         post.RoomType=request.POST['RoomType']
#         post.Amenities=request.POST['Amenities']
#         post.RoomNo=request.POST['RoomNo']
#         post.save()
#         context = {'form': RoomForm()}
#         return render(request , "Room.html" , context)
#     else:
#         Value = {'form': RoomForm()}
#         return render(request, "Room.html", Value)
    


# def RoomType(request):
#     if request.method=="POST":
#         post= RoomTypeModel()
#         post.TypeId=request.POST['TypeId']
#         post.Room=request.POST['Room']
#         post.Description=request.POST['Description']
#         post.Price=request.POST['Price']
#         post.save()
#         context = {'form': RoomTypeForm()}
#         return render(request , "RoomType.html" , context)
#     else:
#         context = {'form': RoomTypeForm()}
#         return render(request, "RoomType.html", context)
