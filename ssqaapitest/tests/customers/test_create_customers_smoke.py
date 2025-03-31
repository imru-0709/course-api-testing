import pytest
import logging as logger
from ssqaapitest.src.dao.customers_dao import CustomersDAO
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility

import setuptools

from ssqaapitest.src.utilities.genericUtilities import generate_random_email_and_password
from ssqaapitest.src.helpers.customers_helpers import CustomerHelper
#from setuptools import setup, find_packages

#setup(name="ssqaapitest", version="0.1", packages=find_packages())

@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_only_email_password():

    logger.info("TEST: Create new customer with email and password only")
    logger.debug("TEST: Create new customer with email and password only")

    """
    1. There should be one email per user. 
    2. Hence we need a helper class to generate random email address for each user
    3. Helper class 'generate_random_email_and_password()' returns a dictionary to 'rand_info'
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

    # verify the status code of the call - this is already taken care of in requestutility()
    # verify the email and first name in the response - this is already taken care of
    """
    1. Making connection to Database and making a call to Database will be a helper class 'get_customer_by_email()'
    2. the goal is to compare the ID returned by Database helper class ( id_in_db = cust_info[0]['ID']) 
    is the same as the ID returned by API call (id_in_api = cust_api_info['id'])
    """
    # verify the customer is created in the database
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)
    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']

    assert id_in_api == id_in_db, f'Create customer response "id" not same as "ID" in database' \
                                f'Email:{email}'

@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():
   # get existing email from DB
   """
   1. A random existing customer will be returned by helper method - 'get_random_customer_from_db()'
   2. Then we get the user_email of that existing customer and store it in 'existing_email'
   3. payload is created with and existing email and hardcoded password = Password1
   4. then a POST call is made with endpoint = 'customers' and the payload that was created
        and a status code = 400
   5. The goal is we expect the POST call to fail since the customer already exists and give a 400 error.
   6. also assert on the text 'registration-error-email-exists'
    """
   cust_dao = CustomersDAO()
   existing_cust = cust_dao.get_random_customer_from_db()
   existing_email = existing_cust[0]['user_email']

   # call the api
   req_helper = RequestsUtility()
   payload = {"email": existing_email, "password": "Password1"}
   cust_api_info = req_helper.post(endpoint='customers', payload=payload, expected_status_code=400 )
   assert cust_api_info['code'] == 'registration-error-email-exists', f"Create customer with" \
    f"existing user error 'code' is not correct. Expected : 'registration-error-email-exists' " \
    f"Actual: {cust_api_info['code']}"

 #  import pdb;pdb.set_trace()

   # assert cust_api_info['message'] == f"'An account is already registered with {existing_email}. Please log in or use a different email address.'" , \
   #  f"Expected : An account is already registered with {existing_email}. Please log in or use a different email address." \
   #  f"Actual: {cust_api_info['message']}"



