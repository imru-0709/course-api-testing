import pytest

from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import logging as logger

@pytest.mark.products
@pytest.mark.tcid24
def test_get_all_products():
    """
        1. This testcase will call the 'RequestsUtility() helper class.
        2. The helper class 'RequestsUtility()' has a 'get' method which returns a JSON response of GET call
        3. The 'get()' method takes the 'endpoint' value of needed for the 'get ' call which is 'products'
        4. The goal is to do an assert and confirm that the GET call response is not EMPTY.
        5. "assert req_response" makes sure to verify if the GET call response is EMPTY or NOT EMPTY
        """
    req = RequestsUtility()
    req_response = req.get( endpoint="products", payload=None, headers=None, expected_status_code=200)
 #   import pdb; pdb.set_trace()
    assert req_response != None, f"Get all products endpoint returned nothing"
    logger.debug(f"Response of list all: {req_response}")