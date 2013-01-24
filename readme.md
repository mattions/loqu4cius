# A Lightweight blog engine, using Django 1.4 and App Engine.

## Requirements

Google Appengine Python SDK 1.7.3+

## Getting started

Run locally:

    git clone https://github.com/mattions/loqu4cius.git
    cd loqu4cius
    
Change the development database with your MySql database, 
create a virtualenviroment and install all the required package

	pip install -r requirements.txt
	
Sync the db

	./manage.py syncdb

Launch the server with honcho

	honcho -f Procfile.dev start

Visit <http://localhost:8080> to check it out 

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
`application` in `app.yaml` with the name of your app:

You're ready to deploy:

	./release_site.py
	
Note: `release_site.py` automatically uploads the site, runs `./manage.py syncdb` in production
increase the version number by one, commits the changes to the repo and tag the code with the 
version.


## Running tests

	Creating test database for alias 'default'...
	..
	----------------------------------------------------------------------
	Ran 2 tests in 0.222s
	
	OK
	Destroying test database for alias 'default'...


## So what's going on?

The main structure of the project is similar to https://github.com/potatolondon/djappengine
Check that readme for more info.

## Loqu4cius specific settings

#### settings.py

- settings.BLOG_NAME is used to set the blog name and title
- and settings.DISQUS_SHORTNAME is used to integrate the disqus comments

### blog

- The app that runs the blog 
