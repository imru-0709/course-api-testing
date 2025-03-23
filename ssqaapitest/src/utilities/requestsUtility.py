
from ssqaapitest.src.configs.hosts_config import API_HOSTS
from ssqaapitest.src.utilities.credentialsUtility import  CredentialsUtility
import requests
import json
import os
from requests_oauthlib import OAuth1
class RequestsUtility(object):

    def __init__(self):

    #    wc_creds = CredentialsUtility.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]

        self.auth = OAuth1('ck_1ae3bf3449ec1fae7e646bc633af8489ae787e5c','cs_ed6149672b676398eb83927109c177791b076571')
      #  self.auth = OAuth1(wc_creds['wc_key'], wc_creds['wc_secret'])

    def post(self, endpoint, payload=None, headers=None, expected_status_code = 200):

        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        assert self.status_code == int(expected_status_code), \
            f'Expected status code {expected_status_code} but actual {self.status_code}'
        return rs_api.json()


    def get(self):
        pass