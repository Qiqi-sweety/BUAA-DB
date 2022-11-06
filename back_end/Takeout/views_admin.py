import json

from back_end.utils.meta_wrapper import JSR
from django.views import View
from models import *


class displayInfo(View):
    @JSR('hint')
    def display(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        kind = kwargs["kind"]
        return_list = []
        if kind == "店铺":
            stores = Store.objects.all()
            for i in stores:
                tmp = [i.name, i.address, i.logo, i.sales]
                return_list.append(tmp)
            return return_list
        elif kind == "用户":
            items = Item.objects.all()
            for i in items:
                tmp = [i.name, i.address, i.image, i.card_num]
                return_list.append(tmp)
            return return_list
        elif kind == "订单":
            orders = Order.objects.all()
            for i in orders:
                tmp = [i.id, i.belonging_user, i.belonging_store, i.time, i.money]
                return_list.append(tmp)
            return return_list
        else:
            comments = Comment.objects.all()
            for i in comments:
                tmp = [i.belonging_order.id, i.belonging_user, i.belonging_store, i.time, i.star]
                return_list.append(tmp)
            return return_list


def valid(store):
    # TODO
    return True


class check(View):
    @JSR('hint')
    def check(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        stores = Store.objects.filter(isChecked=False)
        for i in stores:
            if valid(i):
                i.isChecked = True
                i.save()
