from django.conf import settings
from django.conf.urls import patterns, url

from django.views.generic.dates import MonthArchiveView

from .views import EntryList, EntryDetail, EntryCreate, EntryUpdate, EntryDelete
from .views import EntryMonthArchiveView

urlpatterns = patterns('',
   url(r'^create/$', EntryCreate.as_view(), name="entry-create"),
   url(r'^(?P<slug>[-_\w]+)/update/$', EntryUpdate.as_view(), name="entry-update"),
   url(r'^(?P<slug>[-_\w]+)/delete/$', EntryDelete.as_view(), name="entry-delete"),
   url(r'^(?P<slug>[-_\w]+)/$', EntryDetail.as_view(), name="entry-detail"),
   url(r'^post/monthly/$', EntryMonthArchiveView.as_view(), name="monthly"),
   url(r'^$', EntryList.as_view(), name='entry-list'),
   url(r'^$', EntryList.as_view(), name='home'),
   )