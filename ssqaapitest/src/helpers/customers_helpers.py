
from ssqaapitest.src.utilities.genericUtilities import generate_random_email_and_password
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility

class CustomerHelper(object):

    """
    1.This is a helper class and not a test class hence the __init__
    """
    def __init__(self):
        self.requests_utility = RequestsUtility()

    """
    1. Function to create customer and have the flexibility to pass default values for email and password as 'None'
    2. **kwargs for whatever else like payload that needs to be passed
    """
    def create_customer(self, email=None, password=None, **kwargs):

        if not email:
            ep= generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'Password1'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        # make API call here using a helper class
        create_user_json = self.requests_utility.post('customers', payload=payload, expected_status_code=201)
        return True