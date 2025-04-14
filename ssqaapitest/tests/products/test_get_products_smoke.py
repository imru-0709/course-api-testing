import pytest

from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
from ssqaapitest.src.dao.products_dao import  ProductsDAO
from ssqaapitest.src.helpers.products_helper import ProductsHelper
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

@pytest.mark.products
@pytest.mark.tcid25
def test_get_product_by_id():

    #get a product from database
    dao = ProductsDAO()
    rand_product = dao.get_random_product_from_db(qty=1)
    rand_product_id = rand_product[0]['ID']
    db_name = rand_product[0]['post_title']

    #make the call
    product_helper = ProductsHelper()
    rs_api = product_helper.get_product_by_id(rand_product_id)
    api_name = rs_api['name']
    #import pdb; pdb.set_trace()

    #verify the response
    assert db_name == api_name, f"Get product by id returned wrong product. Id: {rand_product_id}" \
    f"Db name: {db_name}, Api name : {api_name}"