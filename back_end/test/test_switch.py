import requests
import random
import string
import test_LR


def random_string(l=10):
    return ''.join(random.sample(string.ascii_letters + string.digits, l))


def test_search():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/switch/search/"
    data = {
        "msg": "奶茶",
        "store_id": 2,
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()['code'] == '200')


def test_homepage():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/switch/homepage/"
    data = {
        "store_id": 2,
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()['code'] == '200')


def test_goods():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/switch/goods/"
    data = {
        "store_id": 2,
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()['code'] == '200')


def test_comments():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/switch/comments/"
    data = {
        "store_id": 2,
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()['code'] == '200')


def test_add_to_cart():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/switch/addToCart"
    data = {
        "store_id": 2,
        "item_id": 2,
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()['code'] == '200')


def test_make_order():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/switch/makeOrder"
    data = {
        "store_id": 2,
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()['code'] == '200')