# mybrc

Reposiroty to hold all the code developed by interns for the myBRC dashboard project and all its associated components like SLURM plugin.

Main components include:
	1. Dashboard code
	2. RESTful service to SLURM data in the external Database
	3. SLURM plugin code


## 1. Dashboard 

Contains code for Frontend of Django web app. Within Docker container for development and production. Docker container uses **docker compose** for ease of use. 

#### Development mode 

Uses <code>requirements/development.txt</code> and launches with:

```
    $ docker-compose up
```

#### How to run 

```
    $ python manage.py runserver
```

May first need to migrate new changes for Django  

```
    $ python manage.py migrate 
```

## 2. RESTful API + SQL

**rest/** and **sql/** directories contain the code for the RESTful API and the SQL commands that build the database + tables. 

## 3. SLURM plugin 

*To be included...* 