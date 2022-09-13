import json

from utils.meta_wrapper import JSR
from django.views import View
from models import *


class user_register(View):
    @JSR('hint')
    def register(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        this_name = kwargs["name"]
        if len(User.objects.filter(name=this_name)) != 0:
            return "用户名已被注册"

        user = User(name=kwargs["name"], password=kwargs["password"], address=kwargs["address"], money=kwargs["money"],
                    telephone=kwargs["telephone"])
        user.save()
        return "注册成功"


class store_register(View):
    @JSR('hint')
    def register(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        this_name = kwargs["name"]
        if len(Store.objects.filter(name=this_name)) != 0:
            return "用户名已被注册"

        store = Store(name=kwargs["name"], password=kwargs["password"], address=kwargs["address"],
                      license=kwargs["license"], logo=kwargs["logo"])
        register = Register(store=store)
        register.save()
        return "申请成功，等待管理员审核"


class admin_register(View):
    @JSR('hint')
    def register(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        if int(kwargs["public_key"]) != 10086:
            return "对不起，您的公钥信息错误，未通过管理员申请"

        this_name = kwargs["name"]
        if len(Administer.objects.filter(name=this_name)) != 0:
            return "用户名已被注册"

        admin = Administer(name=kwargs["name"], password=["private_key"])
        admin.save()
        return "注册成功"


class rider_register(View):
    @JSR('hint')
    def register(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        this_name = kwargs["name"]
        if len(Rider.objects.filter(name=this_name)) != 0:
            return "用户名已被注册"

        rider = Rider(name=kwargs["name"], telephone=["telephone"])
        rider.save()
        return "注册成功"


class user_login(View):
    @JSR('hint')
    def login(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        user = kwargs["name"]
        users = User.objects.all()
        if len(users.filter(name=user)) == 0:
            return "用户未注册"
        else:
            this_user = users.filter(name=user)
            if this_user[0].password == kwargs["password"]:
                return "登陆成功"
            else:
                return "密码错误"


class store_login(View):
    @JSR('hint')
    def login(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        store = kwargs["name"]
        stores = Store.objects.all()
        if len(stores.filter(name=store)) == 0:
            return "用户未注册"
        else:
            this_store = stores.filter(name=store)
            if this_store[0].password == kwargs["password"]:
                return "登陆成功"
            else:
                return "密码错误"


class admin_login(View):
    @JSR('hint')
    def login(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        admin = kwargs["name"]
        admins = Administer.objects.all()
        if len(admins.filter(name=admin)) == 0:
            return "用户未注册"
        else:
            this_admin = admins.filter(name=admin)
            if this_admin[0].password == kwargs["password"]:
                return "登陆成功"
            else:
                return "密码错误"


class rider_login(View):
    @JSR('hint')
    def login(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        rider = kwargs["name"]
        riders = Rider.objects.all()
        if len(riders.filter(name=rider)) == 0:
            return "用户未注册"
        else:
            this_rider = riders.filter(name=rider)
            if this_rider[0].password == kwargs["password"]:
                return "登陆成功"
            else:
                return "密码错误"


class user_homepage_recommender(View):
    @JSR('recommender')
    def homepage_recommender(self,request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        # get the user's specific information
        # recommender stores
        k_list=[]
        return k_list


class user_search_recommender(View):
    @JSR('recommender')
    def homepage_recommender(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        item=kwargs["item"]

        # get the user's specific information
        # a recommender algorithm for the specific user

        k_list = []
        return k_list


class search_bar(View):
    @JSR('restrict')
    def bar(self,request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        kind = kwargs["type"]
        k_list = []

        # live, difficult

        return k_list


class search_item(View):
    @JSR('recommender')
    def item(self,request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        # get the user's specific information
        # a recommender algorithm for the specific user

        k_list = []
        return k_list
# 商家加菜

# 用户点菜，进入购物车

#
