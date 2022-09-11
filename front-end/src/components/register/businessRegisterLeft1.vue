<template>
    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="businessRegisterForm1" 
    >
  
      <el-form-item prop="username" class = "idInputBox">
        <el-input
          v-model="input"
          type="id"
          placeholder="用户名"
          size = "large"
          class = "idInputBoxClass"
        >
          <template #prefix>
            <el-icon class="el-input__icon"><user /></el-icon>
          </template>
        </el-input>
  
      </el-form-item>
  
  
      <el-form-item prop="password" class = "passwordInputBox">
        <el-input
          v-model="input"
          type="password"
          placeholder="设置密码"
          show-password
          size = "large"
          class = "passwordInputBoxClass"  
        >
          <template #prefix>
            <el-icon class="el-input__icon"><lock /></el-icon>
          </template>
  
        </el-input>
      </el-form-item>

      <el-form-item prop="password" class = "passwordConfirmBox">
        <el-input
          v-model="input"
          type="password"
          placeholder="确认密码"
          show-password
          size = "large"
          class = "passwordConfirmBoxClass"  
        >
          <template #prefix>
            <el-icon class="el-input__icon"><lock /></el-icon>
          </template>
  
        </el-input>
      </el-form-item>



  
      
  
      <el-form-item class = "nextStepButtonItem">
  
        <el-button 
          color = "#fec01b" 
          :dark="isDark" 
          round
          plain
          size = "large"
          class = "nextStepButton"  
        >
          下一步
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
    .businessRegisterForm1 {
      width: 350px;
      height: 350px;
      border-radius: 20px;
      margin-top:0px;
      /* 整个表单el-form位于整个屏幕的位置 margin */ 
    }
    
    .idInputBox {
      width: 300px;
      width: 300px;
      margin-top: 10px;
      margin-left: auto;
      margin-right: auto;
      margin-bottom: 10px;
      height: 45px;
      
    }
  
    .passwordInputBox {
      width: 300px;
      margin-bottom: 10px;
      margin-left: auto;
      margin-right: auto;
      margin-top: 10px;
      height: 45px;
    }
    .passwordConfirmBox {
      width: 300px;
      margin-bottom: 10px;
      margin-left: auto;
      margin-right: auto;
      margin-top: 10px;
      height: 45px;
    }

    .nextStepButton {
      width: 300px;
      margin-top:20px;
      margin-left: auto;
      margin-right: auto;
      margin-bottom: 20px;
      
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

      padding-top: 20px;
    }
  
    .row {
      width : 350px
    }
  
  </style>