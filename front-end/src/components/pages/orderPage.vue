<template>
    <div class="common-layout">
      <el-container>
        <el-header>
          
        </el-header>
        <el-main>
          <order-tabs/>
        </el-main>
      </el-container>
    </div>
    
</template>
  
  
<script>
  
  import orderTabs from '../orderPage/orderTabs.vue';
  
  export default {
    name: 'orderPage',
    components: {
      orderTabs,
    }
  }
</script>
  
<style>  
  .el-header {
    background-color:white;
    border-radius: 10px;
  }
  
  .el-main {
    height: 870px;
    border-radius: 20px;
    padding-left: 0px;
    padding-right: 0px;
    padding-bottom: 0px;
    padding-top: 0px;
  }
  

  
</style>
  