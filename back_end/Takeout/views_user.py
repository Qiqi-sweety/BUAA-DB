import json
from datetime import *

from utils.dump import dump_comment, dump_user, dump_order
from utils.meta_wrapper import JSR
from django.views import View
from Takeout.models import *


class showOrders(View):
    @JSR('code', 'message', 'list')
    def post(self, request):
        if not request.user.is_authenticated:
            return "403", "用户未登录"
        cookie = request.user
        user = cookie.user
        if cookie.type != "user":
            return "300", "用户未登录"

        orders = Order.objects.filter(belonging_user=user)
        return_list = []
        for i in orders:
            return_list.append(dump_order(i))
        return "200", "success", return_list


class writeComment(View):
    @JSR('code', 'message', 'hint')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        try:
            order = Order.objects.get(id=kwargs["order_id"])
        except Exception:
            return "300", "订单不存在", "error"

        comment = Comment(info=kwargs["content"], star=kwargs["star"], image=kwargs["photo"],
                          belonging_order=order)
        comment.save()
        return "200", "评论成功", "success"


class myComments(View):
    @JSR('code', 'message', 'list')
    def post(self, request):
        if not request.user.is_authenticated:
            return "403", "还没登录"
        cookie = request.user
        user = cookie.user
        if cookie.type != "user":
            return "300", "未登录"
        orders = Order.objects.filter(belonging_user=user)
        comments = []
        for i in orders:
            comment = Comment.objects.get(belonging_order=i)
            comments.append(comment)
        return_list = []
        for i in comments:
            return_list.append(dump_comment(i))
        return "200", "success", return_list


class manage(View):
    @JSR('code', 'message', 'user_info')
    def post(self, request):

        if not request.user.is_authenticated:
            return "403", "还没登录"
        cookie = request.user
        user = cookie.user
        if cookie.type != "user":
            return "300", "未登录"

        return_dict = dump_user(user)
        return "200", "success", return_dict


class changeInfo(View):
    @JSR('code', 'message', 'hint')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        if not request.user.is_authenticated:
            return "403", "还没登录"
        cookie = request.user
        user = cookie.user
        if cookie.type != "user":
            return "300", "未登录"

        kind = kwargs["type"]
        info = kwargs["info"]

        return_msg = "修改成功"
        if kind == "name":
            if len(User.objects.filter(name=info)) != 0:
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
        user.save()

        return "200", "success", return_msg
