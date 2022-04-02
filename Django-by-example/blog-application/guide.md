APS_._1234
###############################################

Creating an isolated Python environment
  python -m venv my_env

  Python libraries you install while your virtual environment is active will go into
  the my_env/lib/python3.8/site-packages directory.

  source my_env/bin/activate
#################################################################################################
Installing Django with pip
  pip install "Django==3.0.*"

#########################################################################
Django has been successfully installed. Run python on a terminal, import Django, and check its version, as follows:
https://docs.djangoproject.com/en/3.0/topics/install/
>>> import django
>>> django.get_version()
'3.0.4'


#######################################################################################
Creating your first project
  django-admin startproject mysite

############################################################################################
database migrations that are applied by Django.

  python manage.py migrate

###########################################################################
Running the development server
  python manage.py runserver
#############################################################################
Project settings
  https://docs.djangoproject.com/en/3.0/ref/settings/

#############################################################################
Projects and applications
Throughout this book, you will encounter the terms project and application over
and over. In Django, a project is considered a Django installation with some settings.
An application is a group of models, views, templates, and URLs. Applications
interact with the framework to provide some specific functionalities and may
be reused in various projects. You can think of a project as your website, which
contains several applications, such as a blog, wiki, or forum, that can also be used
by other projects.

############################################################################
Creating an application
  python manage.py startapp blog
########################################################################
Django comes with different types of fields that you can use to define your models.
You can find all field types at https://docs.djangoproject.com/en/3.0/ref/
models/fields/.

#############################################################################
Activating the application
  add in installed app
  'blog.apps.BlogConfig',

####################################################################
Creating and applying migrations
  python manage.py makemigrations blog
#######################################################################
The sqlmigrate command takes the migration names and
returns their SQL without executing it. Run the following command to inspect the
SQL output of your first migration:

  python manage.py sqlmigrate blog 0001


###########################################################################
Creating an administration site for models.
  Creating a superuser
  python manage.py createsuperuser

################################################################################
Adding models to the administration site
  admin.py
  from .models import Post
  admin.site.register(Post)

################################################################################
Customizing the way that models are displayed

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')

############################################################################################
Working with QuerySets and managers

  https://docs.djangoproject.com/en/3.0/ref/models/

  The Django ORM is based on QuerySets. A QuerySet is a collection of database
queries to retrieve objects from your database. You can apply filters to QuerySets
to narrow down the query results based on given parameters.

################################################################################################
Creating objects
