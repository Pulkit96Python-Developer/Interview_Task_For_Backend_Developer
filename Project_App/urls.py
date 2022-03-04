from django.contrib import admin
from django.urls import path
from Project_App import views

urlpatterns = [
    path('',views.Home,name='Home_Page'),
    path('Registration_Successful',views.Registration_Successful,name='Registration_Successful'),
    path('login',views.Login,name='login'),
    path('Verification',views.Verification,name="Verification"),
    path('Admin_Login',views.Admin_Login,name='Admin_Login'),
    path('Admin_Registration',views.Admin_Registration,name='Admin_Registration'),
    path('Admin_Login_Verification',views.Admin_Login_Verification,name='Admin_Login_Verification'),
    path('Add_New_User',views.Add_New_User,name='Add_New_User'),
    path('User_Listing',views.User_Listing,name='User_Listing'),
    path('Edit_User/<int:i>/',views.Edit_User,name='Edit_User'),
    path('Delete_User/<int:i>/',views.Delete_User,name='Delete_User'),
    path('Edit_User/<int:i>/User_Credentials_Changed',views.User_Credentials_Changed,name="User_Credentials_Changed"),
    path('Selected_User_Details',views.Selected_User_Details,name='Selected_User_Details')
]
