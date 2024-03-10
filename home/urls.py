from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home , name ='Home'),
    path('About', views.About , name ='About'),
    path('Contact', views.Contact , name ='Contact'),
    path('Registration', views.register , name ='Registration'),
    path('Staff', views.Staff , name ='Staff'),
    path('Feedback', views.Feedback , name ='Feedback'),
    path('Room', views.Roomview , name ='Room'),
    path('RoomType', views.RoomTypeview , name ='RoomType'),
    path('Book', views.Book , name ='Book'),
    path('Bill', views.Bill , name ='Bill'),
    path('login/', auth_views.LoginView.as_view(template_name='Login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Logout.html'), name='logout'),
    path('reset_Password/', auth_views.PasswordResetView.as_view(template_name='ForgotPassword.html'),name='reset_password'),
    path('reset_Password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='PasswordResetSent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='PasswordResetConf.html'), name='password_reset_confirm'),
    path('reset_Password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='PasswordResetDone.html'), name='password_reset_complete'),
]
