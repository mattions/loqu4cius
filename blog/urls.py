from django.conf import settings
from django.conf.urls import patterns, url

from .views import EntryList, EntryDetail, EntryCreate, EntryUpdate, EntryDelete

urlpatterns = patterns('',
   url(r'^', EntryList.as_view(), name='home'),
   url(r'post/create', EntryCreate.as_view(), name="entry-create"),
   url(r'post/(?P<slug>\w+)/', EntryDetail.as_view(), name="entry-detail"),
   url(r'post/(?P<slug>\w+)/update', EntryUpdate.as_view(), name="entry-update"),
   url(r'post/(?P<slug>\w+)/delete', EntryDelete.as_view(), name="entry-delete")
   )