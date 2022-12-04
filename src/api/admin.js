import request from './request'

export const user_recommend = (data) => {
    return request({
        url: 'homepage/recommend/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}