import pytest

pytestmark = [pytest.mark.be]

@pytest.fixture(scope='module')
def setup_steps():
    print("")
    print(">>>>>SETUP<<<<<")

@pytest.mark.smoke
def test_login_page_valid_user(setup_steps):
    print("Login with valid user")
    print("Function: aaaaaaa")

def test_login_page_wrong_password():
    print("Login with wrong password")
    print("Function: bbbbbbbbbb")