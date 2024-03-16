from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth import get_user_model

# Register your models here.

admin.site.register(Feedback)
admin.site.register(Staff)
admin.site.register(Contact)

class CustomUserAdmin(UserAdmin):
    list_display = ('first_name' , 'last_name' , 'email' , 'gender' , 'username' ,)


admin.site.register(User , CustomUserAdmin)
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Booking)
admin.site.register(Bill)
admin.site.register(Search)