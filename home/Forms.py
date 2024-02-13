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

# class UsersForm(UserCreationForm):

#     class Meta(UserCreationForm.Meta):
#         model = UsersModel
#         fields = "__all__"


# class RoomTypeForm(forms.ModelForm):
#     class Meta:
#         model = RoomTypeModel
#         fields = "__all__"

# class RoomForm(forms.ModelForm):
#     class Meta:
#         model = RoomModel
#         fields = "__all__"


