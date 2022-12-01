import requests
import random
import string
import test_LR


def test_cart():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/cart/cart/"
    data = {
        "store_id": 33,
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()['code'] == '200')