from django.shortcuts import render, HttpResponse
import requests
import os, os.path, json


def get(get_idx = 0):
    url = 'http://128.3.7.72:8000/accounts' 
    #params = {'count': count}
    #r = requests.get(url, params=params)
    r = requests.get(url)

    vpn = r.json()
    acc_id = vpn['results'][get_idx]['accountid']
    acc_name = vpn['results'][get_idx]['accountname']
    acc_time = vpn['results'][get_idx]['updated']
    acc_alloc = vpn['results'][get_idx]['accountallocation']
    acc_balance = vpn['results'][get_idx]['accountbalance']
    acc_desc = vpn['results'][get_idx]['description']
    vpn_return = {'acc_id' : acc_id, 'acc_name' : acc_name, 
                'acc_time' : acc_time, 'acc_desc' : acc_desc,
                'acc_alloc' : acc_alloc, 'acc_balance' : acc_balance}
    #vpn_return = {'count' : vpn['results'][0]['accountid']}

    #vpn_return = {'count' : vpn['results'][0]['accountid'],
    #            'results' : vpn['results']}

    return vpn_return

def get_local_json():
    """
    Get local JSON file stored in: 'static/sample_data/users.json'
    """

    ## Read in local json file 
    js_data = open("./static/sample_data/users.json")
    js_load = json.load(js_data)
    #js_dump = json.dumps(js_data)
    js_data.close()

    users_json = js_load['results'][0]

    json_return = {'acc_id' : users_json['userid'],
                    'acc_alloc' : users_json['allocation'],
                    'acc_njobs' : users_json['number-jobs'],
                    'acc_njobs_sub' : users_json['number-jobs-submitted'],
                    'acc_njobs_end' : users_json['number-jobs-ended']}

    return json_return