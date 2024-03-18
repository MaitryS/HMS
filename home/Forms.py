from django import forms
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from django.contrib.auth.models import User
from django.db import transaction
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()



Gender_choices = [('Male','Male'),('Female','Female')]

class UserSignUpForm(UserCreationForm):
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    email = forms.EmailField(required= True)
    gender=forms.ChoiceField(choices=Gender_choices,widget=forms.RadioSelect() ,required= True)
    contactno = forms.CharField(required= True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name' , 'last_name','email' ,'gender' ,'contactno',
                  'username',)

    @transaction.atomic
    def data_save(self):
        user =super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')  
        user.last_name = self.cleaned_data.get('last_name')  
        user.email = self.cleaned_data.get('email')  
        user.gender = self.cleaned_data.get('gender')  
        user.contactno = self.cleaned_data.get('contactno')   
        user.save()
        return user 
        


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = "__all__"



class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"

class BookingForm(forms.ModelForm):  
    checkin_date = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}))
    checkout_date = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}))
    class Meta:
        model = Booking
        fields = ("room","checkin_date", "checkout_date")

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = "__all__"

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = "__all__"

class SearchForm(forms.ModelForm):
    guest = forms.ChoiceField(choices= Guest,required= True)
    checkin = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}))
    checkout = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}))
    class Meta:
        model = Search
        fields = "__all__"



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class StaffForm(forms.ModelForm):
    DOB = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}))
    startdate = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}))
    enddate = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}))
    class Meta:
        model = Staff
        fields = "__all__"


