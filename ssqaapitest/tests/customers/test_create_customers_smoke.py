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
    2. The email from above and the password from above will be passed as arguments to the 'cust_obj.create_customer()' method
    3. Then the return value is a dictionary which is stored in 'cust_api_info'
    4. Then we do an assert on the email id and also to make sure that the new customer created does not have a first name
    """
    #make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)
    assert cust_api_info['email'] == email , f"Create customer api return wrong email. Email: {email}"
    assert cust_api_info['first_name'] == '' , f" Create customer api returned value for first name but it should be empty"

    # verify the status code of the call - this is already taken care of in requestutl
    # verify the email and first name in the response - this is already taken care of
    """
    1. Making connection to Database and making a call to Database will be a helper class
    """
    # verify the customer is created in the database
