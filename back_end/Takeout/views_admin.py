import json

from utils.meta_wrapper import JSR
from django.views import View
from Takeout.models import *
from utils.dump import dump_store, dump_item, dump_order, dump_comment, dump_user


class displayInfo(View):
    @JSR('code', 'message', 'list')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        if not request.user.is_authenticated:
            return "403", "还没登录"

        kind = kwargs["kind"]
        isChecked = kwargs["isChecked"] if "isChecked" in kwargs else True
        return_list = []
        if kind == "店铺":
            stores = Store.objects.filter(isChecked=isChecked)
            if not isChecked:
                for i in stores:
                    s = dump_store(i)
                    s['license'] = i.license
                    return_list.append(s)
            else:
                for i in stores:
                    return_list.append(dump_store(i))
        if kind == "用户":
            users = User.objects.all()
            for i in users:
                orders = Order.objects.filter(belonging_user=i)
                tmp = dump_user(i)
                tmp["order_count"] = len(orders)
                return_list.append(tmp)
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
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        if not request.user.is_authenticated:
            return "403", "还没登录"

        store = Store.objects.get(id=kwargs["store_id"])
        store.isChecked = True
        store.save()

        return "200", "success"
