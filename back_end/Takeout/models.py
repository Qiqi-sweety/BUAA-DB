from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from datetime import date


class MyManager(BaseUserManager):
    def create_user(self, name, password):
        user = get_user_model()(
            name=name
        )
        user.set_password(password)
        user.save()
        return user


# 基类
class Cookie(AbstractBaseUser):
    name = models.CharField(max_length=20, verbose_name="用户名", unique=True)
    type = models.CharField(max_length=20, verbose_name="类型")
    objects = MyManager()
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="用户", null=True)
    store = models.ForeignKey("Store", on_delete=models.CASCADE, verbose_name="店铺", null=True)
    USERNAME_FIELD = 'name'


# 用户
class User(models.Model):
    user_name = models.CharField(max_length=20, verbose_name="用户名")
    address = models.TextField(blank=False, default="", max_length=256, verbose_name="地址")
    card_num = models.CharField(verbose_name="银行卡号", max_length=30)


# 商家
class Store(models.Model):
    store_name = models.CharField(max_length=20, verbose_name="店铺名", unique=True)
    address = models.TextField(blank=False, default="", max_length=256, verbose_name="地址")
    license = models.TextField(blank=False, default="", max_length=256, verbose_name="营业执照")
    logo = models.TextField(blank=False, default="", max_length=256, verbose_name="logo")
    info = models.TextField(verbose_name="商铺描述", max_length=1000)

    star = models.FloatField(verbose_name="星级", default=5)
    sales = models.IntegerField(verbose_name="销量", default=0)
    isChecked = models.BooleanField(verbose_name="是否通过审核", default=False)


# 商品
class Item(models.Model):
    name = models.CharField(verbose_name="商品名", max_length=256, default="")
    image = models.TextField(blank=False, default="", max_length=256, verbose_name="商品图片")
    price = models.FloatField(verbose_name="商品价格")
    intro = models.TextField(verbose_name="商品描述", max_length=1000)
    belonging_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    sales = models.IntegerField(verbose_name="销量", default=0)


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    tmp_num = models.IntegerField(verbose_name="数量", default=0)


# 购物车
class Cart(models.Model):
    items = models.ManyToManyField(OrderItem)
    belonging_user = models.ForeignKey(User, on_delete=models.CASCADE)
    belonging_store = models.ForeignKey(Store, on_delete=models.CASCADE)


# 订单
class Order(models.Model):
    items = models.ManyToManyField(OrderItem)
    time = models.DateField(verbose_name="订单时间", default=date.today)
    address = models.CharField(verbose_name="订单配送地点", max_length=256)

    isProcessed = models.BooleanField(verbose_name="是否已处理", default=False)
    isDelivered = models.BooleanField(verbose_name="是否已送达", default=False)

    belonging_store = models.ForeignKey(Store, on_delete=models.PROTECT)
    belonging_user = models.ForeignKey(User, on_delete=models.PROTECT)

    money = models.FloatField(verbose_name="订单金额", default=0)

    isCommented = models.BooleanField(verbose_name="是否已评价", default=False)


# 评论
class Comment(models.Model):
    info = models.TextField(verbose_name="评价", max_length=1000)
    star = models.IntegerField(verbose_name="星级", default=5)
    time = models.DateField(verbose_name="评论时间", default=date.today)
    image = models.TextField(blank=False, default="", max_length=256, verbose_name="评论图片")
    belonging_order = models.OneToOneField(Order, on_delete=models.PROTECT, unique=True)


# 运送单
class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    time = models.DateTimeField(default=date.today, verbose_name="预计送达时间")
    fee = models.FloatField(verbose_name="骑手小费", default=5)
    isOnTime = models.BooleanField(verbose_name="是否按时送达", default=True)
    # TODO


# 注册申请
class Register(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    time = models.DateTimeField(default=date.today, verbose_name="注册时间")
    isPass = models.BooleanField(verbose_name="是否通过", default=False)
    # TODO
