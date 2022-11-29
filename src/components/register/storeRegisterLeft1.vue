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
      status-icon
      class="storeRegisterLeft1" 
    >
  
      <el-form-item prop="name" class = "nameInputBoxItem">
        <el-input
          v-model="form.name"
          type="name"
          placeholder="店铺名"
          size = "large"
          class = "nameInputBox"
        >
          <template #prefix>
            <el-icon class="el-input__icon"><Shop /></el-icon>
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

      <el-form-item class = "nextStepButtonItem">
  
        <el-button 
          color="#fec01b"
          round
          plain
          size="large"
          class="nextStepButton"
          @click="storeRegister1"
        >
          下一步
        </el-button>
  
      </el-form-item>

      <el-form-item class = "loginLink">
        
        <el-row class = "row">
        <el-col :span="12">  
          <el-link :underline="false" @click="to_storeLoginPage">
            登录账号
          </el-link>
        </el-col>
        <el-col :span="12">
          <el-link :underline="false" @click="to_firstPage">
            返回首页
          </el-link>
        </el-col>
      </el-row>
          
      </el-form-item>
    </el-form>
  </template>
  
  <script setup>
  import {reactive, ref} from "vue"
  import {ElMessage} from "element-plus"
  import {store_register_1} from "@/api/register";
  import {useRouter} from "vue-router";
  const router = useRouter()

  const form = reactive({
    name: '',
    password: '',
    password_confirm: ''
  })

  let formRef = ref(null)

  const validatePass = (rule, value, callback) => {
    if (value.toString().length < 6) {
      callback(new Error('请设置至少6位的密码'))
    } else {
      if (!formRef.value) return
      formRef.value.validateField('password_confirm', () => null)
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
        message: '请输入注册店铺名',
        trigger: 'blur'
      },
      {
        max: 256,
        message: '用户名过长，请重新输入',
        trigger: 'change'
      }
    ],
    password: [
      {
        validator: validatePass,
        trigger: 'change'
      },
      {
        required: true,
        validator: validatePass,
        trigger: 'blur'
      }
    ],
    password_confirm: [
      {
        validator: validatePass2,
        trigger: 'change'
      },
      {
        required: true,
        validator: validatePass2,
        trigger: 'blur'
      }
    ]
  })

  const storeRegister1 = () => {
    if (form.password !== form.password_confirm) {
      ElMessage({message: "未确认密码", type: "error"})
      return
    }
    let data = {
      name: form.name,
      password: form.password,
    }
    console.log(data)
    store_register_1(data)
        .then(res => {
          let content = res.data
          console.log(content)
          if (content.code === '200') {
            router.push({
              name: 'storeRegisterCard2',
              query: data,
            })
          } else {
            ElMessage({message: content.message, type: content.hint})
          }
        })
  }

  const to_storeLoginPage = () => {
    router.push('/storeLoginPage')
  }

  const to_firstPage = () => {
    router.push('/')
  }
  </script>
  
  <style>
    .storeRegisterLeft1 {
      /*width: 350px;*/
      width: 80%;
      height: 350px;
      border-radius: 20px;
      margin-top: 50px;
      /* 整个表单el-form位于整个屏幕的位置 margin */ 
    }
    
    /*.nameInputBox {*/
    /*  width: 300px;*/
    /*  margin: 10px auto;*/
    /*  height: 45px;*/
    /*}*/

    /*.passwordInputBox {*/
    /*  width: 300px;*/
    /*  margin: 10px auto;*/
    /*  height: 45px;*/
    /*}*/
    /*.passwordConfirmBox {*/
    /*  width: 300px;*/
    /*  margin: 10px auto;*/
    /*  height: 45px;*/
    /*}*/

    .nextStepButtonItem {
      width: 300px;
      margin: 20px auto;
    }

    .nextStepButton {
      width: 300px;
      margin: 20px auto;
    }
  
    .loginLink {
      width: 300px;
      margin: 0 0 0 80px;
      /* border:2px solid black; */

      padding: 20px 0 0;
    }
  
    .row {
      width : 350px
    }
  
  </style>