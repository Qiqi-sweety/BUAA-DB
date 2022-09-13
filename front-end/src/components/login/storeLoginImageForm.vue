<template>
    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="storeLoginImageForm"
      
    >
      <el-form-item class = "storeImage">
        <img alt="storeLoginLogo" src="../../assets/storeLogo.svg" > 
      </el-form-item>
    </el-form>

  
</template>

<script lang="ts" setup>

</script>

<style>

  .storeLoginImageForm {
    width: 400px;
    height: 450px;
    border-radius: 20px;
  }
  .storeImage {
    margin-top: 80px;
  }
  
</style>