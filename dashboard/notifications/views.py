from notifications import services
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django import template 
import os, os.path, json
import requests

# Create your views here.
def notifications(request): 

	check_param = request.GET.get('search_account')

	serv_get_json = services.get_local_json()

	print("\n\n---------------")
	print("Within notifications...")
	print("serv_get_json: ", serv_get_json)
	print("-------------------\n\n")

	if check_param != None:
		req_val = request.GET['search_account']

		try:
			serv_get = services.get(int(req_val))
			print("\nIn the TRY...")
			print("serv_get: ", serv_get)
			#break
			url = 'http://128.3.7.72:8000/accounts' 
			r = requests.get(url)

			vpn = r.json()
			#sample_acc = vpn['results'][int(req_val)]
			serv_get = services.get(int(req_val))
			title = "Notification Center"
			acc_perc = check_balance(serv_get['acc_balance'], serv_get['acc_alloc'])
			args = { 'the_title': title, 'acc_id': serv_get['acc_id'],
						'acc_name': serv_get['acc_name'], 
						'acc_time': serv_get['acc_time'],
						'acc_desc': serv_get['acc_desc'],
						'acc_alloc': serv_get['acc_alloc'],
						'acc_balance': serv_get['acc_balance'],
						'acc_perc': acc_perc, 'bad_submit': 'false' }
			return render(request, 'notifications.html', args)

		except ValueError:
			print("\nIn the EXCEPT...")
			print("Error: ", ValueError)
			title = "Notification Center"
			args = { 'the_title': title, 'acc_id': "None",
						'acc_name': "None", 
						'acc_time': 0,
						'acc_desc': "None",
						'acc_alloc': 0,
						'acc_balance': 0,
						'bad_submit': 'true',
						'bad_message': 'Please search accounts by number (0 - 2).'}
			return render(request, 'notifications.html', args)	

		except IndexError:
			print("\nIn the EXCEPT...")
			print("Error: ", IndexError)
			title = "Notification Center"
			args = { 'the_title': title, 'acc_id': "None",
						'acc_name': "None", 
						'acc_time': 0,
						'acc_desc': "None",
						'acc_alloc': 0,
						'acc_balance': 0,
						'bad_submit': 'true',
						'bad_message': 'Please search accounts by numbers between 0 - 2.'}
			return render(request, 'notifications.html', args)

	else:

		title = "Notification Center"

		if services.get():
			messages.info(request, services.get())
			serv_get = services.get()
		
		acc_perc = check_balance(serv_get['acc_balance'], serv_get['acc_alloc'])

		args = { 'the_title': title, 'acc_id': serv_get['acc_id'],
					'acc_name': serv_get['acc_name'], 
					'acc_time': serv_get['acc_time'],
					'acc_desc': serv_get['acc_desc'],
					'acc_alloc': serv_get['acc_alloc'],
					'acc_balance': serv_get['acc_balance'],
					'acc_perc': acc_perc, 'bad_submit': 'false' }
		'''
		args = { 'the_title': title, 'bad_submit': 'false'}
		'''
		
		return render(request, 'notifications.html', args)


def check_balance(account_bal, account_alloc):
    if (account_alloc <= 0):
        account_perc = 0
    elif (account_bal <= 0):
        account_perc = 0
    else:
        account_perc = (account_bal / account_alloc) * 100
    return account_perc

# Create class + methods for each JSON data field
class getCount:
	def get():
		count = services.get()
		return render(request, 'notifications.html', count)


