from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render ,redirect
from django.contrib import messages
from django.urls import reverse
from .Forms import  *
from .models import *
from django.views.generic import CreateView
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import  login_required
from .decorators  import unauthenticated_user
import datetime
# generating pdf from bill
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage
# sending pdf via email
import smtplib #SMTP (Simple Mail Transfer Protocol) library.
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
import datetime

# # Create your views here.
# def check_availability(request , room , checkin , checkout):
    # avail_list = []
    # booking_list = Booking.objects.filter(room = room)
    # for booking in booking_list:
    #     if booking.checkin_date >= checkout or booking.checkout_date <= checkin:
    #         avail_list.append(True)
    #     else:
    #         avail_list.append((False))
    # return all(avail_list)     


def check_availability(request):
    if request.method == 'GET':
        checkin = request.GET.get('checkin')
        checkout = request.GET.get('checkout')
        checkin_d = datetime.datetime.strptime(checkin, '%Y-%m-%d').date()
        checkout_d = datetime.datetime.strptime(checkout, '%Y-%m-%d').date()
        avail_list = []
        booking_list = Booking.objects.all()
        for booking in booking_list:
            if booking.checkin_date > checkout_d or booking.checkout_date < checkin_d:
                avail_list.append(True)
            else:
                avail_list.append((False))

        if all(avail_list):
            messages.success(request, f'Room Is available ')
            return redirect('Home')
        else:
           messages.error(request , f'room is not available')
        return redirect('Home')
    else:
        return render(request, 'index.html', {'error_message': 'Invalid request method.'})
def Home(request):
    tr=RoomType.objects.all()
    room = Room.objects.all()[:3]
    rooms = Room.objects.all()
    guest = Guest.objects.all()

    context = {
        'room': room,  
        'rooms' :rooms , 
        'guest' :guest ,
        }
    return render(request, "index.html", context)

def About(request):
    return render(request , "About.html")


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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:  
                return redirect(reverse('/admin/'))
            else:
                return redirect('Home') 
        else:
            messages.error(request, 'Invalid username or password.')

        messages.success(request, f' Welcome! {username} You have uccesfully logged in.')
    return render(request, 'login.html')    

def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            messages.success(request, 'Your Details Submited Sucessfully')
            return redirect("Contact")    
    else:
        form = ContactForm()
    params = {'form': form}
    return render(request, "Contact.html", params)

def Staff(request):
    if request.method == 'POST':
        form = SearchForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            params = {'Data': SearchForm()} 
            return render(request , "staff.html" , params)   
    else:
        form = SearchForm()
    params = {'form': form}
    return render(request, "staff.html", params)

def ourRooms(request):
    room_types = RoomType.objects.all()
    rooms = Room.objects.all()
    context = {'room_types': room_types, 'rooms': rooms}
    return render(request, "Room.html   ", context)

def Roomview(request , myid):
    rooms = Room.objects.all()
    room = Room.objects.filter(id = myid)
    print(room) 
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'FeedBack Submited Sucessfully')
            params = {'Feedbackdata': FeedbackForm()} 
            return redirect("Home")    
    else:
        form = FeedbackForm()  
    params = {'room': room[0] , 'rooms': rooms ,'form': form} 
    return render(request , "Room1.html" , params)

   

@login_required
def BookingRoom(request ):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user_id = request.user.id 
            instance.save()
            messages.success(request, 'Your Details Submited Sucessfully')
            return redirect("Booking")
    
    else:
        form = BookingForm()

    params = {'form': form}
    return render(request, "Booking.html", params)

