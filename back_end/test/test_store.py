import requests
import random
import string
import test_LR


def test_add_good():
    # session = requests.session()
    login = test_LR.test_cookie_login()
    print(login.cookies)
    cookie = login.cookies

    url = "http://127.0.0.1:8000/store/add_good/"
    data = {
        'name': "奶茶",
        'image': "/media/bread.jpg",
        'price': 5,
        'intro': "好喝",
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    # assert (r.json()["code"] == "200")


def test_delete_good():
    # session = requests.session()
    login = test_LR.test_cookie_login()
    cookie = login.cookies

    url = "http://127.0.0.1:8000/store/delete_good/"
    data = {
        "item_id": 1,
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == "200")


def test_homepage():
    login = test_LR.test_cookie_login()
    cookie = login.cookies

    url = "http://127.0.0.1:8000/store/homepage/"
    r = requests.post(url, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == "200")


def test_display_goods():
    login = test_LR.test_cookie_login()
    cookie = login.cookies

    url = "http://127.0.0.1:8000/store/display_goods/"
    r = requests.post(url, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == "200")


def test_process_order():
    login = test_LR.test_cookie_login()
    cookie = login.cookies

    url = "http://127.0.0.1:8000/store/process_order/"
    date = {
        "order_id": 1,
    }
    r = requests.post(url, json=date, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == "200")


def test_manage_orders():
    login = test_LR.test_cookie_login()
    cookie = login.cookies

    url = "http://127.0.0.1:8000/store/manage_orders/"
    date = {
        "isProcessed": True,
    }
    r = requests.post(url, json=date, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == "200")


def test_show_info():
    login = test_LR.test_cookie_login()
    cookie = login.cookies

    url = "http://127.0.0.1:8000/store/show_info/"
    r = requests.post(url, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == "200")


def test_change_info():
    login = test_LR.test_cookie_login()
    cookie = login.cookies

    url = "http://127.0.0.1:8000/store/change_info/"
    data = {
        "type": "name",
        "info": "why not you re all right"
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == "200")


def test_comments():
    login = test_LR.test_cookie_login()
    cookie = login.cookies

    url = "http://127.0.0.1:8000/store/comments/"
    r = requests.post(url, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == "200")