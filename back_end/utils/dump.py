def dump_store(store):
    return {'id': store.id, 'name': store.store_name, 'address': store.address, 'info': store.info,
            'star': store.star, 'sales': store.sales, 'logo': store.logo, 'isChecked': store.isChecked}


def dump_item(item):
    return {"id": item.id, 'name': item.name, 'price': item.price, 'intro': item.intro,
            'sales': item.sales, 'image': item.image}


def dump_comment(comment):
    t = comment.time
    store = comment.belonging_order.belonging_store
    user = comment.belonging_order.belonging_user
    return {'order_id': comment.belonging_order.id, 'image': comment.image, 'user_id': user.id,
            'user_name': user.user_name, 'store_name': store.store_name, 'store_logo': store.logo,
            'star': comment.star, 'time': t.strftime("%Y.%m.%d"), 'content': comment.info}


def dump_order(order):
    t = order.time
    return {"order_id": order.id, "items": [{"item": dump_item(i.item), "num": i.tmp_num} for i in order.items.all()],
            "time": t.strftime("%Y.%m.%d"), "address": order.address,
            "store": order.belonging_store.store_name,
            "is_commented":order.isCommented,
            "user": order.belonging_user.user_name}


def dump_user(user):
    return {"id": user.id, "name": user.user_name, "address": user.address, "card_num": user.card_num, }
