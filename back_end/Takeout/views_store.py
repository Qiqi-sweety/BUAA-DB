import json

from back_end.utils.meta_wrapper import JSR
from django.views import View
from models import *


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


class manage_goods(View):
    @JSR('hint')
    def get(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        store = kwargs["store"]
        items = Item.objects.filter(belonging_store=store)
        return_list = []
        for i in items:
            tmp_list = {'name': i.name, 'image': i.image, 'price': i.price, 'sales': i.sales}
            return_list.append(tmp_list)
        return return_list


class delete_good(View):
    @JSR('hint')
    def get(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        item = kwargs["item"]
        item.delete()
        return "删除成功"


class add_good(View):
    @JSR('hint')
    def get(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        store = kwargs["store"]
        name = kwargs["name"]
        price = kwargs["price"]
        intro = kwargs["intro"]
        image = kwargs["image"]
        Item.objects.create(name=name, price=price, intro=intro, image=image, belonging_store=store)
        return "添加成功"


class manage_orders(View):
    @JSR('hint')
    def get(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        store = kwargs["store"]
        isProcessed = kwargs["isProcessed"]
        orders = Order.objects.filter(belonging_store=store, isProcessed=isProcessed)
        return_list = []
        for i in orders:
            res = []
            for j in i.items.all():
                tmp_list = {'name': j.name, 'image': j.image, 'price': j.price, 'sales': j.sales}
                res.append(tmp_list)
            tmp_list = {'goods': res, 'time': i.time, 'money': i.money}
            return_list.append(tmp_list)
        return return_list


class process(View):
    @JSR('hint')
    def get(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        order = kwargs["order"]
        order.isProcessed = True
        order.save()
        return "处理成功"


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


class manage(View):
    @JSR('hint')
    def get(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        store=Store.objects.get(name=kwargs["store"])
        return_dict = {'name': store.name, 'address':store.address,'password':store.password,'logo': store.logo, 'info': store.info,'license':store.license}
        return return_dict


class changeInfo(View):
    @JSR('hint')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        kind = kwargs["type"]
        info = kwargs["info"]
        store=Store.objects.get(name=kwargs["store"])
        return_msg = "修改成功"
        if kind == "name":
            if Store.objects.filter(name=info):
                return_msg = "店铺名已存在"
            else:
                store.name = info
        elif kind == "image":
            store.image = info
        elif kind == "address":
            store.address = info
        elif kind == "logo":
            store.logo = info
        elif kind == 'password':
            store.password = info
        elif kind == 'info':
            store.info = info
        elif kind == 'license':
            store.license = info
        else:
            return_msg = "修改失败"
        return return_msg

