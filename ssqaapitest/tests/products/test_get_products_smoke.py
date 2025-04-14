import pytest

from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import logging as logger

@pytest.mark.products
@pytest.mark.tcid24
def test_get_all_products():
    req = RequestsUtility()
    req_response = req.get( endpoint="products", payload=None, headers=None, expected_status_code=200)
 #   import pdb; pdb.set_trace()
    assert req_response != None, f"Get all products endpoint returned nothing"
    logger.debug(f"Response of list all: {req_response}")