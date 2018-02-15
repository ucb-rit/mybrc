from django.shortcuts import render, HttpResponse
import requests
import os, os.path, json


def get():
    url = 'http://128.3.7.72:8000/accounts' 
    #params = {'count': count}
    #r = requests.get(url, params=params)
    r = requests.get(url)

    vpn = r.json()
    vpn_return = {'count': vpn['count']}
    return vpn_return