from utils.meta_wrapper import JSR
from utils.dump import *
from django.views import View
from Takeout.models import *


class user_info(View):
    @JSR('code', 'hint', 'orders_num', 'total_money', 'favorite_store', 'month_info', 'money_info')
    def post(self, request):
        if not request.user.is_authenticated:
            return "403", "用户未登录"
        cookie = request.user
        user = cookie.user
        if cookie.type != "user":
            return "300", "用户未登录"

        orders = Order.objects.filter(belonging_user=user)
        orders_num = len(orders)
        total_money = 0
        for i in range(orders_num):
            total_money += orders[i].money

        # order for favorite store
        favorite_stores = {}
        for i in orders:
            store_id = i.belonging_store.id
            if store_id not in favorite_stores:
                favorite_stores[store_id] = 1
            else:
                favorite_stores[store_id] += 1
        dict(sorted(favorite_stores.items(), key=lambda item: item[1], reverse=True))
        favorite_store = Store.objects.get(id=list(favorite_stores.keys())[0])

        # orders group by month
        month_info = {
            'money': [0] * 12,
            'sales': [0] * 12
        }
        for i in orders:
            year, month = i.time.strftime('%Y-%m').split('-')
            if year != '2022':
                continue
            month_info['money'][int(month) - 1] += i.money
            month_info['sales'][int(month) - 1] += 1

        # order by money
        money1, money2, money3, money4, money5 = 0, 0, 0, 0, 0
        for i in orders:
            tmp = i.money
            if tmp < 10:
                money1 += 1
            elif tmp < 30:
                money2 += 1
            elif tmp < 50:
                money3 += 1
            elif tmp < 100:
                money4 += 1
            else:
                money5 += 1
        money_info = [money1, money2, money3, money4, money5]

        # orders.values('belonging_store').annotate(total=Count('belonging_store')).order_by('-total')
        return "200", "success", orders_num, total_money, dump_store(favorite_store), month_info, money_info


class store_info(View):
    @JSR('code', 'hint', 'orders_num', 'star', 'favorite_item', 'item_sales_list', 'month_info', 'income')
    def post(self, request):
        if not request.user.is_authenticated:
            return "403", "店铺未登录"
        cookie = request.user
        store = cookie.store
        if cookie.type != "store":
            return "300", "店铺未登录"

        orders = Order.objects.filter(belonging_store=store)
        orders_num = len(orders)

        items = Item.objects.filter(belonging_store=store).order_by('-sales')
        favorite_item = items[0]

        item_sales_list = {
            "item_name": [],
            "sales": []
        }
        income = 0
        for i in items:
            item_sales_list["item_name"].append(i.name)
            item_sales_list["sales"].append(i.sales)
            income += i.price * i.sales

        # orders group by month
        month_info = {
            'money': [0] * 12,
            'sales': [0] * 12
        }
        for i in orders:
            year, month = i.time.strftime('%Y-%m').split('-')
            if year != '2022':
                continue
            month_info['money'][int(month) - 1] += i.money
            month_info['sales'][int(month) - 1] += 1

        return "200", "success", orders_num, store.star, dump_item(favorite_item), \
               item_sales_list, month_info, income


class admin_info(View):
    @JSR('code', 'hint', 'store_num', 'user_num', 'best_sales_store', 'best_star_store', 'store_list')
    def post(self, request):
        store_num = len(Store.objects.all())
        user_num = len(User.objects.all())
        best_sales_store = Store.objects.all().order_by('-sales')[0]
        best_star_store = Store.objects.all().order_by('-star')[0]

        # orders_num = len(Order.objects.all())

        stores = Store.objects.all()
        store_list = []
        for i in stores:
            tmp = [i.store_name, i.sales, 0, i.star]
            orders = Order.objects.filter(belonging_store=i)
            total_money = 0
            for j in orders:
                total_money += j.money
            tmp[2] = total_money
            store_list.append(tmp)

        return "200", "success", store_num, user_num, dump_store(best_sales_store), dump_store(
            best_star_store), store_list
