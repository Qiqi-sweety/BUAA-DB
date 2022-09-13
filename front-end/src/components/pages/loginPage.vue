<template>
  <div class="loginLayout">
    <el-container>
      <el-header>
  
      </el-header>
      <el-main>
        <div class = "LoginClass">
          <!-- <storeLoginCard/> -->
          <!-- <managerLoginCard/> -->
          <userLoginCard/>
        </div>
      </el-main>
    </el-container>
  </div>
</template>
  
<script>
  import userLoginCard from '../login/userLoginCard.vue'
  import managerLoginCard from '../login/managerLoginCard.vue'
  import storeLoginCard from '../login/storeLoginCard.vue'
  
  export default {
    name: 'loginPage',
    components: {
      userLoginCard,
      managerLoginCard,
      storeLoginCard,
  }
  }
</script>
  
<style>
  .el-header {
    /* background-color: #f4d870; */
    height: 60px;
    background-color: white;
  }
  
  .el-main {
    height: 870px;
  }
  
  .LoginClass {
    margin-top:100px;
  }
  
</style>
  