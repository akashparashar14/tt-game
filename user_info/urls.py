from django.urls import path
from .views import RegisterView, ProfileView, UpdateProfileView

urlpatterns = [
      path('register/', RegisterView.as_view()),
      path('user/', ProfileView.as_view()), 
      path('update/<int:pk>',UpdateProfileView.as_view() ),    
]