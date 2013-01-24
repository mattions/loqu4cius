from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.dates import MonthArchiveView
from django.utils.timezone import now
from django.db.models import Q
from django.conf import settings 

from braces.views import LoginRequiredMixin
import django_wysiwyg

from .models import Entry
from .forms import EntryForm

import logging

logger = logging.getLogger(__name__)

class EntryCreate(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        logger.debug(form.instance.body_text)
        form.instance.body_text = django_wysiwyg.clean_html(form.instance.body_text)
        logger.debug("Body_text cleaned version:")
        logger.debug(form.instance.body_text)
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
    
    queryset = Entry.objects.order_by("-pub_date")
    
    def get_queryset(self):
        
        queryset = super(EntryList, self).get_queryset()
        q = self.request.GET.get('q')
        if q is None:
            return queryset
        # Return a filtered queryset
        return queryset.filter(Q(title__icontains=q) | Q(tags__name__contains=q)).distinct()
