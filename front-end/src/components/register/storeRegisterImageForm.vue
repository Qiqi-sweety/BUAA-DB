<template>

    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="storeRegisterImageForm"
    >
      <el-form-item class = "storeRegisterImage">

        <img alt="storeRegisterLogo" src="../../assets/storeLogo.svg" >

      
      </el-form-item>

    
    </el-form>
</template>

<script lang="ts" setup>




</script>

<style>

  .storeRegisterImageForm {
    width: 400px;
    height: 350px;
    /*padding: 30px;*/
    border-radius: 20px;
    /* 整个表单el-form位于整个屏幕的位置 margin */  
  }
  .storeRegisterImage {
    margin-top:0px;
  }
  
</style>