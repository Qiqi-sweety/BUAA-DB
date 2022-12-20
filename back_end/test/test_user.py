import requests
import random
import string
import test_LR


def test_showOrders():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/user/showOrders/"
    r = requests.post(url, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == '200')


def test_write_comments():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/user/writeComments/"
    data = {
        "order_id": 18,
        "content": "不咋地",
        "star": 1,
        "photo": "/media/milktea.jpg",
    }
    r=requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == '200')


def test_myComments():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/user/myComments/"
    r = requests.post(url, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == '200')


def test_manage():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/user/manage/"
    r = requests.post(url, cookies=cookie)
    print(r.json())

    assert (r.json()["code"] == '200')


def test_change_info():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/user/changeInfo/"
    data = {
        "type": "password",
        "info": "123456",
        "info2":"234567"
    }
    r = requests.post(url, json=data, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == '200')