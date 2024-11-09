from django.urls import path
from . import views


urlpatterns = [
    # Home Page


    # Authentication URLs
    path('signup/', views.register, name='signup'),  # User registration
    path('login/', views.login_view, name='login'),  # User login
    path('logout/', views.logout_view, name='logout'),  # User logout

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),  # User dashboard

    # Profile Completion (After Registration)
    path('profile/update/', views.complete_profile, name='complete_profile'),  # Complete profile after signup

    # Profile Editing and Viewing
    path('profile/edit/', views.profile_edit, name='profile_edit'),  # Edit own profile
    path('profile/', views.profile_view, name='profile_view'),  # View own profile

    # User Profiles (Other Users)
    path('profiles/<str:username>/', views.user_profile_view, name='user_profile'),  # View another user's profile
]
