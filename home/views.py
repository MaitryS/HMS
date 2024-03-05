from django.shortcuts import render ,redirect
from django.contrib import messages
from .Forms import  *
from .models import *
from django.views.generic import CreateView
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import  login_required
from .decorators  import unauthenticated_user
# # Create your views here.


def Base(request):
        roomtype_list = RoomType.objects.all()
        room = Room.objects.all()

        context = {
                'roomtype_list': roomtype_list,
                'room': room,
            }
        return render(request , "Room.html" , context)

def Home(request):
    return render(request , "index.html")

def About(request):
    return render(request , "About.html")

def Services(request):
    return render(request , "Services.html")


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form =  UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome! {username} Your account has been created! You are now able to log in')
            return redirect('Home')
    else:
        form =  UserSignUpForm()
    return render(request, 'Registration.html',{'form': form})

@unauthenticated_user
def Login(request):
    return render(request , "Login.html")


def Contact(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            instance = form.save(commit = False)
            instance.save()

            params = {'Contactdata': ContactForm()} 
            return render(request , "Contact.html" , params)
    
    else:
        form = ContactForm()

    params = {'form': form}
    return render(request, "Contact.html", params)

@login_required
def Feedback(request):
    if request.method == 'POST':

        form = FeedbackForm(request.POST)

        if form.is_valid():

            instance = form.save(commit = False)
            instance.save()

            params = {'Feedbackdata': FeedbackForm()} 
            return render(request , "Feedback.html" , params)
    
    else:
        form = FeedbackForm()

    params = {'form': form}
    return render(request, "Feedback.html", params)



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


def Roomview(request):
    if request.method == 'POST':

        form = RoomForm(request.POST)

        if form.is_valid():

            instance = form.save(commit = False)
            instance.save()

            params = {'RoomData': RoomForm()} 
            return render(request , "Room.html" , params)
    
    else:
        form = RoomForm()

    params = {'form': form}
    return render(request, "Room.html", params)
    


def RoomTypeview(request):
    if request.method == 'POST':

        form = RoomTypeForm(request.POST)

        if form.is_valid():

            instance = form.save(commit = False)
            instance.save()

            params = {'RoomTypeData': RoomTypeForm()} 
            return render(request , "RoomType.html" , params)
    
    else:
        form = RoomTypeForm()

    params = {'form': form}
    return render(request, "RoomType.html", params)


@login_required
def Book(request):
    if request.method == 'POST':

        form = BookForm(request.POST)

        if form.is_valid():

            instance = form.save(commit = False)
            instance.save()

            params = {'BookData': BookForm()} 
            return render(request , "Room.html" , params)
    
    else:
        form = BookForm()

    params = {'form': form}
    return render(request, "Room.html", params)


@login_required
def Bill(request):
    if request.method == 'POST':

        form = BillForm(request.POST)

        if form.is_valid():

            instance = form.save(commit = False)
            instance.save()

            params = {'Billdata': BillForm()} 
            return render(request , "RoomType.html" , params)
    
    else:
        form = BillForm()

    params = {'form': form}
    return render(request, "RoomType.html", params)
