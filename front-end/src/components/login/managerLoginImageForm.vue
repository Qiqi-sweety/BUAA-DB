<template>
    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="managerLoginImageForm"     
    >
      <el-form-item class = "managerImage">

        <img alt="managerLoginLogo" src="../../assets/managerLogo.svg" >
      
      </el-form-item>
    </el-form>
  
</template>

<script lang="ts" setup>

</script>

<style>
  .managerLoginImageForm {
    width: 400px;
    height: 450px;
    /*padding: 30px;*/
    border-radius: 20px;
    /* 整个表单el-form位于整个屏幕的位置 margin */  
  }
  .managerImage {
    margin-top: 80px;
  }
  
</style>