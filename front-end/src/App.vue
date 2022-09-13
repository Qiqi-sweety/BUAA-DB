<template>
  <!-- <firstPageVue/> -->
  <!-- <loginPageVue/> -->
  <registerPageVue/>
  <!-- <orderPageVue/> -->
</template>

<script>
  import loginPageVue from './components/pages/loginPage.vue'
  import registerPageVue from './components/pages/registerPage.vue'
  import firstPageVue from './components/pages/firstPage.vue'
  import orderPageVue from './components/pages/orderPage.vue'

export default {
  name: 'App',
  components: {
    loginPageVue,
    registerPageVue,
    firstPageVue,
    orderPageVue,
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

.el-header {
  height: 60px;
  background-color: white;
}

.el-main {
  height: 870px;
}

.customerLoginClass {
  margin-top:100px;
}
</style>
