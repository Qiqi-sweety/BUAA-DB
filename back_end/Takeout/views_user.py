import json

from back_end.utils.meta_wrapper import JSR
from django.views import View
from models import *


class home_search(View):
    @JSR('hint')
    def search(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        name = kwargs["type"]
        msg = kwargs["msg"]
        return_list = []
        return_msg = ""
        if name == "店铺":
            stores = Store.objects.filter(name__icontains=msg)
            if len(stores) == 0:
                return_msg += "未匹配到相关店铺"
            else:
                return_msg += "成功匹配到相关店铺"
                for i in stores:
                    name = i.name
                    logo = i.logo
                    star = i.star
                    sales = i.sales
                    tmp = [name, logo, star, sales]
                    return_list.append(tmp)
            return return_msg, return_list
        else:
            items = Item.objects.filter(name__icontains=msg)
            stores = items.values('belonging_store')
            if len(items) == 0:
                return_msg += "未匹配到相关店铺"
            else:
                return_msg += "成功匹配到相关店铺"
                return_list = []
                for i in stores:
                    res = {}
                    store_name = i.name
                    store_logo = i.logo
                    store_star = i.star
                    store_sales = i.sales
                    tmp = [store_name, store_logo, store_star, store_sales]
                    res["store"] = tmp
                    for j in items:
                        if j.belonging_store == i:
                            item_name = j.name
                            item_price = j.price
                            item_image = j.image
                            tmp = [item_name, item_price, item_image]
                            res["item"].append(tmp)
                    return_list.append(res)
            return return_msg, return_list


class recommender(View):
    @JSR('hint')
    def recommend(self, request):
        stores = Store.objects.all()
        stores = stores.order_by('-star')
        return_list = []
        for i in stores:
            name = i.name
            logo = i.logo
            star = i.star
            sales = i.sales
            tmp = [name, logo, star, sales]
            return_list.append(tmp)
        return return_list
