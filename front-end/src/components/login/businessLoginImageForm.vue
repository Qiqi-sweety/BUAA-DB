<template>
    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="businessLoginImageForm"
      
    >
      <el-form-item class = "businessImage">
        <img alt="businessLoginLogo" src="../../assets/businessLogo.svg" > 
      </el-form-item>
    </el-form>

  
</template>

<script lang="ts" setup>

</script>

<style>

  .businessLoginImageForm {
    width: 400px;
    height: 450px;
    border-radius: 20px;
  }
  .businessImage {
    margin-top: 80px;
  }
  
</style>