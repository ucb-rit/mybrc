import json
from django.shortcuts import render
from django.http import JsonResponse
from dashboard import utils
import os, os.path, json
import requests

"""
    Main views for savio_dashboard.
"""
def home(request):
    return render(request, 'home.html');

def login(request): 
    return render(request, "login.html");

def job_history(request):
    title = "Job History"

    args = {'theTitle': title}
    return render(request, 'job_history.html', args);

def notifications(request): 

    ## FIXME: VPN is currently not accessible. 
	#check_param = request.GET.get('search_account')
    check_param = None

    serv_get_json = utils.get_local_json()

    print("\n\n---------------")
    print("Within notifications...")
    print("serv_get_json: ", serv_get_json)
    print("-------------------\n\n")

    if check_param != None:
        req_val = request.GET['search_account']

        try:
            serv_get = utils.get(int(req_val))
            print("\nIn the TRY...")
            print("serv_get: ", serv_get)
            #break
            url = 'http://128.3.7.72:8000/accounts' 
            r = requests.get(url)

            vpn = r.json()
            #sample_acc = vpn['results'][int(req_val)]
            serv_get = utils.get(int(req_val))
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

        """
        if utils.get():
            messages.info(request, utils.get())
            serv_get = utils.get()

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
        """
        
        args = { 'the_title': title, 'acc_id': 1,
            'acc_name': 'foo',
            'acc_time': 1,
            'acc_desc': 'Good work',
            'acc_alloc': 10000,
            'acc_balance': 8000,
            'acc_perc': 80,
            'bad_submit': 'false'}

        return render(request, 'notifications.html', args)

