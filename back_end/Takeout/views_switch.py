import json

from utils.dump import dump_item, dump_store, dump_comment
from utils.meta_wrapper import JSR
from django.views import View
from Takeout.models import *


class search(View):
    @JSR('code', 'message', 'items')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        return_list = []
        store = Store.objects.get(id=kwargs["store_id"])
        items = Item.objects.filter(name__icontains=kwargs["msg"], belonging_store=store)

        if len(items) == 0:
            return "404", "未找到相关商品"

        for i in items:
            return_list.append(dump_item(i))
        return "200", "success", return_list


class homepage(View):
    @JSR('code', 'message', 'info', 'items')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        store = Store.objects.get(id=kwargs["store_id"])

        items = Item.objects.filter(belonging_store=store).order_by('-sales')
        hot_items = []
        for i in range(min(5, len(items))):
            hot_items.append(dump_item(items[i]))
        store_info = dump_store(store)
        return "200", "success", store_info, hot_items


class goods(View):
    @JSR('code', 'message', 'items')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        store = Store.objects.get(id=kwargs["store_id"])

        items = Item.objects.filter(belonging_store=store).order_by('-sales')
        return_list = []
        for i in items:
            return_list.append(dump_item(i))

        return "200", "success", return_list


class comments(View):
    @JSR('code', 'message', 'comments')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        store = Store.objects.get(id=kwargs["store_id"])
        orders = Order.objects.filter(belonging_store=store)
        words = []
        for i in orders:
            word = Comment.objects.filter(belonging_order=i)
            if word:
                words.append(word[0])
        return_list = []
        for i in words:
            return_list.append(dump_comment(i))
        return "200", "success", return_list





