# Hi

--

# Goals

* Build a complete, good practices Django app
* Test the app
* Deploy the app to Heroku

--

# Terms

## Project

This directory *generally* holds on to everything in your project. Doesn't have to, but keeping everything inside makes for a tidier checkout and easy transation to make an app or project reusable.

## App

These are, again, generally single directory that holds everything associated with a single bit of functionality in your project. Good app design states that each app concerns itself with one, and ideally only one, piece of functionality in your project. All Django apps have a `models.py` module, even if that module is empty. I generally end up giving all of my apps a `forms.py`, `urls.py`, and a `tests` directory instead of single `tests.py` module they come with.

### App templates

While it's not required to organize your templates by app, I think it makes the most sense. Notice how the `templates` also contains another directory with the app name. This is a bit redundant, but it helps to enforce the organization more, too.

## Project stub

By default, Django creates a pseudo-app named the same as your project. This app holds onto your site-wide URLs and other things that should be global to your project.

## Global templates

These templates are for your entire site. Generally this is where you'll find whatever template actually holds onto your `doctype`.

## Static files

Finally, these are the design assets for your project. You can further create app-specific assets if you wanted to, but I generally don't for non-reusable apps. We won't cover how to do this, but docs are available or you can ask me after class or during a break.

--

# Starting

Pick somewhere you want to create this project. I generally go for a directory named `sites` but it's entirely up to you.

## `virtualenv`

`virtualenv`, if you don't know, is a great tool for dividing up your Python installed packages. That means this project, today, can use Django 1.5.1 and the project you do in three months can use Django 1.6.0 and you can work on both, on the same machine and even at the same time, without worrying about the newer Django clobbering the older Django.

If you haven't installed it already, `sudo pip install virtualenv`. I also recommend checking out `virtualenvwrapper` later; it'll make your life with `virtualenv` even easier.

`virtualenv microblog-venv --distribute` will create our `virtualenv` and tell it to use Distribute instead of the older Setuptools. You should now see a directory named `microblog-venv` with a few other folders inside of it. We won't be working in this directory, but it's good to know that it's there. To actually get started installing things we need, we need to first activate the virtual environment with `source microblog-venv/bin/activate`. You'll see your prompt change.

## Django's startproject

Now we'll start installing our requirements. At first, we only have two. Django and a Postgres library so we can talk to our database. If you do `which pip` you'll see that it references the `pip` executable in our virtual environment instead of the one installed globally on our system, which means any installs will go to our virtual environment instead of globally. Yay! So let's do `pip install django==1.5.1` and wait a little bit for it to download and be processed. The `==1.5.1` tells `pip` to only install the 1.5.1 release of Django.

When we get our prompt back, we can now type `django-admin.py` and get a list of commands that are available. We want to start a project so let's use `startproject`. `django-admin.py startproject microblog` starts our microblog project for us by creating the project stub and `manage.py` inside the project directory.

## Create a database

Before we get into configuring our project, let's go ahead and create a database. `createdb microblog` creates one for people that use Postgres. If you're using MySQL, `mysqladmn create microblog`.

### Install database adapter

If you're using Postgres, `pip install psycopg2`. If you're using MySQL, `pip install MySQL-python`. This should be the last thing that is different for us between the two databases.

## Requirements

We can use `pip freeze` to give us a list of all of our installed packages. We should export this into a file that we can use to replicate this project and that Heroku will use to set up our environment. `pip freeze > requirements.txt` will generate the file for us (the name is important to Heroku).

:: 01 ::

## Settings

* Split up settings :: 02 ::
* Set up file paths
* .gitignore local.py
* Import everything in `settings/__init__.py`
* Overide bits in `settings.local` :: 03 ::

## Syncdb

* Explain what this does and doesn't do (i.e. it's dumb)
* Create superuser

## Install South

* `pip install south`
* Add to `THIRD_PARTY_APPS`
* `syncdb` for the last time :: 04 ::

## Runserver

* `python manage.py runserver`
* 127.0.0.1:8000

Awesome, but our project doesn't *do* anything. Start by turning on the admin.

--

# Admin

## Enable the admin

* urls
* / is going to 404 now, explain why.
* Show off users/groups, explain how this is a major Django selling point.

:: 05 ::

--

# Posts app

## Start the app

* `./manage.py startapp posts`
* Apps should do one thing
* Add app to `LOCAL_APPS` :: 06 ::

## First Model

```
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __unicode__(self):
      return self.name
```

* missing any intelligent save.
* explain `timezone.now`
* explain `__unicode__`

### First migration

* `python manage.py schemamigration --initial posts`
* `python manage.py migrate posts`

:: 08 ::


### admin

* create `posts/admin.py`
* refresh the admin

:: 09 ::

--

# Templates

## Globals

* create `templates` & `templates/layouts` folders in the root `blog/` folder
* touch `templates/home.html` and `templates/layouts/base.html`
* add basic html stubs to `base.html`
* add simple `TemplateView` to `urls.py`

:: 10 ::

## Inheritance and blocks

* Add some common blocks to `base.html`
* Override those blocks in `home.html` just to show how they work

:: 11 ::

## App templates

