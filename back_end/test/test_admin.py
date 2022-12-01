import requests
import random
import string
import test_LR


def test_displayInfo():
    #TODO err!
    login = test_LR.test_cookie_login("admin")
    cookie=login.cookies
    url = "http://127.0.0.1:8000/admin/displayInfo/"
    data = {
        "kind": "店铺",
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == '200')


def test_validate():
    # todo not yet
    login = test_LR.test_cookie_login("admin")
    cookie = login.cookies
    url = "http://127.0.0.1:8000/admin/validate/"
