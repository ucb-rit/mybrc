from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .models import User

import requests
import xmltodict


class CASAuthentication (BaseAuthentication):

    PROXY_CAS_URL = 'https://auth.berkeley.edu/cas/proxyValidate'

    def authenticate(self, request):
        if 'proxyTicket' not in request.query_params or 'savio_username' not in request.query_params:
            return None

        try:
            user = User.objects.get(username=request.query_params['savio_username'])
        except User.DoesNotExist:
            raise AuthenticationFailed('User not found in REST database.')

        payload = {
            'ticket': requests.query_params['proxyTicket'],
            # TODO: Make an actual service URL.
            'service': 'foo'
        }
        cas_proxy_verification = requests.get(PROXY_CAS_URL, params=payload)

        if not cas_proxy_verification.ok:
            raise AuthenticationFailed('CAS proxy verification request failed.')

        response_dict = xmltodict.parse(cas_proxy_verification.text)['cas:serviceResponse']

        if 'cas:authenticationSuccess' not in response_dict:
            raise AuthenticationFailed('CAS proxy ticket invalid.')

        calnet_id = response_dict['cas:authenticationSuccess']['cas:user']

        if user.check_password(calnet_id):
            return (user, None)
        else:
            raise AuthenticationFailed('Calnet ID incorrect for given user.')