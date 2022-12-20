import requests
import random
import string
import test_LR


def test_cart():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/cart/cart/"
    data = {
        "store_id": 2,
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()['code'] == '200')


def test_addItem():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/cart/addItem/"
    data = {
        "store_id": 1,
        "item_id": 3,
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()['code'] == '200')


def test_deleteItem():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/cart/deleteItem/"
    data = {
        "store_id": 2,
        "item_id": 3,
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()['code'] == '200')


def test_makeOrder():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/cart/makeOrder/"
    data = {
        "store_id": 3,
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()['code'] == '200')


if __name__ == '__main__':
    from test_LR import test_cookie_login
    test_cookie_login("user")
    test_makeOrder()

