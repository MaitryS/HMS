from django import forms
from .models import *

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = "__all__"

class StaffForm(forms.ModelForm):
    class Meta:
        model = StaffModel
        fields = "__all__"

class UsersForm(forms.ModelForm):
    class Meta:
        model = UsersModel
        fields = "__all__"


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomTypeModel
        fields = "__all__"

class RoomForm(forms.ModelForm):
    class Meta:
        model = RoomModel
        fields = "__all__"


