from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^appengine_sessions/', include('appengine_sessions.urls')),
    (r'core/', include('core.urls')),
#    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url('', TemplateView.as_view(template_name="about.html"), name="home"),
    url('blog/', include('blog.urls')),

)
