import json
from utils.meta_wrapper import JSR
from django.views import View
from Takeout.models import *
from utils.dump import dump_item


class cart(View):
    @JSR('code', 'message', 'items')
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

        store = Store.objects.get(id=kwargs["store_id"])
        this_cart = Cart.objects.get(belonging_user=user, belonging_store=store)
        return_list = []
        for i in this_cart.items.all():
            this_dict = dump_item(i.item)
            this_dict['num'] = i.tmp_num
            return_list.append(this_dict)

        return "200", "success", return_list


class addItem(View):
    @JSR('code', 'message')
    def post(self, request):
        global order_item, this_cart
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

        item = Item.objects.get(id=kwargs["item_id"])
        store = Store.objects.get(id=kwargs["store_id"])
        carts = Cart.objects.filter(belonging_user=user, belonging_store=store)
        if len(carts) != 0:
            this_cart = carts[0]
        else:
            this_cart = Cart.objects.create(belonging_user=user, belonging_store=store)
        isItemInCart = False
        for i in this_cart.items.all():
            if i.item.id == item.id:
                order_item = i
                isItemInCart = True
                break
        if isItemInCart:
            # order_item = OrderItem.objects.get(item=item, cart=this_cart)
            order_item.tmp_num = order_item.tmp_num + 1
            order_item.save()
            this_cart.save()
            return "200", "add num"
        else:
            order_item = OrderItem.objects.create(item=item)
            this_cart.items.add(order_item)
            order_item.tmp_num = 1
            order_item.save()
            this_cart.save()
            return "200", "add item"


class deleteItem(View):
    @JSR('code', 'message')
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

        item = Item.objects.get(id=kwargs["item_id"])
        store = Store.objects.get(id=kwargs["store_id"])
        this_cart = Cart.objects.get(belonging_user=user, belonging_store=store)
        isItemInCart = False
        for i in this_cart.items.all():
            if i.item.id == item.id:
                isItemInCart = True
                break
        if isItemInCart:
            order_item = OrderItem.objects.get(item=item, cart=this_cart)
            order_item.tmp_num = order_item.tmp_num - 1
            order_item.save()
            if order_item.tmp_num == 0:
                this_cart.items.remove(order_item)
                this_cart.save()
                order_item.delete()
                return "200", "delete item"
            return "200", "delete num"
        else:
            return "300", "zero but remove"


class makeOrder(View):
    @JSR('code', 'message')
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

        store = Store.objects.get(id=kwargs["store_id"])
        items = Cart.objects.get(belonging_user=user, belonging_store=store).items.all()
        money = 0
        for i in items:
            print(i)
            for j in range(i.tmp_num):
                money += i.item.price
                i.item.sales += 1
            i.item.save()
        order = Order.objects.create(belonging_user=user, belonging_store=store, address=user.address, money=money)
        items=Cart.objects.get(belonging_user=user, belonging_store=store).items.all()
        for i in items:
            order.items.add(i)
        order.save()

        this_cart = Cart.objects.get(belonging_user=user, belonging_store=store)
        this_cart.delete()

        return "200", "success"
