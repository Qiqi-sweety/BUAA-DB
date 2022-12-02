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
            words.append(word)
        return_list = []
        for i in words:
            return_list.append(dump_comment(i))
        return "200", "success", return_list


class addToCart(View):
    @JSR('code', 'message')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        store = Store.objects.get(id=kwargs["store_id"])

        if not request.user.is_authenticated:
            return "403", "用户未登录"
        cookie = request.user
        user = cookie.user
        if cookie.type != "user":
            return "300", "用户未登录"

        item = Item.objects.get(belonging_store=store, id=kwargs['item_id'])

        if len(Cart.objects.filter(belonging_store=store, belonging_user=user)) == 0:
            cart = Cart.objects.create(belonging_user=user, belonging_store=store)
        else:
            cart = Cart.objects.get(belonging_store=store, belonging_user=user)

        cart.items.add(item)
        return "200", "success"


class makeOrder(View):
    @JSR('code', 'message')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        store = Store.objects.get(id=kwargs["store_id"])

        if not request.user.is_authenticated:
            return "403", "用户未登录"
        cookie = request.user
        user = cookie.user
        if cookie.type != "user":
            return "300", "用户未登录"

        cart = Cart.objects.get(belonging_store=store, belonging_user=user)
        items = cart.items.all()
        if len(items) == 0:
            return "404", "购物车为空"

        order = Order.objects.create(belonging_store=store, belonging_user=user,address=user.address)
        order.items.set(items)
        order.save()
        cart.items.clear()
        return "200", "success"
