<!-- userLoginPage的一部分——左侧输入表单表单部分 -->

<!-- TODO:
根据输入数据得到的后端返回值实现登录反馈
  1.“用户未注册”出现弹窗
  2.“密码错误”出现弹窗
  3.“登陆成功”跳转到userMainPage——用户主页
-->

<template>
  <el-form 
    :model="form"
    :rules="rules"
    ref="form"
    class="userLoginForm" 
  >

    <h3 class = "userLoginTitle">
      我要点餐
    </h3>

    <p class = "userLoginDetail">
      吃饱了才有力气减肥!
    </p>

    <el-form-item prop="name" class = "nameInputBoxItem">
      <el-input
        v-model="inputName"
        type="name"
        placeholder="用户名"
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
        v-model="inputPw"
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
        @click="login_in"
      >
        登录
      </el-button>

    </el-form-item>

    <el-form-item class = "registerLink">
      <el-row class = "row">
        <el-col :span="12">  
          <el-link @click.native="to_userRegisterPage" :underline="false">
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
import {defineComponent, inject} from "vue";

export default defineComponent({
  data() {
    return {
      inputName: '',
      inputPw: '',
    }
  },
  methods: {
    to_firstPage(){
      this.$router.push({path: '/'})
    },
    to_userRegisterPage(){
      this.$router.push({path: '/userRegisterPage'})
    },
    login_in(){
      inject("$axios")
          .get("http://127.0.0.1:8000/search/", {
            label: this.inputLabel,
            key: this.inputKey,
          })
          .then((val) => {
            console.log(val);
            if (this.label === "店铺") {
              this.stores = val.list
            } else {
              this.food = val.list
            }
          });
    }
  }
})

</script>

<style>
  .userLoginForm {
    width: 350px;
    height: 450px;
    border-radius: 20px;
    /* 整个表单el-form位于整个屏幕的位置 margin */ 
  }
  .userLoginTitle {
    color :black;
    font-size: 35px;
    text-align: center;
    margin-bottom: 0;
  }

  .userLoginDetail {
    width:80%;
    color :#606266;
    text-align: center;
    font-family: "微软雅黑";
    font-weight:bold;
    margin: 10px auto 30px;

  }
  
  .nameInputBoxItem {
    width: 300px;
    margin: 0 auto;
    height: 45px;
  }

  .passwordInputBoxItem {
    width: 300px;
    margin: 10px auto;
    height: 45px;
  }

  .rememberBoxItem {
    width: 100px;
    margin-top: 30px;
    margin-bottom: 0;
    margin-left: 30px;
  }

  .loginButtonItem {
    width: 300px;
    margin-top: 0;
    margin-left: auto;
    margin-right: auto;
    
  }

  .loginButton {
    width: 300px;
  }

  .el-link {
    vertical-align: text-bottom;
  }

  .registerLink {
    width: 300px;
    margin: 0 0 0 60px;
    padding: 0 0 0 35px;
    /* border:2px solid black; */
  }

  .row {
    width : 350px
  }

</style>

