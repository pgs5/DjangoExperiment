from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sheet
# Create your views here.

class SheetListView(ListView):
    model = Sheet
    context_object_name ='objects'
    

class SheetDetailView(DetailView):
    model = Sheet
