<!-- storeRegisterCard1的组件:左侧表单获得商家注册的店铺名和密码部分-->

<!-- TODO:
下一步按钮：根据后端返回值
1.“密码不一致”出现弹窗
2.“店铺名已被使用”出现弹窗
3.“成功”发送一个信号给storeRegisterCard1，然后storeRegisterCard1把信号传给storeRegisterPage，storeRegisterPage会切换到storeRegisterCard2组件

登录账号按钮：跳转到storeRegisterPage

返回首页按钮：跳转到firstPage -->


<template>
    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="storeRegisterLeft1" 
    >
  
      <el-form-item prop="name" class = "nameInputBox">
        <el-input
          v-model="input"
          type="name"
          placeholder="店铺名"
          size = "large"
          class = "nameInputBoxClass"
        >
          <template #prefix>
            <el-icon class="el-input__icon"><Shop /></el-icon>
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
  
  <style>
    .storeRegisterLeft1 {
      width: 350px;
      height: 350px;
      border-radius: 20px;
      margin-top:0px;
      /* 整个表单el-form位于整个屏幕的位置 margin */ 
    }
    
    .nameInputBox {
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
      margin: 0 0 0 70px;
      /* border:2px solid black; */

      padding: 20px 0 0;
    }
  
    .row {
      width : 350px
    }
  
  </style>