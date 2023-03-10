import request from './request'

export const store_homepage = (data) => {
    return request({
        url: 'store/homepage/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const show_info = (data) => {
    return request({
        url: 'store/show_info/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const change_info = (data) => {
    return request({
        url: 'store/change_info/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const show_items = (data) => {
    return request({
        url: 'store/display_goods/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const add_items = (data) => {
    return request({
        url: 'store/add_good/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const del_items = (data) => {
    return request({
        url: 'store/delete_good/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const show_orders = (data) => {
    return request({
        url: 'store/manage_orders/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const process_order = (data) => {
    return request({
        url: 'store/process_order/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const show_comments = (data) => {
    return request({
        url: 'store/comments/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const show_data = (data) => {
    return request({
        url: 'statistic/store_info',
        method: 'POST',
        data: JSON.stringify(data)
    })
}