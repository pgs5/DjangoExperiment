from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

class SheetUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Sheet
    fields = ['title','description', 'composer' ,'sheet_pdf','initial_key']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class SheetDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Sheet
    success_url ='/sheet-music/'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
