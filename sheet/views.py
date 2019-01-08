from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Sheet

# Create your views here.

class SheetListView(ListView):
    model = Sheet
    ordering = ['-date_posted']
    paginate_by = 3



class SheetDetailView(DetailView):
    model = Sheet

class SheetCreateView(CreateView):
    model = Sheet
    fields = ['title','description', 'composer' ,'sheet_pdf','initial_key']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
