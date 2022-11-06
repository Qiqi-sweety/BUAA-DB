import { createRouter, createWebHistory } from 'vue-router'

const router = new createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes:[
        {
            path: '/',
            name: 'firstPage',
            component: () => import('../components/pages/firstPage')
        },
        {
            path: '/userLoginPage',
            name: 'userLoginPage',
            component: () => import('../components/pages/userLoginPage.vue')
        },
        {
            path: '/storeLoginPage',
            name: 'storeLoginPage',
            component: () => import('../components/pages/storeLoginPage.vue')
        },
        {
            path: '/managerLoginPage',
            name: 'managerLoginPage',
            component: () => import('../components/pages/managerLoginPage.vue')
        },
        {
            path: '/userRegisterPage',
            name: 'userRegisterPage',
            component: () => import('../components/pages/userRegisterPage.vue')
        },
        {
            path: '/storeRegisterPage',
            name: 'storeRegisterPage',
            component: () => import('../components/pages/storeRegisterPage.vue')
        },
        {
            path: '/personalCenterPage',
            name: 'personalCenterPage',
            component: () => import('../components/pages/personalCenterPage.vue')
        }
    ]
})

export default router