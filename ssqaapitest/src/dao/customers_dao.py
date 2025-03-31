
from ssqaapitest.src.utilities.dbUtility.dbUtility import DBUtility
import random

class CustomersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    """
    1. The goal is to run the SQL command to query the table 'users' and find the row entry in the table for the emailID {email}
    2. Then using inbuilt libraries get the response into a dict 'rs_sql'
    3. Return the dict 'rs_sql' back to the function that is calling it.
    """
    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM local.wp_users WHERE user_email = '{email}';"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    """
    1. The goal is to run the SQL command to query the table 'users' and 
       order the customers by ID in descending order and limit by 5000
    2. Then using inbuilt libraries get the response into a dict 'rs_sql'
    3. run a 'random()' to choose a single (since qty will be 1) customer ID - random.sample(rs_sql, int(qty))
    3. Return the randomly selected customer based on the randomly selected ID.
    """
    def get_random_customer_from_db(self, qty=1):
        sql = f"SELECT * FROM local.wp_users ORDER BY id DESC LIMIT 5000;"
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))