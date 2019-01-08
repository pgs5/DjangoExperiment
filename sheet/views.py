from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sheet
# Create your views here.

class SheetListView(ListView):
    model = Sheet

class SheetDetailView(DetailView):
    model = Sheet
