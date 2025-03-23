import pytest
import logging as logger

import setuptools

from ssqaapitest.src.utilities.genericUtilities import generate_random_email_and_password
from ssqaapitest.src.helpers.customers_helpers import CustomerHelper
#from setuptools import setup, find_packages

#setup(name="ssqaapitest", version="0.1", packages=find_packages())
@pytest.mark.tcid29
def test_create_customer_only_email_password():

    logger.info("TEST: Create new customer with email and password only")
    logger.debug("TEST: Create new customer with email and password only")

    """
    1. There should be one email per user. 
    2. Hence we need a helper class to generate random email address for each run
    3. Helper class returns a dictionary to 'rand_info'
    4. email is stored from rand_info['email'] and password is stored from rand_info['password']
    5. payload also consists of the random email generated and the random password generated
    """

    rand_info = generate_random_email_and_password()
    logger.info(rand_info)
    email = rand_info['email']
    password = rand_info['password']

    #create payload

    """
    1. Need a helper class to make the call
    """
    #make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # verify the status code of the call

    # verify the email in the response

    """
    1. Making connection to Database and making a call to Database will be a helper class
    """
    # verify the customer is created in the database
