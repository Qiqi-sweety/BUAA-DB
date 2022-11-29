import request from './request'

export const user_register = (data) => {
    return request({
        url: 'user/register/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const store_register_1 = (data) => {
    return request({
        url: 'store/register/step1/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const store_register_2 = (data) => {
    return request({
        url: 'store/register/step2/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}