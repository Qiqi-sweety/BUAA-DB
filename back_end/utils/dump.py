def dump_store(store):
    return {'id': store.id, 'name': store.store_name, 'address': store.address, 'info': store.info,
            'star': store.star, 'sales': store.sales, 'logo': store.logo}


def dump_item(item):
    return {"id": item.id, 'name': item.name, 'price': item.price, 'intro': item.intro,
            'sales': item.sales, 'image': item.image}


def dump_comment(comment):
    t = comment.time
    store = comment.belonging_order.belonging_store
    user = comment.belonging_order.belonging_user
    return {'order_id': comment.belonging_order.id, 'image': comment.image, 'user_id': user.id,
            'store_name': store.store_name, 'store_logo': store.logo,
            'star': comment.star, 'time': t.strftime("%Y-%m-%d %H:%M:%S"), 'content': comment.info}


def dump_order(order):
    t = order.time
    return {"order_id": order.id, "items": [dump_item(i) for i in order.items.all()],
            "time": t.strftime("%Y-%m-%d %H:%M:%S"), "address": order.address,
            "store": order.belonging_store.store_name,
            "user": order.belonging_user.user_name}


def dump_user(user):
    return {"id": user.id, "name": user.user_name, "address": user.address}
