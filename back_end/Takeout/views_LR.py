import json

from back_end.utils.meta_wrapper import JSR
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

        this_password1 = kwargs["password1"]
        this_password2 = kwargs["password2"]
        if this_password1 != this_password2:
            return "两次密码不一致"

        address = kwargs["address"]
        care_num = kwargs["care_num"]

        if this_password1 == "" or this_password2 == "":
            return "密码不能为空"
        if address == "":
            return "地址不能为空"
        if care_num == "":
            return "卡号不能为空"

        this_user = User(name=this_name, password=this_password1, address=address, care_num=care_num)
        this_user.save()

        return "注册成功"


class store_register_step1(View):
    @JSR('hint')
    def register(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        this_name = kwargs["name"]
        if len(Store.objects.filter(name=this_name)) != 0:
            return "店铺名已被注册"

        password1 = kwargs["password1"]
        password2 = kwargs["password2"]
        if password1 != password2:
            return "密码不一致"

        store = Store(name=kwargs['name'], password=password1)
        store.save()
        return "下一步"


class store_register_step2(View):
    @JSR('hint')
    def register(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        name = kwargs["name"]
        store = Store.objects.get(name=name)

        address = kwargs["address"]
        logo = kwargs["logo"]
        license = kwargs["license"]
        info = kwargs["info"]

        if name == "":
            return "店铺名不能为空"
        elif address == "":
            return "地址不能为空"
        elif logo == "":
            return "logo不能为空"
        elif license == "":
            return "营业执照不能为空"
        elif info == "":
            return "店铺简介不能为空"
        else:
            store.address = address
            store.logo = logo
            store.license = license
            store.info = info
            store.save()
            return "申请成功，等待管理员审核"


class user_login(View):
    @JSR('hint')
    def login(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "参数异常"

        user = kwargs["name"]
        users = User.objects.filter(name=user)

        if len(users) == 0:
            return "用户未注册"
        else:
            if users[0].password == kwargs["password"]:
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
        stores = Store.objects.filter(name=store)
        if len(stores) == 0:
            return "店铺未注册"
        else:
            if stores[0].password == kwargs["password"]:
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

        if kwargs["name"] == "admin" and kwargs["password"] == "PleaseGiveMe30":
            return "登陆成功"
        else:
            return "用户名或密码错误"
