from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth import get_user_model

# Register your models here.

admin.site.register(FeedbackModel)
admin.site.register(StaffModel)

class CustomUserAdmin(UserAdmin):
    list_display = ('first_name' , 'last_name' , 'email' , 'Gender' , 'username' ,)


admin.site.register(UsersModel , CustomUserAdmin)
# admin.site.register(RoomModel)
# admin.site.register(RoomTypeModel)