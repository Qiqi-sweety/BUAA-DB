<template>
    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="businessRegisterForm2" 
    >

      <el-form-item prop="name" class = "shopNameInputBox">
        <el-input
          v-model="input"
          type="name"
          placeholder="小店名称"
          size = "large"
          class = "shopNameInputBoxClass"
        >
          <template #prefix>
            <el-icon class="el-input__icon"><user /></el-icon>
          </template>
        </el-input>
  
      </el-form-item>
  
      <el-form-item prop="address" class = "shopAddressInputBox">
        <el-input
          v-model="input"
          type="address"
          placeholder="小店地址"
          size = "large"
          class = "shopAddressInputBoxClass"
        >
          <template #prefix>
            <el-icon class="el-input__icon"><location /></el-icon>
          </template>
        </el-input>
  
      </el-form-item>

      <el-form-item prop="intro" class = "introInputBox">
        <el-input
            v-model="textarea2"
            :autosize="{ minRows: 3, maxRows: 4 }"
            type="textarea"
            placeholder="小店介绍"
        >
          
  
        </el-input>
      </el-form-item>

      
      <el-form-item class = "nextStepButton">
  
        <el-button 
          color = "#fec01b" 
          :dark="isDark" 
          round
          plain
          size = "large"
          class = "nextStepButton"  
        >
          提交申请
        </el-button>
  
      </el-form-item>

      
  
      <el-form-item class = "loginLink">
        
        <el-row class = "row">
        <el-col :span="12">  
            <el-link :underline="false">
            登录账号
          </el-link>
          </el-col>
        <el-col :span="12">
          <el-link :underline="false">
            返回首页
          </el-link>
        </el-col>
      </el-row>
          
      </el-form-item>
    </el-form>
  </template>
  
  <script lang="ts" setup>
  
  </script>
  
  <style scoped>
    .businessRegisterForm2 {
      width: 350px;
      height: 350px;
      border-radius: 20px;
      margin-top:0px;
      /* 整个表单el-form位于整个屏幕的位置 margin */ 
    }

    .shopNameInputBox {
      width: 300px;
      width: 300px;
      margin-top: 10px;
      margin-left: auto;
      margin-right: auto;
      margin-bottom: 10px;
      height: 45px;
      
    }
    
    .shopAddressInputBox {
      width: 300px;
      width: 300px;
      margin-top: 10px;
      margin-left: auto;
      margin-right: auto;
      margin-bottom: 10px;
      height: 45px;
      
    }



    
  
    .introInputBox {
      width: 300px;
      margin-bottom: 10px;
      margin-left: auto;
      margin-right: auto;
      margin-top: 20px;
      height: 70px;
    }



    .nextStepButton {
      width: 300px;
      margin-top:20px;
      margin-left: auto;
      margin-right: auto;
      
    }
  
    .el-link {
      margin-right: 8px;
    }
    .el-link .el-icon--right.el-icon {
      vertical-align: text-bottom;
    }
  
    .loginLink {
      width: 300px;
      margin: 0px 0px 0px 70px;
      padding: 0px 0px 0px auto;
      padding-left: 0px;
      /* border:2px solid black; */

      margin-bottom: 0px;
    }
  
    .row {
      width : 350px
    }
  
  </style>