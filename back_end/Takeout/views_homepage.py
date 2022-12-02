import json

from utils.dump import dump_store, dump_item
from utils.meta_wrapper import JSR
from django.views import View
from Takeout.models import *


class search(View):
    @JSR('code', 'message', 'store_list', 'item_list')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        msg = kwargs["msg"]
        return_list = []
        return_msg = "success"

        def not_found(type):
            stores = Store.objects.all().order_by('-sales', '-star')
            return_list = []
            for i in stores:
                return_list.append(dump_store(i))
            return "404", f"未匹配到相关{type}", return_list

        if msg == "":
            return not_found(kwargs["type"])

        if kwargs["type"] == "店铺":
            stores = Store.objects.filter(store_name__icontains=msg)
            if len(stores) == 0:
                return not_found(kwargs["type"])
            for i in stores:
                return_list.append(dump_store(i))
            return "200", return_msg, return_list
        elif kwargs["type"] == "商品":
            items = Item.objects.filter(name__icontains=msg)
            stores = items.values('belonging_store').distinct()
            store_list = []
            items_list = []
            if len(items) == 0:
                return not_found(kwargs["type"])
            for i in stores:
                store_list.append(dump_store(i))
                print(dump_store(i))
                items = Item.objects.filter(belonging_store=i)
                item_cards = []
                for j in items:
                    item_cards.append(dump_item(j))
                items_list.append(item_cards)
            return "200", return_msg, store_list, items_list
        else:
            return "403", "前端查询类别有误"


class recommend(View):
    @JSR('recommended_stores')
    def post(self, request):
        stores = Store.objects.all().order_by('-sales', '-star')
        return_list = []
        for i in stores:
            return_list.append(dump_store(i))
        print(return_list)
        return return_list

    # TODO 调用推荐算法实现推荐功能
