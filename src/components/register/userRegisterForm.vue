<!-- userRegisterPage的一部分——左侧表单部分 -->

<!-- TODO:
注册按钮：
1.“用户名被使用”出现弹窗
2.“密码不一致”出现弹窗
3.“信息不完整”出现弹窗
4.“注册成功”跳转到userMainPage——用户主页

登录账号按钮：跳转到userLoginPage

返回首页按钮：跳转到firstPage -->

<template>
    <el-form 
      :model="form"
      :rules="rules"
      status-icon
      class="userRegisterForm" 
    >
  
      <h3 class="userRegisterTitle">
        新用户注册
      </h3>
  
      <p class="userRegisterDetail">
        吃饱了才有力气减肥!
      </p>
  
      <el-form-item prop="name" class = "nameInputBoxItem">

        <el-input
          v-model="form.name"
          type="name"
          size="large"
          placeholder="用户名"
          maxlength="20"
          class="nameInputBox"
          >
            <template #prefix>
              <el-icon class="el-input__icon"><user /></el-icon>
            </template>
        </el-input>

      </el-form-item>
  
  
      <el-form-item prop="password" class = "passwordInputBoxItem">
        <el-input
          v-model="form.password"
          type="password"
          placeholder="设置密码"
          show-password
          size="large"
          minlength="6"
          class="passwordInputBox"
        >
          <template #prefix>
            <el-icon class="el-input__icon"><lock /></el-icon>
          </template>
  
        </el-input>
      </el-form-item>

      <el-form-item prop="password_confirm" class = "passwordConfirmBoxItem">
        <el-input
          v-model="form.password_confirm"
          type="password"
          placeholder="确认密码"
          show-password
          size="large"
          class="passwordConfirmBox"
        >
          <template #prefix>
            <el-icon class="el-input__icon"><lock /></el-icon>
          </template>
  
        </el-input>
      </el-form-item>

      <el-form-item prop="address" class = "addressInputBoxItem">
        <el-input
          v-model="form.address"
          type="address"
          placeholder="设置收货地址"
          size="large"
          maxlength="256"
          class="addressInputBox"
        >
          <template #prefix>
            <el-icon class="el-input__icon"><position /></el-icon>
          </template>
  
        </el-input>
      </el-form-item>

      <el-form-item prop="card" class = "cardNumInputBoxItem">
        <el-input
          v-model="form.card"
          type="card"
          placeholder="银行卡卡号"
          size="large"
          maxlength="30"
          class="cardNumInputBox"
        >
          <template #prefix>
            <el-icon class="el-input__icon"><CreditCard /></el-icon>
          </template>
  
        </el-input>
      </el-form-item>


      <el-form-item class = "registerButtonItem">
  
        <el-button 
          color = "#fec01b" 
          round
          plain
          size = "large"
          class = "registerButton"
          @click = "userRegister"
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
  
  <script setup>
  import { reactive, ref } from "vue"
  import { ElMessage } from "element-plus"
  import { user_register } from "@/api/register";

  const form = reactive({
    name: '',
    password: '',
    password_confirm: '',
    address: '',
    card: ''
  })

  const formRef = ref(null)

  const validatePass = (rule, value, callback) => {
    if (value.toString().length < 6) {
      callback(new Error('请设置至少6位的密码'))
    } else {
      if (form.password_confirm !== '') {
        if (!formRef.value) return
        formRef.value.validateField('password_confirm', () => null)
      }
      callback()
    }
  }
  const validatePass2 = (rule, value, callback) => {
    if (value === '') {
      callback(new Error('请再次输入密码'))
    } else if (value !== form.password) {
      callback(new Error('两次输入密码不一致'))
    } else {
      callback()
    }
  }

  const rules = ref({
    name: [
      {
        required: true,
        message: '请输入注册用户名',
        trigger: 'blur'
      },
      {
        max: 256,
        message: '用户名过长，请重新输入'
      }
    ],
    password: [
      {
        required: true,
        validator: validatePass,
        trigger: 'change'
      }
    ],
    password_confirm: [
      {
        required: true,
        validator: validatePass2,
        trigger: 'change'
      }
    ],
    address: [
      {
        required: true,
        message: '请输入收货地址',
        trigger: 'blur'
      }
    ],
    card: [
      {
        required: true,
        message: '请输入正确的银行卡卡号',
        trigger: 'blur'
      }
    ],
  })

  const userRegister = () => {
    user_register({
      name: form.name,
      password: form.password,
      address: form.address,
      card_num: form.card
    }).then(res => {
      let content = res.data
      console.log(content)
      if (content.code === "200") {
        ElMessage({message: content.hint, type: 'success'})
      } else if (content.code === "300") {
        ElMessage({message: content.hint, type: 'error'})
      }
    })
  }
  
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
      margin-bottom: 0;
      margin-top: 0;
    }
  
    .userRegisterDetail {
      width: 80%;
      color: #606266;
      text-align: center;
      font-family: "微软雅黑";
      font-weight:bold;
      margin: 10px auto 30px;
    }

    .nameInputBoxItem {
      width: 300px;
      margin: 0 auto;
      height: 45px;
    /* border: 1px solid black; */
    }

    /* .nameInputBox {
      margin-top: 0%;
      border: 1px solid black;
    } */

    .passwordInputBoxItem {
      width: 300px;
      margin: 10px auto;
      height: 45px;
    }
    
    .passwordConfirmBoxItem {
      width: 300px;
      margin: 10px auto;
      height: 45px;
    }

    .addressInputBoxItem {
      width: 300px;
      margin: 10px auto;
      height: 45px;
    }


    .cardNumInputBoxItem {
      width: 300px;
      margin: 10px auto;
      height: 45px;
    }

    /*.cardPasswordInputBoxItem {*/
    /*  width: 300px;*/
    /*  margin: 10px auto;*/
    /*  height: 45px;*/
    /*}*/
  
    .registerButtonItem {
      width: 300px;
      margin-top:20px;
      margin-left: auto;
      margin-right: auto;
    }

    .registerButton {
      width: 300px;
    }
  
    .loginLinkItem {
      width: 300px;
      padding: 0;
      margin-bottom: 0;
      margin-left: 20%;
    }
  
    .row {
      width : 350px
    }
  
  </style>