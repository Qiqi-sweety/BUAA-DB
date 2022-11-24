import request from './request'

export const user_register = (data) => {
    return request({
        url: 'user/register/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}