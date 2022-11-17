import json

from utils.dump import dump_store, dump_item
from utils.meta_wrapper import JSR
from django.views import View
from Takeout.models import *


class search(View):
    @JSR('code', 'message', 'list')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        msg = kwargs["msg"]
        return_list = []
        return_msg = ""

        if kwargs["type"] == "店铺":
            stores = Store.objects.filter(name__icontains=msg)
            if len(stores) == 0:
                return "404", "未匹配到相关店铺"
            for i in stores:
                return_list.append(dump_store(i))
        elif kwargs["type"] == "商品":
            items = Item.objects.filter(name__icontains=msg)
            stores = items.values('belonging_store').distinct()
            if len(items) == 0:
                return "404", "未匹配到相关商品"
            for i in stores:
                res = {"store": dump_store(i)}
                items = Item.objects.filter(belonging_store=i)
                item_cards = []
                for j in items:
                    item_cards.append(dump_item(j))
                res["items"] = item_cards
                return_list.append(res)
        else:
            return "403", "前端查询类别有误"

        return "200", return_msg, return_list


class recommend(View):
    @JSR('recommended_stores')
    def post(self, request):
        stores = Store.objects.all().order_by('-sales', '-star')
        return_list = []
        for i in stores:
            return_list.append(dump_store(i))
        return return_list

    # TODO 调用推荐算法实现推荐功能
