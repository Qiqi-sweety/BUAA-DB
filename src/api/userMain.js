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
        url: 'switch/addToCart/',
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
        url: 'switch/makeOrder/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}