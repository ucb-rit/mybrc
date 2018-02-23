# mybrc

Reposiroty to hold all the code developed by interns for the myBRC dashboard project and all its associated components like SLURM plugin.

Main components include:
	1. Dashboard code
	2. RESTful service to SLURM data in the external Database
	3. SLURM plugin code


## 1. Dashboard 

Contains code for Frontend of Django web app. 


#### How to run 

```
    $ python manage.py runserver
```

May first need to migrate new changes for Django  

```
    $ python manage.py migrate 
```

#### To Do 

Create <b>services.py</b> and <b>views.py</b> for each page. Will be located within each dir - <i>e.g. su_calculator/</i>.

## 2. RESTful API + SQL

**rest/** and **sql/** directories contain the code for the RESTful API and the SQL commands that build the database + tables. 

## 3. SLURM plugin 

*To be included...* 