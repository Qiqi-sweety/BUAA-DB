def dump_store(store):
    return {'id': store.id, 'name': store.store_name, 'address': store.address, 'info': store.info,
            'star': store.star, 'sales': store.sales}


def dump_item(item):
    return {"id": item.id, 'name': item.name, 'price': item.price, 'intro': item.intro,
            'sales': item.sales}


def dump_comment(comment):
    return {'order_id': comment.belonging_order.id,
            'star': comment.star, 'time': comment.time, 'content': comment.info}


def dump_order(order):
    return {"order_id": order.id, "items": [dump_item(i) for i in order.items.all()],
            "time": order.time, "address": order.address, "store": order.belonging_store.store_name,
            "user": order.belonging_user.user_name}


def dump_user(user):
    return {"id": user.id, "name": user.user_name, "address": user.address}
