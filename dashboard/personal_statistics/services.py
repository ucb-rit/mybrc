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
    return vpn_return