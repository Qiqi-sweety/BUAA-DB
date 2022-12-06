import json
import uuid

from django.contrib.auth import get_user_model, authenticate, login

from utils.meta_wrapper import JSR
from django.views import View
from Takeout.models import *


class user_register(View):
    @JSR('code', 'hint', 'message')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "", "参数异常"

        if kwargs["name"] == "":
            return "300", "error", "用户名不能为空"
        elif len(Cookie.objects.filter(name=kwargs["name"])) != 0:
            return "300", "error", "用户名已被注册"
        if kwargs["password"] == "":
            return "300", "error", "密码不能为空"
        elif len(kwargs["password"]) < 6:
            return "300", "error", "密码须不少于6位"
        if kwargs["address"] == "":
            return "300", "error", "地址不能为空"
        if kwargs["card_num"] == "":
            return "300", "error", "卡号不能为空"

        cookie = get_user_model().objects.create_user(kwargs['name'], kwargs['password'])

        this_user = User(user_name=kwargs['name'], address=kwargs["address"], card_num=kwargs["card_num"])
        this_user.save()
        cookie.user = this_user
        cookie.type = "user"
        cookie.save()

        return "200", "success", "注册成功"


class store_register_step1(View):
    @JSR('code', 'hint', 'message')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "", "参数异常"

        if kwargs["name"] == "":
            return "300", "error", "店铺名不能为空"
        if len(Cookie.objects.filter(name=kwargs["name"])) != 0:
            return "300", "error", "店铺名已被注册"
        if kwargs["password"] == "":
            return "300", "error", "密码不能为空"

        return "200", "success", "下一步"


class store_register_step2(View):
    @JSR('code', 'hint', 'message')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "", "参数异常"

        if kwargs["logo"] == "":
            return "300", "error", "请上传logo"
        if kwargs["address"] == "":
            return "300", "error", "地址不能为空"
        if kwargs["info"] == "":
            return "300", "error", "店铺简介不能为空"
        if kwargs["license"] == "":
            return "300", "error", "营业执照不能为空"

        cookie = get_user_model().objects.create_user(kwargs['name'], kwargs['password'])
        store = Store(store_name=kwargs['name'], logo=kwargs["logo"], address=kwargs["address"], info=kwargs["info"],
                      license=kwargs["license"])
        store.save()
        cookie.store = store
        cookie.type = "store"
        cookie.save()

        return "200", "success", "申请成功，等待管理员审核"


class set_admin(View):
    @JSR('code', 'hint')
    def post(self, request):
        cookie = get_user_model().objects.create_user("admin", "ADMIN")
        cookie.type = "admin"
        cookie.save()
        return "200","success"


class cookie_login(View):
    @JSR('code', 'hint', 'message')
    def post(self, request):
        try:
            kwargs: dict = json.loads(request.body)
        except Exception:
            return "400", "", "参数异常"
        if kwargs.keys() != {'name', 'password'}:
            return "400", "", "参数异常"
        if not get_user_model().objects.filter(name=kwargs['name']).exists():
            return "300", "error", "账号不存在"
        user = authenticate(request, username=kwargs['name'], password=kwargs['password'])
        if user is not None:
            login(request, user)
            return "200", "success", "登录成功"
        else:
            return "300", "error", "用户名或密码错误"


class update_photo(View):
    @JSR('code', 'hint', 'message', 'url')
    def post(self, request):
        if not request.user.is_authenticated:
            return "403", "还没登录"

        photo = request.FILES
        if len(photo) == 0:
            return "400", "error", "没有图片", ""
        if len(photo) > 1:
            return "400", "error", "只能上传一张图片", ""
        img = list(photo.values())[0]
        if img.size > 1024 * 1024:
            return "400", "error", "图片过大", ""
        # generate random name
        name = str(uuid.uuid4()) + '.jpg'
        with open(f'media/{name}', 'wb+') as destination:
            for chunk in img.chunks():
                destination.write(chunk)
        return "200", "success", "上传成功", "/media/" + name
