<!-- userLoginPage的一部分——左侧输入表单表单部分 -->

<template>
  <el-form
    class="userLoginForm" 
  >

    <h3 class = "userLoginTitle">
      我要点餐
    </h3>

    <p class = "userLoginDetail">
      吃饱了才有力气减肥!
    </p>

    <el-form-item class = "nameInputBoxItem">
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


    <el-form-item class = "passwordInputBoxItem">
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

      <el-checkbox v-model="remPw" label="记住密码" size="large"/>
      
    </el-form-item>

    <el-form-item class = "loginButtonItem">

      <el-button 
        color="#fec01b"
        round
        plain
        size="large"
        class="loginButton"
        @click="userLogin"
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
import {defineComponent} from "vue";
import {ElMessage} from "element-plus";
import {login} from "@/api/login"

export default defineComponent({
  data() {
    return {
      inputName: '',
      inputPw: '',
      remPw: false
    }
  },
  methods: {
    to_firstPage(){
      this.$router.push({path: '/'})
    },
    to_userRegisterPage(){
      this.$router.push({path: '/userRegisterPage'})
    },
    userLogin(){
      login({
        name: this.inputName,
        password: this.inputPw
      }).then(res => {
        let content = res.data
        console.log(content)
        ElMessage({message: content.message, type: content.hint})
        if (content.code === '200') {
          this.$router.push('/userMainPage')
        }
      })
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

