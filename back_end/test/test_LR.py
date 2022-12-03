import requests
import random
import string


def random_string(l=10):
    return ''.join(random.sample(string.ascii_letters + string.digits, l))


def test_user_register():
    url = "http://127.0.0.1:8000/user/register/"
    data = {
        "name": random_string(5),
        "address": random_string(20),
        "card_num": random_string(10),
        "password": "123456",
    }
    r = requests.post(url, json=data)
    print(r.json())
    assert (r.json()["code"] == "200")


def test_store_register_step2():
    url = "http://127.0.0.1:8000/store/register/step2/"
    data = {
        "name": random_string(5),
        "password": "123456",
        "logo": "/media/123.jpg",
        "address": "123",
        "info": "123",
        "license": "/media/123.jpg"
    }
    r = requests.post(url, json=data)
    print(r.json())
    assert (r.json()["code"] == "200")


def test_cookie_login(type="store"):
    session = requests.session()

    url = "http://127.0.0.1:8000/login/"

    if type == "user":
        data = {
            "name": "user_123",
            "password": "123456",
        }
    elif type == "store":
        data = {
            "name": "store_zhy",
            "password": "123456",
        }
    else:
        data = {
            "name": "admin",
            "password": "ADMIN",
        }

    r = session.post(url, json=data)
    print(r)
    assert (r.json()["code"] == "200")
    return r


def test_set_admin():
    url = "http://127.0.0.1:8000/set_admin/"
    r = requests.post(url)
    print(r.json())


# def test_update_photo():
#     login = test_cookie_login()
#     cookie = login.cookies
#
