from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.dates import MonthArchiveView
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
    form_class = EntryForm
    template_name = "blog/entry_detail_update.html"

class EntryDelete(LoginRequiredMixin, DeleteView):
    model = Entry
    
class EntryDetail(DetailView):
    model = Entry

class EntryList(ListView):
    model = Entry
    
    def get_queryset(self):
        
        queryset = super(EntryList, self).get_queryset()
        q = self.request.GET.get('q')
        if q is None:
            return queryset
        # Return a filtered queryset
        return queryset.filter(title__icontains=q)

    
class EntryMonthArchiveView(MonthArchiveView):
    model = Entry
    date_field='pub_date'
    make_object_list = True
    allow_future = True