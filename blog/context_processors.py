from django.conf import settings

def get_disqus_shortname(request):
    return({"DISQUS_SHORTNAME" : settings.DISQUS_SHORTNAME})