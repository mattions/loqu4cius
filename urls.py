from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    (r'^appengine_sessions/', include('appengine_sessions.urls')),
    (r'', include('core.urls')),
    url(r"^home", TemplateView.as_view(template_name="homepage.html"), name="home"),

)
