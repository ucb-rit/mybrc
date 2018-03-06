from personal_statistics import services
from django.shortcuts import render, HttpResponse
from django.contrib import messages
import os, os.path, json

# Create your views here.
def personal_statistics(request):
	title = "Personal Statistics"

	if services.get():
		messages.info(request, services.get())
		serv_get = services.get()

	args = { 'the_title': title, 'acc_id': serv_get['acc_id'],
				'acc_name': serv_get['acc_name'], 
				'acc_time': serv_get['acc_time'],
				'acc_desc': serv_get['acc_desc'],
				'acc_alloc': serv_get['acc_alloc'],
				'acc_balance': serv_get['acc_balance'] }
	return render(request, 'personal_statistics.html', args)