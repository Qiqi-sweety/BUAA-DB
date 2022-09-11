<template>
  <div class="loginLayout">
    <el-container>
      <el-header>
  
      </el-header>
      <el-main>
        <div class = "LoginClass">
          <!-- <businessLoginCard/> -->
          <!--<managerLoginCard/>-->
          <customerLoginCard/>
        </div>
      </el-main>
    </el-container>
  </div>
</template>
  
<script>
  import customerLoginCard from '../login/customerLoginCard.vue'
  import managerLoginCard from '../login/managerLoginCard.vue'
  import businessLoginCard from '../login/businessLoginCard.vue'
  
  export default {
    name: 'loginPage',
    components: {
      customerLoginCard,
      managerLoginCard,
      businessLoginCard,
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
  