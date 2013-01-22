from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.timezone import now

from braces.views import LoginRequiredMixin

from .models import Entry
from .forms import EntryForm

class EntryCreate(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(EntryCreate, self).form_valid(form)

class EntryUpdate(LoginRequiredMixin, UpdateView):
    model = Entry

class EntryDelete(LoginRequiredMixin, DeleteView):
    model = Entry
    
class EntryDetail(DetailView):
    model = Entry

class EntryList(ListView):
    model = Entry