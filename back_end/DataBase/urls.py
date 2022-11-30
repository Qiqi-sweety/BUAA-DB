"""DataBase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Takeout import views_homepage, views_LR, views_switch, views_store, views_admin
from django.conf import settings
from Takeout import views_user
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,
        {"document_root": settings.MEDIA_ROOT}, name='media'),
    path('admin/', admin.site.urls),
    # views_LR
    path('image/update/', views_LR.update_photo.as_view()),
    path('login/', views_LR.cookie_login.as_view()),
    path('user/register/', views_LR.user_register.as_view()),
    path('store/register/step1/', views_LR.store_register_step1.as_view()),
    path('store/register/step2/', views_LR.store_register_step2.as_view()),
    # views_homepage
    path('homepage/search/', views_homepage.search.as_view()),
    path('homepage/recommend/', views_homepage.recommend.as_view()),
    # views_switch_store
    path('switch/search/', views_switch.search.as_view()),
    path('switch/homepage/', views_switch.homepage.as_view()),
    path('switch/goods/', views_switch.goods.as_view()),
    path('switch/comments/', views_switch.comments.as_view()),
    # views_user
    path('user/showOrders/', views_user.showOrders.as_view()),
    path('user/writeComment/', views_user.writeComment.as_view()),
    path('user/myComments/', views_user.myComments.as_view()),
    path('user/changeInfo/', views_user.changeInfo.as_view()),
    path('user/manage/', views_user.manage.as_view()),
    # views_store
    path('store/homepage/', views_store.homepage.as_view()),
    path('store/display_goods/', views_store.display_goods.as_view()),
    path('store/delete_good/', views_store.delete_good.as_view()),
    path('store/add_good/', views_store.add_good.as_view()),
    path('store/manage_orders/', views_store.manage_orders.as_view()),
    path('store/process_order/', views_store.process_order.as_view()),
    path('store/comments/', views_store.comments.as_view()),
    path('store/change_info/', views_store.change_info.as_view()),
    path('store/show_info/', views_store.show_info.as_view()),
    # views_admin
    path('admin/displayInfo/', views_admin.displayInfo.as_view()),
    path('admin/validate/', views_admin.validate.as_view()),
]
