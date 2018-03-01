from notifications import services
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django import template 
import os, os.path, json

# Create your views here.
def notifications(request):
	title = "Notification Center"

	if services.get():
		messages.info(request, services.get())
		serv_get = services.get()

	print("\nWithin notifications()")
	print("services.get(): ", services.get())
	print("-------\n")

	args = { 'the_title': title, 'acc_id': serv_get['acc_id'],
				'acc_name': serv_get['acc_name'], 
				'acc_time': serv_get['acc_time'],
				'acc_desc': serv_get['acc_desc'],
				'acc_alloc': serv_get['acc_alloc'],
				'acc_balance': serv_get['acc_balance'] }

	print("\nWithin notifications")
	print("args: ", args)
	print("+++++++\n\n")
	
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

