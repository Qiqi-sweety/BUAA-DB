<template>
    <div class="common-layout">
      <el-container>
        <el-header class = "firstPageHeader">        
        </el-header>
        <el-main>
          <el-row class = "introRowClass">
            <intro/>
          </el-row>
            <cards/>
        </el-main>
      </el-container>
    </div>
    
</template>
  
  
<script>
  
  import cards from '../firstPage/cards.vue'
  import intro from '../firstPage/intro.vue'
  
  export default {
    name: 'firstPage',
    components: {
      cards,
      intro,
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
  
  .introRowClass {
    background-color:   #fdf9e7;
    height: 455px;
    margin-bottom: 0px;
    margin-top: 0px;
  }
  
</style>
  