import json
from back_end.utils.meta_wrapper import JSR
from django.views import View
from models import *
from utils.dump import dump_item


class cart(View):
    @JSR('code', 'message', 'items')
    def get(self, request):
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

        store=Store.objects.get(id=kwargs["store_id"])
        this_cart = Cart.objects.get(belonging_user=user,belonging_store=store)
        return_list = []
        for i in this_cart.items:
            return_list.append(dump_item(i))

        return "200", "success", return_list
