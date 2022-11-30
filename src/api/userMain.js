import request from './request'

export const user_recommend = (data) => {
    return request({
        url: 'homepage/recommend/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}

export const user_search = (data) => {
    console.log(JSON.stringify(data))
    return request({
        url: 'homepage/search/',
        method: 'POST',
        data: JSON.stringify(data)
    })
}