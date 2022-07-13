from django.urls import path
from .views import RegisterView, ProfileView

urlpatterns = [
      path('register/', RegisterView.as_view()),
      path('user/', ProfileView.as_view()),     
]