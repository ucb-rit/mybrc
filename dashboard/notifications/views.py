from notifications import services
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django import template 
import os, os.path, json
import requests

# Create your views here.
def notifications(request):    	

	if request.GET: 
		req_val = request.GET['sample_form']

		url = 'http://128.3.7.72:8000/accounts' 
		r = requests.get(url)

		vpn = r.json()
		#sample_acc = vpn['results'][int(req_val)]
		serv_get = services.get(int(req_val))
		title = "Notification Center"
		args = { 'the_title': title, 'acc_id': serv_get['acc_id'],
					'acc_name': serv_get['acc_name'], 
					'acc_time': serv_get['acc_time'],
					'acc_desc': serv_get['acc_desc'],
					'acc_alloc': serv_get['acc_alloc'],
					'acc_balance': serv_get['acc_balance'] }
		return render(request, 'notifications.html', args)
	else:

		title = "Notification Center"

		if services.get():
			messages.info(request, services.get())
			serv_get = services.get()

		args = { 'the_title': title, 'acc_id': serv_get['acc_id'],
					'acc_name': serv_get['acc_name'], 
					'acc_time': serv_get['acc_time'],
					'acc_desc': serv_get['acc_desc'],
					'acc_alloc': serv_get['acc_alloc'],
					'acc_balance': serv_get['acc_balance'] }
		
		return render(request, 'notifications.html', args)

# Create class + methods for each JSON data field
class getCount:
	def get():
		count = services.get()
		return render(request, 'notifications.html', count)

"""class getCount:
    def get():
        count = services.get()

		print("")
		print("count: ", count)
		print("")

        return render(request, 'notifications.html', count)
"""

