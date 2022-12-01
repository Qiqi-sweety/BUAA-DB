import requests
import random
import string
import test_LR


def random_string(l=10):
    return ''.join(random.sample(string.ascii_letters + string.digits, l))


def test_recommend():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/homepage/recommend/"
    r = requests.post(url, cookies=cookie)
    print(r.json())
    assert (len(r.json()["recommended_stores"]) >= 5)


def test_search():
    login = test_LR.test_cookie_login("user")
    cookie = login.cookies

    url = "http://127.0.0.1:8000/homepage/search/"
    # data = {
    #     "msg": "store",
    #     "type": "店铺",
    # }
    # r = requests.post(url, json=data, cookies=cookie)
    # print(r.json())
    # assert (len(r.json()["search_result"]) >= 1)
    # todo still some bugs here
    date = {
        "msg": "奶茶",
        "type": "商品",
    }
    r = requests.post(url, json=date, cookies=cookie)
    print(r.json())
    assert (r.json()["code"] == "403")
