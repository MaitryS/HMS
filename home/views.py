from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render ,redirect
from django.contrib import messages
from django.urls import reverse
from .Forms import  *
from .models import *
from django.views.generic import CreateView
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import  login_required
from .decorators  import unauthenticated_user
from datetime import date
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
# # Create your views here.


def Home(request):
    tr=RoomType.objects.all()
    room = Room.objects.all()[:4]
    search = Search.objects.all()
    context = {'room': room,'search':search}
    return render(request , "index.html",context)

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

def Check_Availability(request):
    if request.method == 'POST':
        form = SearchForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            params = {'Data': SearchForm()} 
            return render(request , "index.html" , params)   
    else:
        form = SearchForm()
    params = {'form': form}
    return render(request, "index.html", params)

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
def Booking(request ):
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


def generate_pdf():
    # Retrieve the details from model or any other data source
    bills = Bill.objects.select_related('booking').all()
    bill = Bill.objects.all()

        # Render the template with the bills data
    template_path = 'Bill.html'
    context = {'bills': bills}
    template = get_template(template_path)
    html = template.render(context)
    
    # Create a PDF file
    pdf_file = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest = pdf_file)
    print(html)
    
    if pisa_status.err:
        return HttpResponse('Failed to generate PDF')  # Return error if PDF generation fails
    else:
        return pdf_file.getvalue()  # Return the content of the PDF file
    
@login_required
def Billing(request):
    # Generate PDF
    pdf_content = generate_pdf()
    print(pdf_content)
    
    if pdf_content is None:
        return HttpResponse('Failed to generate PDF')
    # dipanshshah20@gmail.com
    # jainish1604@gmail.com
    # Email configuration
    sender_email = "themetro1224@gmail.com"
    receiver_email = "maitryshah91101@gmail.com"
    subject = "Your Booking Details"
    body = "Please confirm the attached PDF Booking file."

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Add PDF attachment
    part = MIMEBase("application/pdf", "octet-stream")
    part.set_payload(pdf_content)
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename=dest.pdf")
    message.attach(part)

    # Connect to SMTP server and send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, "rozt mpta mtdu ctcz")
        server.sendmail(sender_email, receiver_email, message.as_string())
    
    print("Email sent successfully!")
    return HttpResponse("Email sent successfully!")

