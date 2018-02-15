from django.db import models
from django.db.models.signals import post_save
import json, os, os.path

#Loads json file
file_path = os.path.join(os.path.dirname(__file__), '../static/docs/sample.json')
with open(file_path, 'r') as json_data:
	data = json.load(json_data)

#Job object
class Job(models.Model):
	job_data = data["job"]

class User(models.Model):
	user_data= data["user"]

class Account(models.Model):
	account_data = data["account"]