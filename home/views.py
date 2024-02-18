from django.shortcuts import render
from .Forms import  *
from .models import *
from django.views.generic import CreateView
# Create your views here.

def home(request):
    return render(request , "index.html")

def About(request):
    return render(request , "About.html")

def Contact(request):
    return render(request , "Contact.html")

def Services(request):
    return render(request , "Services.html")

def Login(request):
    return render(request , "Login.html")

def Logout(request):
    return render(request , "index.html")


def Users(request):
    # if request.method=="POST":
        # post= UsersModel()
        # post.Gender=request.POST['Gender']
        # post.ContactNo=request.POST['ContactNo']
        # post.BirthDate=request.POST['BirthDate']
        # post.Address=request.POST['Address']
        # post.Country=request.POST['Country']
        # post.save()
    context = {'form': UserSignUpForm()}
    return render(request , "Registration.html" , context )
    # else:
    #     # If it's a GET request or any other method, render the form
    #     context = {'form': UserSignUpForm()}
    #     return render(request, "Registration.html", context)

class register(CreateView):
    model = UsersModel
    form_class = UserSignUpForm
    template_name = 'Registration.html'


def Feedback(request):
    if request.method=="POST":
        post= FeedbackModel()
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
    if request.method == 'POST':

        form = StaffForm(request.POST , request.FILES)

        if form.is_valid():

            instance = form.save(commit = False)
            instance.save()

            params = {'staffData': StaffForm()} 
            return render(request , "Staff.html" , params)
    
    else:
        form = StaffForm()

    params = {'form': form}
    return render(request, "Staff.html", params)


# def Room(request):
#     if request.method=="POST":
#         post= RoomModel()
#         post.Users=request.POST['Users']
#         post.RoomType=request.POST['RoomType']
#         post.Amenities=request.POST['Amenities']
#         post.save()
#         context = {'form': RoomForm()}
#         return render(request , "Room.html" , context)
#     else:
#         Value = {'form': RoomForm()}
#         return render(request, "Room.html", Value)
    


# def RoomType(request):
#     if request.method=="POST":
#         post= RoomTypeModel()
#         post.Room=request.POST['Room']
#         post.Description=request.POST['Description']
#         post.Price=request.POST['Price']
#         post.save()
#         context = {'form': RoomTypeForm()}
#         return render(request , "RoomType.html" , context)
#     else:
#         context = {'form': RoomTypeForm()}
#         return render(request, "RoomType.html", context)
