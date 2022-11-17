def dump_store(store):
    return {'id': store.id, 'name': store.store_name, 'address': store.address, 'logo': store.logo, 'info': store.info,
            'star': store.star, 'sales': store.sales}


def dump_item(item):
    return {"id": item.id, 'name': item.name, 'price': item.price, 'image': item.image, 'info': item.info,
            'sales': item.sales}


def dump_comment(comment):
    return {'order_id': comment.belonging_order.id, "store_name": comment.belonging_store.name,
            "user_id": comment.belonging_user.id, "user_name": comment.belonging_user.name,
            'star': comment.star, 'time': comment.time, 'content': comment.info, 'photo': comment.image}


def dump_order(order):
    return {"order_id": order.id, "items": [dump_item(i) for i in order.items.all()],
            "time": order.time, "address": order.address, "store": order.store.name, "user": order.belonging_user.name}


def dump_user(user):
    return {"id": user.id, "name": user.user_name, "address": user.address}
