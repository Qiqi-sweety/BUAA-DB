import { createRouter, createWebHistory } from 'vue-router'

const router = new createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes: [
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
            redirect: '/storeRegisterPage/step1',
            component: () => import('../components/pages/storeRegisterPage.vue'),
            children: [
                {
                    path: 'step1',
                    name: 'storeRegisterCard1',
                    component: () => import('../components/register/storeRegisterCard1.vue')
                },
                {
                    path: 'step2',
                    name: 'storeRegisterCard2',
                    component: () => import('../components/register/storeRegisterCard2.vue'),
                    props: (route) => ({
                        name: route.query.name,
                        password: route.query.password,
                    })
                    // props: true
                },
                {
                    path: 'step3',
                    name: 'storeRegisterCard3',
                    component: () => import('../components/register/storeRegisterCard3.vue')
                }
            ]
        },
        {
            path: '/personalCenterPage',
            name: 'personalCenterPage',
            redirect: '/personalCenterPage/order',
            component: () => import('../components/pages/personalCenterPage.vue'),
            children: [
                {
                    path: 'order',
                    name: 'orderSheet',
                    component: () => import('../components/personalCenter/orderSheet.vue')
                },
                {
                    path: 'comment',
                    name: 'evaluateSheet',
                    component: () => import('../components/personalCenter/evaluateSheet.vue')
                },
                {
                    path: 'data',
                    name: 'dataSheet'
                },
                {
                    path: 'userManage',
                    name: 'userManageSheet',
                    component: () => import('../components/personalCenter/userManageSheet.vue')
                },
            ]
        },
        {
            path: '/userMainPage',
            name: 'userMainPage',
            redirect: '/userMainPage/main',
            component: () => import('../components/pages/userMainPage.vue'),
            children: [
                {
                    path: 'main',
                    name: 'userMainForm',
                    component: () => import('../components/userMain/userMainForm.vue')
                },
                {
                    path: 'search',
                    name: 'userSearchResForm',
                    component: () => import('../components/userMain/userSearchResForm.vue'),
                    props: (route) => ({
                        key: route.query.key,
                        label: route.query.label,
                    })
                }
            ]
        },
        {
            path: '/storeMainPage',
            name: 'storeMainPage',
            redirect: '/storeMainPage/info',
            component: () => import('../components/pages/storeMainPage.vue'),
            children: [
                {
                    path: 'info',
                    name: 'storeInfoSheet',
                    component: () => import('../components/storeMain/storeInfoSheet.vue')
                },
                {
                    path: 'foodManage',
                    name: 'foodManageSheet',
                    component: () => import('../components/storeMain/foodManageSheet.vue')
                },
                {
                    path: 'orderManage',
                    name: 'orderManageSheet',
                    component: () => import('../components/storeMain/orderManageSheet.vue')
                },
                {
                    path: 'comment',
                    name: 'userEvaluateSheet',
                    component: () => import('../components/storeMain/userEvaluateSheet.vue')
                },
                {
                    path: 'idManage',
                    name: 'storeIdManageSheet',
                    component: () => import('../components/storeMain/storeIdManageSheet.vue')
                },
                {
                    path: 'data',
                    name: 'dataSheet'
                }
            ]
        },
        {
            path: '/managerMainPage',
            name: 'managerMainPage',
            redirect: '/managerMainPage/verify',
            component: () => import('../components/pages/managerMainPage.vue'),
            children: [
                {
                    path: 'verify',
                    name: 'verifySheet',
                    component: () => import('../components/managerMain/verifySheet.vue')
                },
                {
                    path: 'info',
                    name: 'infoSheet',
                    component: () => import('../components/managerMain/infoSheet.vue')
                },
                {
                    path: 'data',
                    name: 'dataSheet'
                }
            ]
        }
    ]
})

export default router