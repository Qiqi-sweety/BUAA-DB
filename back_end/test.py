import requests

def update_image_test():
    url="http://127.0.0.1:8000/image/update/"
    requests.post(url,files={"image":open("test.jpg","rb")})

def main():
    update_image_test()

if __name__ == "__main__":
    main()