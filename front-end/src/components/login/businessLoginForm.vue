<template>
  <el-form 
    :model="form"
    :rules="rules"
    ref="form"
    class="businessLoginForm" 
  >

    <h3 class = "businessLoginTitle">
      我是商家
    </h3>

    <p class = "businessLoginDetail">
      连接千家万户的美食！
    </p>

    <el-form-item prop="username" class = "idInputBox">
      <el-input
        v-model="input"
        type="id"
        placeholder="用户名"
        size = "large"
        class = "idInputBox"
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

    <el-form-item class = "rememberBox">

      <el-checkbox label="记住密码" size = "large"/>
      
    </el-form-item>

    <el-form-item class = "loginButton">

      <el-button 
        color = "#fec01b" 
        :dark="isDark" 
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
          <el-link :underline="false">
            注册账号
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
  .businessLoginForm {
    width: 350px;
    height: 450px;
    border-radius: 20px;
    /* 整个表单el-form位于整个屏幕的位置 margin */ 
  }
  .businessLoginTitle {
    color :black;
    font-size: 35px;
    text-align: center;
    margin-bottom: 0px;
  }

  .businessLoginDetail {
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
  
  .idInputBox {
    width: 300px;
    width: 300px;
    margin-top: 0px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 0px;
    height: 45px;
  }

  .passwordInputBox {
    width: 300px;
    margin-bottom: 0px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 10px;
    height: 45px;
  }

  .rememberBox {
    width: 100px;
    margin-top: 30px;
    margin-bottom: 0px;
    margin-left: 30px;
  }

  .loginButton {
    width: 300px;
    margin-top:0px;
    margin-left: auto;
    margin-right: auto;
    
  }

  .el-link {
    margin-right: 8px;
  }
  .el-link .el-icon--right.el-icon {
    vertical-align: text-bottom;
  }

  .registerLink {
    width: 300px;
    margin: 0px 0px 0px 30px;
    padding: 0px 0px 0px auto;
    padding-left: 35px;
  }

  .row {
    width : 350px
  }

</style>