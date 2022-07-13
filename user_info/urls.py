from django.urls import path
from user_info import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
]