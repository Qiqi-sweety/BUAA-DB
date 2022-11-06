<!-- 商家登录页面 -->

<template>
    <div class="loginLayout">
      <el-container>
        <el-header>
            <el-row>
            <el-col :span="4">
                <img alt="Logo" src="../../assets/logo.png" class = "topLogoClass">         
            </el-col>
            <el-col :span="4">
                <n-tag class = "locationTagClass" :bordered="false">
                    北京市
                    <template #icon>
                        <el-icon><Location /></el-icon>
                    </template>
                </n-tag>
            </el-col>
            <el-col :span="4">
                <div class="grid-content ep-bg-purple" />
                
            </el-col>
            <el-col :span="9"><div class="grid-content ep-bg-purple-light" /></el-col>
            
            <el-col :span="3">

              <n-button @click.native="to_userLoginPage" quaternary ghost class = "managerButtonClass" color = "black">
                用户登录
              </n-button>

              <n-button @click.native="to_managerLoginPage" quaternary ghost class = "logoutButtonClass" color = "black">
                管理员登录
              </n-button>
            </el-col>
          </el-row> 
    
        </el-header>
        <el-main>
          <div class = "LoginClass">
            <el-card class="storeBoxCard"
            style = "  margin:auto;
            width: 1000px;
            height: 550px;
            padding-left: 0px;
            padding-top:0px;"
            >
              <el-row style = "padding-top: 0px;">
                <el-col :span="12" 
                style = "height: 510px;
                        padding-top: 25px;"
                >
                  <storeLoginForm style = " margin:auto;"/>
                </el-col>

                <el-col :span="12" 
                  style = "padding-top: 100px;
                  padding-left: 35px;
                  height: 510px;"
                >
                  <img alt="storeLoginLogo" src="../../assets/storeLogo.svg" > 
                </el-col>
              </el-row>
            </el-card>
          </div>
        </el-main>
      </el-container>
    </div>
  </template>
    
  <script>
    import { defineComponent ,ref } from 'vue'
    import { NTag,NButton} from 'naive-ui'
    import storeLoginForm from '../login/storeLoginForm.vue'
    
    export default defineComponent({
      name: 'storeLoginPage',
      components: {
        storeLoginForm,
        NTag,
        NButton,
      },
      methods: {
        to_userLoginPage(){
          this.$router.push({path: '/userLoginPage'})
        },
        to_managerLoginPage(){
          this.$router.push({path: '/managerLoginPage'})
        }
      }
    })
  </script>
    
  <style>
    .el-header {
      /* background-color: #f4d870; */
      height: 60px;
      background-color: white;
    }
    
    .el-main {
      height: 870px;
    }
    
    .LoginClass {
      margin-top:100px;
    }
    
  </style>