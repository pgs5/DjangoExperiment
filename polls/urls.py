from django.urls import path
from . import views

urlpatterns = [
    path('',views.poll_home, name='poll_home')
]
