import json

from back_end.utils.meta_wrapper import JSR
from django.views import View
from models import *


class search(View):
    @JSR('hint')
    def search(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        msg = kwargs["msg"]
        return_list = []
        return_msg = ""
        items = Item.objects.filter(name__icontains=msg)
        if len(items) == 0:
            return_msg += "未找到相关商品"
        else:
            return_msg += "成功找到相关商品"
            for i in items:
                name = i.name
                image = i.image
                price = i.price
                sales = i.sales
                tmp = [name, image, price, sales]
                return_list.append(tmp)
        return return_msg, return_list


class homepage(View):
    @JSR('hint')
    def get(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        store = kwargs["store"]
        return_card = {'name': store.name, 'logo': store.logo, 'star': store.star, 'sales': store.sales,
                       'address': store.address, 'info': store.info}
        items = Item.objects.filter(belonging_store=store).order_by('-sales')
        return_list = []
        for i in range(5):
            tmp_list = {'name': items[i].name, 'image': items[i].image, 'price': items[i].price,
                        'sales': items[i].sales}
            return_list.append(tmp_list)

        return return_card, return_list


class goods(View):
    @JSR('hint')
    def get(self, request):
        items = Item.objects.all().order_by('-sales')
        return_list = []
        for i in items:
            tmp_list = {'name': i.name, 'image': i.image, 'price': i.price, 'sales': i.sales, 'intro': i.intro}
            return_list.append(tmp_list)
        return return_list


class cart(View):
    @JSR('hint')
    def get(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        user = kwargs["user"]
        carts = Cart.objects.filter(user=user)
        cart = carts[0]
        items = cart.items
        return_list = []
        return_sum = 0
        for i in items:
            tmp_list = {'name': i.name, 'image': i.image, 'price': i.price, 'sales': i.sales}
            return_sum += i.price
            return_list.append(tmp_list)

        return return_list, return_sum


class comments(View):
    @JSR('hint')
    def get(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        store = kwargs["store"]
        words = Comment.objects.filter(belonging_store=store)
        return_list = []
        for i in words:
            user = i.user
            tmp_list = {'user': user.name, 'image': user.image, 'star': i.star, 'comment': i.comment, 'time': i.time}
            return_list.append(tmp_list)
        return return_list
