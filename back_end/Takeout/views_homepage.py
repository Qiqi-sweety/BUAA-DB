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
            stores = Store.objects.filter(store_name__icontains=msg,isChecked=True)
            if len(stores) == 0:
                return not_found(kwargs["type"])
            for i in stores:
                return_list.append(dump_store(i))
            return "200", return_msg, return_list
        elif kwargs["type"] == "商品":
            items = Item.objects.filter(name__icontains=msg,belonging_store__isChecked=True)
            stores = items.values('belonging_store').distinct()
            res_list = []
            if len(items) == 0:
                return not_found(kwargs["type"])
            for i in stores:
                temp = {
                    "store": dump_store(Store.objects.get(id=i["belonging_store"])),
                    "items": []
                }
                print(i)
                items = Item.objects.filter(belonging_store__id=i["belonging_store"])
                for j in items[0:3]:
                    temp["items"].append(dump_item(j))
                res_list.append(temp)
            return "200", return_msg, res_list
        else:
            return "403", "前端查询类别有误"


class recommend(View):
    @JSR('recommended_stores')
    def post(self, request):
        stores = Store.objects.filter(isChecked=True).order_by('-sales', '-star')
        return_list = []
        for i in stores:
            return_list.append(dump_store(i))
        print(return_list)
        return return_list

    # TODO 调用推荐算法实现推荐功能
