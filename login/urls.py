from django.urls import path, include
from login import views

urlpatterns = [
    path("accounts/",include('django.contrib.auth.urls')),
    path("signup/",views.signup, name="signup"),
    path("logout/",views.logout_page, name="logout"),
    path("userdashboard/", views.userdashboard, name="userdashboard"),
    path("editprofile/", views.edit_userprofile, name="editprofile"),
    path("deleteprofile/", views.deleteprofile, name="deleteprofile")
]