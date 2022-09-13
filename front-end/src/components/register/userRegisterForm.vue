<template>
    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="userRegisterForm" 
    >
  
      <h3 class = "userRegisterTitle">
        新用户注册
      </h3>
  
      <p class = "userRegisterDetail">
        吃饱了才有力气减肥!
      </p>
  
      <el-form-item prop="name" class = "nameInputBoxItem">

        <el-input
          v-model="input"
          type="name"
          size = "large"
          placeholder="用户名"
          class = "nameInputBox"
          >
            <template #prefix>
              <el-icon class="el-input__icon"><user /></el-icon>
            </template>
          </el-input>

      </el-form-item>
  
  
      <el-form-item prop="password" class = "passwordInputBoxItem">
        <el-input
          v-model="input"
          type="password"
          placeholder="设置密码"
          show-password
          size = "large"
          class = "passwordInputBox"  
        >
          <template #prefix>
            <el-icon class="el-input__icon"><lock /></el-icon>
          </template>
  
        </el-input>
      </el-form-item>

      <el-form-item prop="password" class = "passwordConfirmBoxItem">
        <el-input
          v-model="input"
          type="password"
          placeholder="确认密码"
          show-password
          size = "large"
          class = "passwordConfirmBox"  
        >
          <template #prefix>
            <el-icon class="el-input__icon"><lock /></el-icon>
          </template>
  
        </el-input>
      </el-form-item>

      <el-form-item prop="address" class = "addressInputBoxItem">
        <el-input
          v-model="input"
          type="address"
          placeholder="设置收获地址"
          size = "large"
          class = "addressInputBox"  
        >
          <template #prefix>
            <el-icon class="el-input__icon"><position /></el-icon>
          </template>
  
        </el-input>
      </el-form-item>

      <el-form-item prop="card_num" class = "cardNumInputBoxItem">
        <el-input
          v-model="input"
          type="card_num"
          placeholder="银行卡卡号"
          size = "large"
          class = "cardNumInputBox"  
        >
          <template #prefix>
            <el-icon class="el-input__icon"><CreditCard /></el-icon>
          </template>
  
        </el-input>
      </el-form-item>


      <el-form-item prop="card_password" class = "cardPasswordInputBoxItem">
        <el-input
          v-model="input"
          type="card_password"
          placeholder="银行卡密码"
          show-password
          size = "large"
          class = "cardPasswordInputBox"  
        >
          <template #prefix>
            <el-icon class="el-input__icon"><lock /></el-icon>
          </template>
  
        </el-input>
      </el-form-item>


      <el-form-item class = "registerButtonItem">
  
        <el-button 
          color = "#fec01b" 
          :dark="isDark" 
          round
          plain
          size = "large"
          class = "registerButton"  
        >
          注册
        </el-button>
  
      </el-form-item>

      
  
      <el-form-item class = "loginLinkItem">
        
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
    .userRegisterForm {
      /* width: 350px; */
      width: 80%;
      height: 580px;
      /* border:2px solid black; */
      /* border: 2px solid black; */
      /* 整个表单el-form位于整个屏幕的位置 margin */ 
    }
    .userRegisterTitle {
      color :black;
      font-size: 35px;
      text-align: center;
      margin-bottom: 0%;
      margin-top: 0%;
    }
  
    .userRegisterDetail {
      width:80%;
      color :#606266;
      text-align: center;
      margin-top: 10px;
      font-family: "微软雅黑";
      margin-left: auto;
      margin-right: auto;
      font-weight:bold;
      margin-bottom: 30px;
    }

    .Label {
      /* font-weight: bold; */
    }

    

    .NameInputBoxItem {
    width: 300px;
    margin-top: 0%;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 0%;
    height: 45px;
    /* border: 1px solid black; */
  }


  /* .nameInputBox {
    margin-top: 0%;
    border: 1px solid black;
  } */

  .passwordInputBoxItem {
    width: 300px;
    margin-bottom: 10px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 10px;
    height: 45px;
  }
    
    .passwordConfirmBoxItem {
      width: 300px;
      margin-bottom: 10px;
      margin-left: auto;
      margin-right: auto;
      margin-top: 10px;
      height: 45px;
    }

    .addressInputBoxItem {
      width: 300px;
      margin-bottom: 10px;
      margin-left: auto;
      margin-right: auto;
      margin-top: 10px;
      height: 45px;
    }


    .cardNumInputBoxItem {
      width: 300px;
      margin-bottom: 10px;
      margin-left: auto;
      margin-right: auto;
      margin-top: 10px;
      height: 45px;
    }

    .cardPasswordInputBoxItem {
      width: 300px;
      margin-bottom: 10px;
      margin-left: auto;
      margin-right: auto;
      margin-top: 10px;
      height: 45px;
    }
  
    .registerButtonItem {
      width: 300px;
      margin-top:20px;
      margin-left: auto;
      margin-right: auto;
    }

    .registerButton {
      width: 300px;
    }
  
    .el-link {
      margin-right: 8px;
    }
    .el-link .el-icon--right.el-icon {
      vertical-align: text-bottom;
    }
  
    .loginLinkItem {
      width: 300px;
      padding: 0px 0px 0px auto;
      padding-left: 0px;
      margin-bottom: 0%;
      margin-left: 20%;
    }
  
    .row {
      width : 350px
    }
  
  </style>