<template>
    <div class="registerLayout">
      <el-container>
        <el-header>
  
        </el-header>
        <el-main>
          <div class = "registerClass">
            <businessRegisterCard/>
            <!-- <CustomerRegisterCard/> -->
          </div>
        </el-main>
      </el-container>
    </div>
    
</template>
  
<script>
  import customerRegisterCard from '../register/customerRegisterCard.vue'
  import businessRegisterCard from '../register/businessRegisterCard.vue'
  
  export default {
    name: 'registerPage',
    components: {
      customerRegisterCard,
      customerRegisterCard,
      businessRegisterCard,
  }
  }
</script>
  
<style>
  .el-header {
    height: 60px;
    background-color: white;
  }
  
  .el-main {
    height: 870px;
  }
  
  .registerClass {
    margin-top:100px;
  }
  
</style>
  