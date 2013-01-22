from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from braces.views import LoginRequiredMixin

from .models import Entry

class EntryCreate(LoginRequiredMixin, CreateView):
    model = Entry

class EntryUpdate(LoginRequiredMixin, UpdateView):
    model = Entry

class EntryDelete(LoginRequiredMixin, DeleteView):
    model = Entry
    
class EntryDetail(DetailView):
    model = Entry

class EntryList(ListView):
    model = Entry