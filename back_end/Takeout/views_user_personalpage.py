import json
from datetime import timezone

from back_end.utils.meta_wrapper import JSR
from django.views import View
from models import *


class showOrders(View):
    @JSR('hint')
    def get(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        user = User.objects.get(name=kwargs["user"])
        orders = Order.objects.filter(user=user)
        return_list = []
        for i in orders:
            item_list = []
            items = i.items.all()
            for j in items:
                tmp = [j.name, j.price, j.image]
                item_list.append(tmp)
            tmp_list = {"order_id": i.id, "store": i.store.name, "items": item_list, "time": i.time, "total": i.total}
            return_list.append(tmp_list)
        return return_list


class writeComment(View):
    @JSR('hint')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        order = kwargs["order"]
        star = kwargs["star"]
        content = kwargs["content"]
        photo = kwargs["photo"]

        comment = Comment(info=content, star=star, time=timezone.now(), image=photo, belonging_order=order,
                          belonging_store=order.store, belonging_user=order.user)
        comment.save()
        return "评论成功"


class myComment(View):
    @JSR('hint')
    def get(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        user = User.objects.get(name=kwargs["user"])
        comments = Comment.objects.filter(belonging_user=user)
        return_list = []
        for i in comments:
            store = i.belonging_store
            tmp_list = {'order_id': i.belonging_order.id, "store_name": store.name, "store_image": store.logo,
                        'star': i.star, 'time': i.time, 'content': i.info, 'photo': i.image}
            return_list.append(tmp_list)
        return return_list


class manage(View):
    @JSR('hint')
    def get(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"
        user = User.objects.get(name=kwargs["user"])
        return_dict = {"name": user.name, 'image': user.image, 'address': user.address,
                       'card_num': user.card_num}
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
        user = User.objects.get(name=kwargs["user"])
        return_msg = "修改成功"
        if kind == "name":
            if User.objects.filter(name=info):
                return_msg = "用户名已存在"
            else:
                user.name = info
        elif kind == "image":
            user.image = info
        elif kind == "address":
            user.address = info
        elif kind == "card_num":
            user.card_num = info
        elif kind == 'card_password':
            user.card_password = info
        else:
            return_msg = "参数异常"
        return return_msg
