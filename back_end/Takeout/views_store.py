import json

from utils.meta_wrapper import JSR
from utils.dump import *
from django.views import View
from Takeout.models import *


class homepage(View):
    @JSR('code', 'message', 'store_data', 'item_data')
    def post(self, request):
        # try:
        #     kwargs: dict = json.loads(request.body)
        # except Exception:
        #     return "400", "参数异常"

        if not request.user.is_authenticated:
            return "403", "店铺未登录"
        cookie = request.user
        store = cookie.store
        if cookie.type != "store":
            return "300", "店铺未登录"

        return_card = dump_store(store)
        return_list = []
        items = Item.objects.filter(belonging_store=store).order_by('-sales')
        num = min(5, len(items))
        for i in range(num):
            return_list.append(dump_item(items[i]))

        return "200", "success", return_card, return_list


class display_goods(View):
    @JSR('code', 'message', 'item_data')
    def post(self, request):
        if not request.user.is_authenticated:
            return "403", "店铺未登录"
        cookie = request.user
        store = cookie.store
        if cookie.type != "store":
            return "300", "店铺未登录"

        items = Item.objects.filter(belonging_store=store)
        return_list = []
        for i in items:
            return_list.append(dump_item(i))
        return "200", "success", return_list


class delete_good(View):
    @JSR('code', 'message', 'hint')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        if not request.user.is_authenticated:
            return "403", "店铺未登录", "error"

        item = Item.objects.get(id=kwargs["item_id"])
        item.delete()
        return "200", "删除成功", "success"


class add_good(View):
    @JSR('code', 'message', 'hint')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        if not request.user.is_authenticated:
            return "403", "店铺未登录", "error"
        cookie = request.user

        if cookie.type != "store":
            return "300", "店铺未登录", "error"

        item = Item(name=kwargs["name"], image=kwargs["image"], price=kwargs["price"], intro=kwargs["intro"],
                    belonging_store=request.user.store)

        item.save()

        return "200", "添加成功", "success"


class manage_orders(View):
    @JSR('code', 'message', 'list')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        if not request.user.is_authenticated:
            return "403", "店铺未登录"
        cookie = request.user
        store = cookie.store
        if cookie.type != "store":
            return "300", "店铺未登录"

        orders = Order.objects.filter(belonging_store=store, isProcessed=kwargs["isProcessed"])
        return_list = []
        for i in orders:
            return_list.append(dump_order(i))
        return "200", "success", return_list


class process_order(View):
    @JSR('code', 'message')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        order = Order.objects.get(id=kwargs["order_id"])
        order.isProcessed = True
        order.save()
        return "200", "处理成功"


class comments(View):
    @JSR('code', 'message', 'comment_list')
    def post(self, request):

        if not request.user.is_authenticated:
            return "403", "店铺未登录"
        cookie = request.user
        store = cookie.store
        if cookie.type != "store":
            return "300", "店铺未登录"

        orders = Order.objects.filter(belonging_store=store)
        words = []
        for i in orders:
            word = Comment.objects.get(belonging_order=i)
            words.append(word)
        return_list = []
        for i in words:
            return_list.append(dump_comment(i))
        return "200", "success", return_list


class show_info(View):
    @JSR('code', 'message', 'store_info')
    def post(self, request):
        if not request.user.is_authenticated:
            return "403", "店铺未登录"
        cookie = request.user
        store = cookie.store
        if cookie.type != "store":
            return "300", "店铺未登录"
        store_info = dump_store(store)
        store_info['license'] = store.license
        return "200", "success", store_info


class change_info(View):
    @JSR('code', 'message', 'hint')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        if not request.user.is_authenticated:
            return "403", "店铺未登录", "error"
        cookie = request.user
        store = cookie.store
        if cookie.type != "store":
            return "300", "店铺未登录", "error"

        kind = kwargs["type"]
        info = kwargs["info"]

        if kind == "name":
            if Cookie.objects.filter(name=info):
                return "300", "店铺名已存在", "error"
            else:
                print(store.store_name)
                store.store_name = info
                print(store.store_name)

        elif kind == "license":
            store.license = info
        elif kind == "logo":
            store.logo = info
        elif kind == "address":
            store.address = info
        elif kind == 'password':
            store.password = info
        elif kind == 'info':
            store.info = info
        else:
            return "404", "所选信息暂不支持修改", "error"
        store.save()
        return "200", "修改成功", "success"
