<!-- storeLoginPage的一部分——左侧输入表单表单部分 -->

<!-- TODO:
登录按钮：根据输入数据得到的后端返回值实现登录反馈
  1.“店铺未注册”出现弹窗
  2.“密码错误”出现弹窗
  3.“登陆成功”跳转到userMainPage——用户主页  

  注册账号按钮：跳转到storeRegisterPage

-->

<template>
  <el-form 
    :model="form"
    :rules="rules"
    ref="form"
    class="storeLoginForm" 
  >

    <h3 class = "storeLoginTitle">
      我是商家
    </h3>

    <p class = "storeLoginDetail">
      连接千家万户的美食！
    </p>

    <el-form-item prop="name" class = "nameInputBoxItem">
      <el-input
        v-model="input"
        type="name"
        placeholder="店铺名"
        size = "large"
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
        placeholder="密码"
        show-password
        size = "large"
        class = "passwordInputBox"  
      >
        <template #prefix>
          <el-icon class="el-input__icon"><lock /></el-icon>
        </template>

      </el-input>
    </el-form-item>

    <el-form-item class = "rememberBoxItem">

      <el-checkbox label="记住密码" size = "large"/>
      
    </el-form-item>

    <el-form-item class = "loginButtonItem">

      <el-button 
        color = "#fec01b" 
        round
        plain
        size = "large"
        class = "loginButton"  
      >
        登录
      </el-button>

    </el-form-item>

    <el-form-item class = "registerLink">
      <el-row class = "row">
        <el-col :span="12">  
          <el-link @click.native="to_storeRegisterPage" :underline="false">
            注册账号
          </el-link>
          </el-col>
        <el-col :span="12">
          <el-link @click.native="to_firstPage" :underline="false">
            返回首页
          </el-link>
        </el-col>
      </el-row>
    </el-form-item>
  </el-form>
</template>

<script>
import {defineComponent} from "vue";

export default defineComponent({
  methods: {
    to_firstPage(){
      this.$router.push({path: '/'})
    },
    to_storeRegisterPage(){
      this.$router.push({path: '/storeRegisterPage'})
    }
  }
})

</script>

<style>
  .storeLoginForm {
    width: 350px;
    height: 450px;
    border-radius: 20px;
    /* 整个表单el-form位于整个屏幕的位置 margin */ 
  }
  .storeLoginTitle {
    color :black;
    font-size: 35px;
    text-align: center;
    margin-bottom: 0px;
  }

  .storeLoginDetail {
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
  
  .nameInputBoxItem {
    width: 300px;
    width: 300px;
    margin-top: 0px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 0px;
    height: 45px;
  }
  
  .passwordInputBoxItem {
    width: 300px;
    margin-bottom: 10px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 10px;
    height: 45px;
  }

  .rememberBoxItem {
    width: 100px;
    margin-top: 30px;
    margin-bottom: 0px;
    margin-left: 30px;
  }


  .loginButtonItem {
    width: 300px;
    margin-top:0px;
    margin-left: auto;
    margin-right: auto;
    
  }

  .loginButton {
    width: 300px;
  }

  .el-link {
    margin-right: 8px;
  }
  .el-link .el-icon--right.el-icon {
    vertical-align: text-bottom;
  }

  .registerLink {
    width: 300px;
    padding: 0 0 0 35px;
    margin: 0 0 30px 30px;
  }

  .row {
    width : 350px
  }

</style>