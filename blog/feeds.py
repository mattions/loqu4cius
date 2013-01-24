from django.contrib.syndication.views import Feed
from django.conf import settings

from .models import Entry

class EntriesFeed(Feed):
    title = settings.BLOG_NAME
    link = "/entries/"
    description = "Updates on changes and additions to chicagocrime.org."

    def items(self):
        return Entry.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body_text
