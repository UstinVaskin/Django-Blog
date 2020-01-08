pipenv shell 


pip or pip3 


pip3 install django 
pip3 install pillow 


python manage.py runserver 




Change db 


In your settings.py:

Replace this: 
DATABASES = {
   ‘default’: {
       ‘ENGINE’: ‘django.db.backends.sqlite3’,
       ‘NAME’: os.path.join(BASE_DIR, ‘db.sqlite3’),
   }
}

With this: 

DATABASES = {
 # added this to use postgres as the database instead of the default sqlite. do this before running the initial migrations or you will need to do it again
   ‘default’: {
       ‘ENGINE’: ‘django.db.backends.postgresql_psycopg2’,
       ‘NAME’: ‘cats (or relevant name)’,
       ‘HOST’: ‘localhost’,
       ‘PORT’: 5432
   }
}

In your terminal: 

brew services start postgresql (to make sure it is running) 
(In the shell) pipenv install pyscopg2
(In the shell)dropdb cats (permanently delete the data from postgres), if you have an error it’s probably due to tableplus (close it) 
(In the shell)createdb cats
(In the shell)python manage.py makemigrations
(In the shell)python manage.py migrate
(In the shell)python manage.py loaddata <file-name>(probably fixtures.json) 

On table plus and connect to your database. Your database should update as you make changes rather than using dbsqlite. 

