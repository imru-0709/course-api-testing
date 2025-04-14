import pytest

from ssqaapitest.src.utilities.genericUtilities import generate_random_string
from ssqaapitest.src.helpers.products_helper import ProductsHelper
from ssqaapitest.src.dao.products_dao import ProductsDAO

@pytest.mark.products
@pytest.mark.tcid26
def test_create_1_simple_product():


#generate some data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"

#make the call
    product_rs = ProductsHelper().call_create_product(payload)

#verify the response is not empty
    assert product_rs, f"Create product api response is empty. Payload is : {payload}"
    assert product_rs['name'] == payload['name'], f"Create product api call response has unexpected name"\
        f"Expected :{payload['name']}, Actual is : {product_rs['name']} "

#verify the product exists in db
    product_id = product_rs['id']
    db_products = ProductsDAO()
    db_product = db_products.get_product_by_id(product_id)
    assert payload['name'] == db_product[0]['post_title'], f"Create product title in db doesnto match" \
        f" title in DB. DB: {db_product['post_title']}, API: {payload['name']}"