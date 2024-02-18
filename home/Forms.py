from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = "__all__"

class StaffForm(forms.ModelForm):
    DOB = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}))
    Startdate = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}))
    Enddate = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}))
    class Meta:
        model = StaffModel
        fields = "__all__"

class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(required= True)
    last_name = forms.CharField(required= True)
    email = forms.EmailField(required= True)
    Gender = forms.CharField(max_length=10 ,required= True)
    ContactNo = forms.CharField(required= True)
    BirthDate = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}),required= True)
    Address = forms.CharField(required= True)
    Country = forms.CharField(required= True)
    username = forms.CharField(required= True)
    # password = forms.CharField(required= True)
    class Meta(UserCreationForm.Meta):
        model = UsersModel
        fields = ('first_name' , 'last_name','email' ,'Gender' ,'ContactNo','BirthDate','Address' ,'Country',
                  'username',)

    @transaction.atomic
    def data_save(self):
        User = UsersModel.objects.create()
        User.first_name = self.cleaned_data.get('first_name')  
        User.last_name = self.cleaned_data.get('last_name')  
        User.email = self.cleaned_data.get('email')  
        User.Gender = self.cleaned_data.get('Gender')  
        User.ContactNo = self.cleaned_data.get('ContactNo')  
        User.BirthDate = self.cleaned_data.get('BirthDate')  
        User.Address = self.cleaned_data.get('Address')  
        User.Country = self.cleaned_data.get('Country')  
        User.username = self.cleaned_data.get('username')  
        # User.password = self.cleaned_data.get('password') 
        User.save()
        return UsersModel 
        


# class AdminLoginForm(UserCreationForm):

#     username = forms.CharField(required= True)
#     password = forms.CharField(required= True)
#     class Meta(UserCreationForm.Meta):
#         model = UsersModel
        


# class RoomTypeForm(forms.ModelForm):
#     class Meta:
#         model = RoomTypeModel
#         fields = "__all__"

# class RoomForm(forms.ModelForm):
#     class Meta:
#         model = RoomModel
#         fields = "__all__"


