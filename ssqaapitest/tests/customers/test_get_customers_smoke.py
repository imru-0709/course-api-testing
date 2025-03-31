

import pytest
import logging as logger
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility


@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():
    """
    1. This testcase will call the 'RequestsUtility() helper class.
    2. The helper class 'RequestsUtility()' has a 'get' method which returns a JSON response of GET call
    3. The 'get()' method takes the 'endpoint' value of needed for the 'get ' call which is 'customers'
    4. The goal is to do an assert and confirm that the GET call response is not EMPTY.
    5. "assert rs_api" makes sure to verify if the GET call response is EMPTY or NOT EMPTY
    """
    req_helper = RequestsUtility()
    rs_api = req_helper.get('customers')
 #   logger.debug(f"Response of list all: {rs_api}")
    assert rs_api, f"Response of list all customers is empty"

