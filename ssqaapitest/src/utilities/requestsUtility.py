
from ssqaapitest.src.configs.hosts_config import API_HOSTS
from ssqaapitest.src.utilities.credentialsUtility import  CredentialsUtility
import requests
import json
import os
import logging as logger
from requests_oauthlib import OAuth1
class RequestsUtility(object):
    """
    1. create a self.auth with OAuth1 library by passing consumer key and secret key
    2. set environment as test by default
    3. set the base.url value
    """
    def __init__(self):
    #    wc_creds = CredentialsUtility.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1('ck_1ae3bf3449ec1fae7e646bc633af8489ae787e5c','cs_ed6149672b676398eb83927109c177791b076571')
      #  self.auth = OAuth1(wc_creds['wc_key'], wc_creds['wc_secret'])

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code , f"Bad status code, expected is {self.expected_status_code}, actual status code us {self.status_code}" \
         f"url: {self.url}, Response Json: {self.rs_json}"

    """
    1. 'payload' can be None
    2. if 'headers' is None then set the 'headers' to 'application/json'
    3. 'expected_status_code'= 200 is present as a default value in the method signature
    4. self.url is created by appending the base_url to the endpoint
    5. POST request is made by passing the url, the data in JSON format, the header and auth ( consumer key and secret key)
    6. setting self.status_code as the status code received from POST call response
    7. setting the 'self.expected_status_code' as 'expected_status_code' from the function call
    8. setting the 'self.rs_json' as 'rs_ap.json()' which is the JSON response of the POST call
    9. Asserting when comparing the expected status code and the POST call status code ( ie. self.status_code)
    """
    def post(self, endpoint, payload=None, headers=None, expected_status_code = 200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        assert self.status_code == int(expected_status_code), \
            f'Expected status code {expected_status_code} but actual {self.status_code}'

        self.assert_status_code()
        logger.debug(f"API response: {self.rs_json}")
        return self.rs_json


    def get(self):
        pass