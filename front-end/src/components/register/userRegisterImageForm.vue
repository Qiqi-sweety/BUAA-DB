<template>

    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="userRegisterImageForm"
      
    >
      <el-form-item class = "userImage">

        <img alt="userRegisterLogo" src="../../assets/userLogo.svg" >

      
      </el-form-item>
    </el-form>

  
</template>

<script lang="ts" setup>

</script>

<style>

  .userRegisterImageForm {
    width: 100%;
    height: 100%;
    /* 整个表单el-form位于整个屏幕的位置 margin */  
  }
  .userImage {
    margin-top: 30%;
  }
  
</style>