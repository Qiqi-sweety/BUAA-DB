<template>
  <div id="app">
    <router-view></router-view>
  </div>
  <!-- 首页 -->
<!--  <firstPageVue/>-->

  <!-- 登录页面 -->
<!--  <managerLoginPageVue/>-->
<!--  <userLoginPageVue/>-->
<!--  <storeLoginPageVue/>-->

  <!-- 注册页面 -->
<!--  <userRegisterPageVue/>-->
<!--  <storeRegisterPageVue/>-->


<!--  <user-main-page-vue/>-->

<!--  <user-order-page-vue/>-->

<!--  <personal-center-page-vue/>-->
<!--  -->
<!--  <store-main-page-vue/>-->
<!--  <manager-main-page-vue/>-->
  
</template>

<script>

import firstPageVue from './components/pages/firstPage.vue'

import userLoginPageVue from './components/pages/userLoginPage.vue'
import managerLoginPageVue from './components/pages/managerLoginPage.vue'
import storeLoginPageVue from './components/pages/storeLoginPage.vue'

import storeRegisterPageVue from './components/pages/storeRegisterPage.vue'

import userOrderPageVue from './components/pages/userOrderPage.vue'
import userMainPageVue from './components/pages/userMainPage.vue'
import storeMainPageVue from './components/pages/storeMainPage.vue'
import managerMainPageVue from './components/pages/managerMainPage.vue'
import personalCenterPageVue from './components/pages/personalCenterPage.vue'
import userRegisterPageVue from './components/pages/userRegisterPage.vue'

export default {
  name: 'App',
  components: {
    firstPageVue,

    userLoginPageVue,
    storeLoginPageVue,
    managerLoginPageVue,

    userRegisterPageVue,
    storeRegisterPageVue,

    userMainPageVue,
    storeMainPageVue,
    managerMainPageVue,

    personalCenterPageVue,
    userOrderPageVue,
  },
  methods: {

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #faecb8;
}

/*.el-header {*/
/*  height: 60px;*/
/*  background-color: white;*/
/*}*/

/*.el-main {*/
/*  height: 870px;*/
/*}*/

/*.customerLoginClass {*/
/*  margin-top:100px;*/
/*}*/
</style>
