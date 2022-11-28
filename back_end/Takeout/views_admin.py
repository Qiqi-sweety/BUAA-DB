import json

from utils.meta_wrapper import JSR
from django.views import View
from Takeout.models import *
from utils.dump import dump_store, dump_item, dump_order, dump_comment


class displayInfo(View):
    @JSR('code', 'message', 'list')
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
                return_list.append(dump_store(i))
        if kind == "用户":
            items = Item.objects.all()
            for i in items:
                return_list.append(dump_item(i))
        if kind == "订单":
            orders = Order.objects.all()
            for i in orders:
                return_list.append(dump_order(i))
        if kind == "评论":
            comments = Comment.objects.all()
            for i in comments:
                return_list.append(dump_comment(i))
        return "200", "success", return_list


class validate(View):
    @JSR('code', 'message')
    def validate(self,request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        if not request.user.is_authenticated:
            return "403", "还没登录"
        stores = Store.objects.filter(isChecked=False)
        if len(stores) != len(kwargs["requests"]):
            return "300", "请求异常"
        for i in range(len(stores)):
            stores[i].isChecked = kwargs["requests"][i]
            stores[i].save()
        return "200", "success"
