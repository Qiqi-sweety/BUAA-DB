import request from './request'

export const show_info = (data) => {
    return request({
        url: 'manage/displayinfo/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const valid_store = (data) => {
    return request({
        url: 'manage/validate/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const show_data = (data) => {
    return request({
        url: 'statistic/admin_info',
        method: 'POST',
        data: JSON.stringify(data)
    })
}