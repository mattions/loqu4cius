# A Lightweight blog engine, using Django 1.4 and App Engine.

## Requirements

Google Appengine Python SDK 1.7.3+

## Getting started

Run locally:

    git clone https://github.com/mattions/loqu4cius.git
    cd loqu4cius
    ./serve.sh

Visit <http://localhost:8080> to marvel at your work.

## Deploy

Create a CloudSQL instance and database https://developers.google.com/cloud-sql/, 
and adjust the database in settings.py

    DATABASES = {
        'default': {
            'ENGINE': 'google.appengine.ext.django.backends.rdbms',
            'INSTANCE': 'loqu4cious:loqu4cius', # Change-me
            'NAME': 'locqu4cius_db', # Change-me
            }
        }

Change the name of the instance with your appspot id. 
First set up an app on <http://appengine.google.com> and replace 
`application` in `app.yaml` with the name of your app (in your text editor or like this):

    sed -i '' 's/djappeng1ne/myappid/' app.yaml

You're ready to deploy:

	./release_site.py
	
Note: `release_site.py` automatically uploads the site, runs "./manage.py syncdb" in production
increase the version number by one, commits the changes to the repo and tag the code with the 
version.


## Running tests

    python manage.py test blog
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s



## So what's going on?

### app.yaml

- Sets up static resources
- Points all other paths to the WSGI app

### main.py

- Sets the `DJANGO_SETTINGS_MODULE` environment var
- Routes logging for production
- Defines the WSGI app

### manage.py

- Uses path-fixing mechanisms in order for tests to run properly

### settings.py

- Usual Django defaults
- Sets the `SESSION_ENGINE` to a custom memcache/datastore session backend
- settings.BLOG_NAME, and settings.DISQUS_SHORTNAME sets respectevely the BLOG_NAME 
  and the DISQUS_SHORTNAME used for the comments on the entry.

### lib/environ.py

- Uses various internal SDK functions to set up the system environment in such a way 
  that things will run in the context of Appengine's service stubs

### lib/memcache.py

- So App Engine's memcache is seen by django

## blog

- The app that runs the blog 
