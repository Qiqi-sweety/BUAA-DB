<template>

    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="businessRegisterImageForm"
    >
      <el-form-item class = "businessRegisterImage">

        <img alt="businessRegisterLogo" src="../../assets/businessLogo.svg" >

      
      </el-form-item>

    
    </el-form>

  
</template>

<script lang="ts" setup>




</script>

<style>

  .businessRegisterImageForm {
    width: 400px;
    height: 350px;
    /*padding: 30px;*/
    border-radius: 20px;
    /* 整个表单el-form位于整个屏幕的位置 margin */  
  }
  .businessRegisterImage {
    margin-top:0px;
  }
  
</style>