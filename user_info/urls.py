from django.urls import path
from .views import RegisterView, ProfileView, UpdateProfileView, ChangePasswordView

urlpatterns = [
      path('register/', RegisterView.as_view()),
      path('userprofile/', ProfileView.as_view()), 
      path('update/<int:pk>',UpdateProfileView.as_view()),   
      path('resetpassword/<int:pk>',ChangePasswordView.as_view()) 
]