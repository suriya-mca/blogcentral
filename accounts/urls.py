from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    # register form url 
    path('regform/', views.regform, name='regform'),
    # login form url
    path('login/', views.login, name='login'),
    # logout form url
    path('logout/', views.logout, name='logout'),
    # reset password url
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="forms/resetPassword.html"), name='password_reset'),
    # reset done messsge url
    path('reset-password-done/', auth_views.PasswordResetDoneView.as_view(template_name="forms/resetDone.html"), name='password_reset_done'),
    #  change password url
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="forms/changePassword.html"), name='password_reset_confirm'),
    # complete password message url
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="forms/completedPassword.html"), name='password_reset_complete'),
]
