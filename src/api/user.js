import request from './request'

export const user_recommend = (data) => {
    return request({
        url: 'homepage/recommend/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const user_search = (data) => {
    return request({
        url: 'homepage/search/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const enter_store = (data) => {
    return request({
        url: 'switch/homepage/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const enter_menu = (data) => {
    return request({
        url: 'switch/goods/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const add_to_cart = (data) => {
    return request({
        url: 'cart/addItem/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const del_from_cart = (data) => {
    return request({
        url: 'cart/deleteItem/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const enter_comment = (data) => {
    return request({
        url: 'switch/comments/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const enter_search = (data) => {
    return request({
        url: 'switch/search/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const show_cart = (data) => {
    return request({
        url: 'cart/cart/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const make_order = (data) => {
    return request({
        url: 'cart/makeOrder/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const show_orders = (data) => {
    return request({
        url: 'user/showOrders/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const write_comment = (data) => {
    console.log(JSON.stringify(data))
    return request({
        url: 'user/writeComments/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const show_comments = (data) => {
    return request({
        url: 'user/myComments/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const show_info = (data) => {
    return request({
        url: 'user/manage/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const change_info = (data) => {
    return request({
        url: 'user/changeInfo/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const show_data = (data) => {
    return request({
        url: 'statistic/user_info',
        method: 'POST',
        data: JSON.stringify(data)
    })
}