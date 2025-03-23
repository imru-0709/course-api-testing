import logging as logger
import random
import string
from string import ascii_lowercase

"""
1. this will generate an email with a pre-fix 'testuser' and the random string followed by domain 'supersqa.com
2. domain and email_prefix is None so that we can customize and pass into this method if the tester wants
3. if 'domain' and/or 'email_prefix' has no value then default values have been provided : 'supersqa.com' and 'testuser' respectively
4. 'random.choices()' will be used to create a random string of length 10
5. email is 'email_prefix' followed by random string and 'domain'
6. 'password_string' is also using 'random.choices()' and creates a random string of length 10
7. random_info is a dictionary which contains the email and password
"""
def generate_random_email_and_password(domain=None, email_prefix=None):
    logger.debug("Generating random email and password")

    if not domain:
        domain = 'supersqa.com'
    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))

    email = email_prefix + '_' + random_string + '@' + domain

    password_length = 20

    password_string = ''.join(random.choices(ascii_lowercase, k = password_length))

    random_info = {'email': email, 'password': password_string}
    logger.debug(f"Randomly generated email and password are: {random_info}")

    return random_info