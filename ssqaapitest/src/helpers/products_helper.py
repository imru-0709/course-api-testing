from ssqaapitest.src.utilities.requestsUtility import RequestsUtility

class ProductsHelper(object):

    """
    1.This is a helper class and not a test class hence the __init__ which is a constrcutor
    """
    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_product_by_id(self, product_id):
        return self.requests_utility.get(f"products/{product_id}")

    def call_create_product(self, payload):
        rs_api = self.requests_utility.post('products', payload=payload, expected_status_code=201)
        return rs_api
