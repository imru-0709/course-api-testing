
from ssqaapitest.src.utilities.genericUtilities import generate_random_email_and_password
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility

class CustomerHelper(object):

    """
    1.This is a helper class and not a test class hence the __init__
    """
    def __init__(self):
        self.requests_utility = RequestsUtility()
    """
    1. Function to create customer and have the flexibility to pass default values for email and password as 'None' or the tester can pass a customized email
    2. **kwargs for whatever else like payload that needs to be passed - like username, address, etc.
    """
    def create_customer(self, email=None, password=None, **kwargs):
        """
        1. payload is a dictionary which defines the bare minimum - email and password and also updates with kwargs
        :param email:If email is not present then call the utility 'generate_random_email_and_password()'
        :param password: is hardcoded as 'password1' because password may get encrypted (unlike email) and it can be difficult for tester to regenerate a
        bug for Dev team using the credentials if password is encrypted
        :param kwargs: this can be all the other data which are part of payload
        :return: it will return a dictionary
        """
        if not email:
            ep= generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'Password1'
        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        """
        1. make API call here using a helper class - requestsUtility()
        2. 'create_user_json' contains POST call response from 'requestsUtility()'
        3. for the POST call,the end point is 'customers' and payload is passed from above and the status code is 201 since a new customer has been created
        """

        create_user_json = self.requests_utility.post('customers',payload =payload, expected_status_code=201)
        return create_user_json