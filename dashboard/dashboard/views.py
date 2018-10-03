from django.shortcuts import render
from django.http import JsonResponse
from . import url_utils
import os, os.path, json
import requests

"""
    Main views for savio_dashboard.
"""
def account_statistics(request):
    return render(request, "account_statistics.html", 
                  { "theTitle" : "Account Statistics" });

def faqs(request):
    return render(request, "faqs.html", 
                  { "theTitle" : "Frequently Asked Questions" });

def job_history(request):
    return render(request, "job_history.html", 
                  { "theTitle" : "Job History" });

def home(request):
    # FIXME: should login route be home
    #return render(request, "home.html");
    return render(request, "login.html");

def login(request): 
    return render(request, "login.html");

def menu(request):
    return render(request, "menu.html");

def notifications(request): 

    # FIXME: VPN is currently not accessible. 
    #check_param = request.GET.get('search_account')
    check_param = None

    serv_get_json = url_utils.get_local_json()

    print("\n\n---------------")
    print("Within notifications...")
    print("serv_get_json: ", serv_get_json)
    print("-------------------\n\n")

    if check_param != None:
        req_val = request.GET['search_account']

        try:
            serv_get = url_utils.get(int(req_val))
            print("\nIn the TRY...")
            print("serv_get: ", serv_get)
            #break
            url = 'http://128.3.7.72:8000/accounts' 
            r = requests.get(url)

            vpn = r.json()
            #sample_acc = vpn['results'][int(req_val)]
            serv_get = url_utils.get(int(req_val))
            title = "Notification Center"
            acc_perc = url_utils.check_balance(serv_get['acc_balance'], serv_get['acc_alloc'])
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
        if url_utils.get():
            messages.info(request, url_utils.get())
            serv_get = url_utils.get()

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
            'bad_submit': 'false' }

        print("\nargs in views: ", args)

        return render(request, 'notifications.html', args)

def personal_statistics(request):
    return render(request, "personal_statistics.html", 
                  { "theTitle" : "Personal Statistics" });

def quota_manager(request):
    return render(request, "quota_manager.html", 
                  { "theTitle" : "Manage Quotas" });

def settings(request):
    return render(request, "settings.html", 
                  { "theTitle" : "Settings" });

def su_calculator(request):
    return render(request, "su_calculator.html", 
                  { "theTitle" : "SU Calculator" });

#################################################################################
## Highcharts example for data viz 
#################################################################################

# FIXME: remove highchart example views when implemented 

def json_example(request):
    return render(request, 'json_example.html')

def chart_data(request):
    dataset = Passenger.objects \
        .values('embarked') \
        .exclude(embarked='') \
        .annotate(total=Count('embarked')) \
        .order_by('embarked')

    port_display_name = dict()
    for port_tuple in Passenger.PORT_CHOICES:
        port_display_name[port_tuple[0]] = port_tuple[1]

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Titanic\'s Passengers By Embarkation Port'},
        'series': [{
            'name': 'Embarkation Port',
            'data': list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)




