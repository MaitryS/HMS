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

meals_choices = [('1', 'no meals') , ('2' , 'breakfast') , ('3', 'breakfast with lunch'), ('4','breakfast with lunch and dinner')]

class RoomForm(forms.ModelForm):
    meals=forms.ChoiceField(choices= meals_choices,widget=forms.RadioSelect() ,required= True)
    class Meta:
        model = Room
        fields = "__all__"

class BookForm(forms.ModelForm):  
    arrival_date = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}))
    departure_date = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}))
    def __init__(self, **kwargs):
        self.room = kwargs.pop('room', None)
        self.user = kwargs.pop('user', None)
        super(BookForm, self).__init__(**kwargs)

    def save(self, commit=True):
        obj = super(BookForm, self).save(commit=False)
        obj.room = self.room
        obj.user = self.user
        if commit:
            obj.save()
        return obj

    class Meta:
        model = Book
        fields = ("arrival_date" , "departure_date")

class BillForm(forms.ModelForm):
    paymentdate = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}))
    class Meta:
        model = Bill
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


