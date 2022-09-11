<template>

    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="customerRegisterImageForm"
      
    >
      <el-form-item class = "customerImage">

        <img alt="customerRegisterLogo" src="../../assets/customerLogo.svg" >

      
      </el-form-item>

    
    </el-form>

  
</template>

<script lang="ts" setup>




</script>

<style>

  .customerRegisterImageForm {
    width: 400px;
    height: 450px;
    /*padding: 30px;*/
    border-radius: 20px;
    /* 整个表单el-form位于整个屏幕的位置 margin */  
  }
  .customerImage {
    margin-top: 80px;
  }
  
</style>