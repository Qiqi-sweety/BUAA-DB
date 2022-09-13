<template>

    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="userLoginImageForm"
      
    >
      <el-form-item class = "userImage">
        <img alt="userLoginLogo" src="../../assets/userLogo.svg" >
      </el-form-item>  
    </el-form>

  
</template>

<script lang="ts" setup>

</script>

<style>

  .userLoginImageForm {
    width: 400px;
    height: 450px;
    /*padding: 30px;*/
    border-radius: 20px;
    /* 整个表单el-form位于整个屏幕的位置 margin */  
  }
  .userImage {
    margin-top: 80px;
  }
  
</style>