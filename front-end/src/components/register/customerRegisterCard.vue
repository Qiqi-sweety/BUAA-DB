<template>
    <el-card class="customerBoxCard">
      <el-row class = "customerRegisterRow">
        <el-col :span="12" class = "customerRegisterFormCol">
           <customerRegisterForm class = "customerRegisterFormClass"/>
        </el-col>
  
  
        <el-col :span="12" class = "customerRegisterImageFormCol">
          <customerRegisterImageForm class = "customerRegisterImageFormClass"/>
        </el-col>
  
  
      </el-row>
    </el-card>
  </template>
  
  <script>
  import customerRegisterForm from './customerRegisterForm.vue'
  import customerRegisterImageForm from './customerRegisterImageForm.vue'
  export default {
    name: 'customerRegisterCard',
    components: {
      customerRegisterForm,  
      customerRegisterImageForm,
    }
  }
  </script>
  
  
  
  <style>
  .text {
    font-size: 14px;
  }
  
  .item {
    padding: 0px;
    margin-bottom: 18px;
  }
  
  .customerRegisterRow {
    padding-top: 0px;
  }
  
  .customerBoxCard {
    margin:auto;
    width: 1000px;
    height: 550px;
    padding-left: 0px;
    padding-top:0px;
  }
  
  .customerRegisterFormCol {
    height: 510px;
    padding-top: 25px;
  
    
  }
  
  .customerRegisterImageFormCol {
    padding-top: 25px;
    padding-left: 35px;
    height: 510px;
  }
  
  
  
  .customerRegisterFormClass {
    margin:auto;
    
  }
  
  .customerRegisterImageFormClass {
    border-radius: 20px;
    margin-top:0px;
  }
  
  </style>