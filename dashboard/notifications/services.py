from django.shortcuts import render, HttpResponse
import requests
import os, os.path, json


def get():
    url = 'http://128.3.7.72:8000/accounts' 
    #params = {'count': count}
    #r = requests.get(url, params=params)
    r = requests.get(url)

    vpn = r.json()
    acc_id = vpn['results'][0]['accountid']
    acc_name = vpn['results'][0]['accountname']
    acc_time = vpn['results'][0]['updated']
    acc_alloc = vpn['results'][0]['accountallocation']
    acc_balance = vpn['results'][0]['accountbalance']
    acc_desc = vpn['results'][0]['description']
    vpn_return = {'acc_id' : acc_id, 'acc_name' : acc_name, 
                'acc_time' : acc_time, 'acc_desc' : acc_desc,
                'acc_alloc' : acc_alloc, 'acc_balance' : acc_balance}
    #vpn_return = {'count' : vpn['results'][0]['accountid']}

    #vpn_return = {'count' : vpn['results'][0]['accountid'],
    #            'results' : vpn['results']}

    print("\nvpn_return")
    print("acc_id: ", acc_id)
    print("\nacc_time: ", acc_time)
    #print("vpn_return['count']: ", vpn_return['count'])
    #print("vpn_return['results']: ", vpn_return['results'][0])
    print("-------------------\n")

    return vpn_return