* create `templates/posts/` in `posts/`
* create `post_list.html` and `post_detail` in the `posts` template dir
* in prep for the future, create `partials/` dir in `posts` directory, too
* and create `_list.html` in the `partials` dir (we'll use these for templatetags)
* in `post_list.html`, extend `base.html` and do a for loop of posts, printing out their titles.

:: 12 ::

--

# Views

## Function-based views

* views in Django can (really always are) be functions
* I prefer class-based views, but we'll get to them later

### List view

* create FBV to display a list of posts
* create `posts/urls.py` and set up the view & url
* add the post urls to `urls.py` under the `blog` namespace

:: 13 ::

### Detail View

* create FBV for a detail view of a post
* create url
* set template to show title, updated_at, and content

:: 14 ::

--

# Model improvements

## Slugs

* showing PKs in the url is sloppy
* add slug field to model
* migrate
* use field in view and url

:: 15 ::

### Admin

* typing that in ourselves sucks
* create ModelAdmin for Post model
* set prepopulated_fields
* make new post instance to show how it works

:: 16 ::

## Autosetting dates

* set created_at and updated_at to be un-editable
* set content of created_at on save, if no PK
* explain how/why of the above step
* show how `editable=False` removes the fields from the admin

:: 17 ::

## Controlling visibility

* add `status` field to the model as boolean
* migrate
* change views to only select posts that have a true `status`
* point out that the above is less than optimal since it's done twice & two different ways

:: 18 ::

### Correct detail view

* import `Http404`
* get proper queryset and filter
* raise 404 if not found

:: 19 ::

### Better way of handling status through django-model-utils

* now we're gonna throw that all away
* `pip install django-model-utils`
* don't need to add it to `INSTALLED_APPS`
* import `Choices` from `model_utils`
* import `StatusModel` from `model_utils.models`
* update `Post` model to be a `StatusModel` and set the `STATUS` `Choices` object
* remove `objects` and model manager
* migrate

:: 20 ::

* change views to use `.live`

:: 21 ::

--

# View improvements

## Models get_absolute_url

* add 'posts' namespace to posts urls
* add link in list template using `{% url %}`

:: 22 ::

* set `get_absolute_url` on the `Post` model
* change list template to use `{{ post.get_absolute_url }}`
* put a link to the list view in the detail template

:: 23 ::

## Media

* add the pure.css link to the base.html template
* create `assets/css` dir and put the pyladies.css file there
* link to `{{ STATIC_URL }}css/pyladies.css` in base.html
* update base.html HTML to start on the theme

:: 24 ::

* update the base.html template to have links to the post list and home

:: 25 ::

--

# More Better Model & Views

## Markdown

* `pip install misaka`* 
* add misaka to requirements.txt
* add `excerpt`, `excerpt_html`, and `content_html` TextFields to the Post model. all are blankable and the `_html` ones are not editable
* add markdown rendering to the `save` method
* explain why to do this on save instead of on render
* migrate
* change detail template to print `content_html|safe`
* remove link back to post list

:: 26 ::

### Some more HTML

* improve markup on blog detail page to match purecss example

:: 27 ::


## Templatetag

* we should be able to list the newest post(s) on the homepage
* we don't want to tie the view to our model, though
* create a simple inclusion tag to show the post(s)

* create `posts/templatetags/post_tags.py` and `__init__.py`

:: 28 ::

## Smarter templating

* why are we repeating so much? what if we want to show our excerpts? let's fix both of those.
* create `partials/_excerpt.html` and use it to print the excerpt, title, etc
* use that on both the list partial and the list template (in fact, include the partial on the template)
* clean up HTML in general around the lists

:: 29 ::

--

# Flat pages

* flat pages are pages that don't need models, just content
* add `django.contrib.flatpages` to `INSTALLED_APPS`
* add flatpages urls
* add flatpages middleware
* `syncdb`
* create `flatpages/default.html` template
* * `{{ flatpage.title }}`
* * `{{ flatpage.content }}`
* set up links to flatpages in footer

:: 30 ::

--

# Testing

* why test?
* what can we test?

## django-discover-runner

* `pip install django-discover-runner`
* set the `TEST_RUNNER` to `discover_runner.DiscoverRunner` in `local.py`

## Start tests

* change `posts/test.py` into a directory
* import `TestCase` from `django.test`
* import our Post model
* create simple tests

:: 31 ::

(do more tests)

--

# Heroku

* finally we'll move to deployment
* install Heroku Toolbelt if you haven't
* create `Procfile`
* `pip install dj-database-url`
* `import dj_database_url` in `base.py`
* set `DATABASES['default']` to `dj_database_url.config()`
* `heroku apps:create`
* copy url from terminal and put it on `ALLOWED_HOSTS`. **no http://**
* `git push heroku master` after a commit

## Sentry

* add the Sentry addon
* `pip install raven`
* add raven to requirements.txt
* add `raven.contrib.django.raven_compat` to `INSTALLED_APPS`
* now any uncaught 500s will be nicely logged (throw one?)

## Static media

* import `StaticFilesHandler` from `django.contrib.staticfiles.handlers`
* wrap the `get_wsgi_application` call in the above handler
* `pip install gunicorn`
* add gunicorn to requirements and `INSTALLED_APPS`
* change `Procfile` to deploy with `wsgi.py`

:: 32 ::

--

# Customize admin

--

# Class-based views
