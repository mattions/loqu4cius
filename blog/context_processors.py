from django.conf import settings

def blog_settings(request):
    ctx = {
           "DISQUS_SHORTNAME" : settings.DISQUS_SHORTNAME,
           "BLOG_NAME" : settings.BLOG_NAME
           }
    return(ctx)