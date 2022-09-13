from django.db import models
from datetime import date


# 用户

class User(models.Model):
    name = models.CharField(blank=True, verbose_name="用户名", max_length=30, default='用户A')
    password = models.CharField(verbose_name="密码", primary_key=True, max_length=256)
    address = models.TextField(blank=False, default="", max_length=256, verbose_name="地址")
    card_num = models.CharField(verbose_name="银行卡号", max_length=30)
    card_password = models.CharField(verbose_name="银行卡密码", max_length=256)


# 商家

class Store(models.Model):
    name = models.CharField(verbose_name="店铺名", max_length=256, default="")
    password = models.CharField(verbose_name="密码", primary_key=True, max_length=256)
    address = models.TextField(blank=False, default="", max_length=256, verbose_name="地址")
    license = models.ImageField(verbose_name="商家执照", name="", width_field=15, height_field=20)
    logo = models.ImageField(verbose_name="店铺头像", blank=True, width_field=15, height_field=20)
    info = models.TextField(verbose_name="商铺描述", max_length=1000)

# 管理员


class Administer(models.Model):
    name = models.CharField(verbose_name="管理员名称", max_length=256, default="")
    password = models.CharField(verbose_name="密码", primary_key=True, max_length=256)


# 骑手
class Rider(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=256, default="")
    telephone = models.CharField(verbose_name="手机号", max_length=256)


# 商品
class Item(models.Model):
    belonging_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="商品名", max_length=256, default="")
    image = models.ImageField(verbose_name="商品图片", name="", width_field=8, height_field=8)
    price = models.FloatField(verbose_name="商品价格")
    intro = models.TextField(verbose_name="商品描述", max_length=1000)


# 购物车
class Cart(models.Model):
    price1 = models.FloatField(verbose_name="门槛价格")
    price2 = models.FloatField(verbose_name="满减金额")
    id1 = models.IntegerField(verbose_name="店铺id")


# 订单
class Order(models.Model):
    belonging_store = models.ForeignKey(Store, on_delete=models.PROTECT)
    belonging_user = models.ForeignKey(User, on_delete=models.PROTECT)
    address = models.CharField(verbose_name="订单配送地点", max_length=256)


# 评论
class Comment(models.Model):
    belonging_store = models.ForeignKey(Store, on_delete=models.PROTECT)
    belonging_user = models.ForeignKey(User, on_delete=models.PROTECT)
    info = models.TextField(verbose_name="商品描述", max_length=1000)
    star = models.IntegerField(verbose_name="星级", default=5)


# 运送单
class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    time = models.DateTimeField(default=date.today,verbose_name="预计送达时间")
    fee = models.FloatField(verbose_name="骑手小费", default=5)
    isOnTime = models.BooleanField(verbose_name="是否按时送达", default=True)


# # 交易记录
# class Trade(models.Model):
#     redpaper_id = models.IntegerField(verbose_name="红包id")
#     user_name = models.CharField(verbose_name="顾客用户名", max_length=256)


# 注册申请
class Register(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    time = models.DateTimeField(default=date.today,verbose_name="注册时间")
    isPass = models.BooleanField(verbose_name="是否通过", default=False)


# # 人员登记
# class CheckIn(models.Model):
#     store_id = models.IntegerField(verbose_name="店铺id")
#     name = models.CharField(verbose_name="顾客用户名", max_length=256)
