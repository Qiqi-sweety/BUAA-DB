<!-- manageLoginPage的一部分——左侧输入表单表单部分 -->

<!-- TODO:
根据输入数据得到的后端返回值实现登录按钮反馈
  1.“管理员未注册”出现弹窗
  2.“密码错误”出现弹窗
  3.“登陆成功”成功跳转到manageMainPage——管理员主页
-->

<template>
  <el-form
    class="managerLoginForm" 
  >

    <h3 class = "managerLoginTitle">
      我是管理员
    </h3>

    <p class = "managerLoginDetail">
      专业管理为你保驾护航！
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

      <el-checkbox v-model="remPw" label="记住密码" size = "large"/>
      
    </el-form-item>

    <el-form-item class = "loginButtonItem">

      <el-button 
        color = "#fec01b"
        round
        plain
        size = "large"
        class = "loginButton"
        @click="managerLogin"
      >
        登录
      </el-button>

    </el-form-item>

    <el-form-item class = "managerLink">
      <el-row style = "width : 350px;">
        <el-col :span="12"></el-col>
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
import {login} from "@/api/login";
import {ElMessage} from "element-plus";

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
    managerLogin(){
      login({
        name: this.inputName,
        password: this.inputPw
      }).then(res => {
        let content = res.data
        console.log(content)
        ElMessage({message: content.message, type: content.hint})
        if (content.code === '200') {
          this.$router.push('/managerMainPage')
        }
      })
    }
  }
})

</script>

<style>
  .managerLoginForm {
    width: 350px;
    height: 450px;
    border-radius: 20px;
    /* 整个表单el-form位于整个屏幕的位置 margin */ 
  }
  .managerLoginTitle {
    color :black;
    font-size: 35px;
    text-align: center;
    margin-bottom: 0px;
  }

  .managerLoginDetail {
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
    margin-top: 0%;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 0%;
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
    margin-top: 0px;
    margin-bottom: 0px;
    margin-left: 30px;
  }

  .loginButtonItem {
    width: 300px;
    margin-top: 0px;
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

  .managerLink {
    width: 300px;
    margin: 0 0 0 30px;
    padding: 0 0 0 35px;
  }

</style>