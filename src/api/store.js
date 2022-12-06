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