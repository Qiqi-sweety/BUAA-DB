import requests
import random
import string
import test_LR


def test_user_info():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/statistic/user_info"
    r = requests.post(url, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == "200")


def test_store_info():
    login = test_LR.test_cookie_login("store")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/statistic/store_info"
    r = requests.post(url, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == "200")


def test_admin_info():
    url = "http://127.0.0.1:8000/statistic/admin_info"
    r = requests.post(url)
    print(r.json())
    assert (r.json()["code"] == "200")
