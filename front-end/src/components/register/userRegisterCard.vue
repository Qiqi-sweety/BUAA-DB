<template>
    <el-card class="userRegisterBoxCard">
      <el-row class = "userRegisterRow">
        <el-col :span="12" class = "userRegisterFormCol">
           <userRegisterForm class = "userRegisterFormClass"/>
        </el-col>
  
  
        <el-col :span="12" class = "userRegisterImageFormCol">
          <userRegisterImageForm class = "userRegisterImageFormClass"/>
        </el-col>
  
  
      </el-row>
    </el-card>
  </template>
  
  <script>
  import userRegisterForm from './userRegisterForm.vue'
  import userRegisterImageForm from './userRegisterImageForm.vue'
  export default {
    name: 'userRegisterCard',
    components: {
      userRegisterForm,  
      userRegisterImageForm,
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
  
  .userRegisterRow {
    padding-top: 0px;
  }
  
  .userRegisterBoxCard {
    margin:auto;
    width: 1000px;
    height: 650px;
    padding-left: 0px;
    padding-top:0px;
  }
  
  .userRegisterFormCol {
    height: 510px;
    padding-top: 25px;
  
    
  }
  
  .userRegisterImageFormCol {
    padding-top: 25px;
    padding-left: 35px;
    height: 510px;
  }
  
  
  
  .userRegisterFormClass {
    margin:auto;
    
  }
  
  .userRegisterImageFormClass {
    border-radius: 20px;
    margin-top:0px;
  }
  
  </style>