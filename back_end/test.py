import requests
import random
import string
def random_string(l=10):
    return ''.join(random.sample(string.ascii_letters + string.digits, l))
def create_store_test():
    # step 1. the url you want to post
    url="http://127.0.0.1:8000/store/register/step2/"
    # step 2. the parameters you want to post in json or python dictionary
    data = {
        "name": random_string(5),
        "password": "123",
        "logo": "/media/123.jpg",
        "address": "123",
        "info": "123",
        "license": "/media/123.jpg"
    }
    # step 3. post the data
    r = requests.post(url, json=data)
    # step 4. print the response

def recommend_test():
    url="http://127.0.0.1:8000/homepage/recommend"
    requests.post(url)
def main():
    recommend_test()

if __name__ == "__main__":
    main()