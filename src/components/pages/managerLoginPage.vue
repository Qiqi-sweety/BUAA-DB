<!-- 管理员登录页面 -->

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
            <el-col :span="9"></el-col>
            <el-col :span="7">
              <n-button @click.native="to_userLoginPage" quaternary ghost class = "becomeUserButtonClass" color = "black">
                用户登录
              </n-button>
              <n-button @click.native="to_storeLoginPage" quaternary ghost class = "becomeStoreButtonClass" color = "black">
                商家登录
              </n-button>
            </el-col>
          </el-row> 
        </el-header>
        <el-main>
          <div>
            <el-card
            style = "margin:auto;
                    width: 1000px;
                    height: 550px;
                    padding-left: 0;
                    padding-top: 0;
                    margin-top:100px;"
            >
              <el-row style = "padding-top: 0;">
                <el-col :span="12" 
                style = "height: 510px;
                        padding-top: 25px;"
                >
                  <managerLoginForm style = "margin:auto;"/>
                </el-col>

                <el-col :span="12" 
                  style = "padding-top: 100px;
                  padding-left: 35px;
                  height: 510px;">
                  <img alt="managerLoginLogo" src="../../assets/managerLogo.svg" >
                </el-col>
              </el-row>
            </el-card>
          </div>
        </el-main>
      </el-container>
    </div>
  </template>
    
  <script>
    import { defineComponent } from 'vue'
    import { NTag,NButton} from 'naive-ui'
    import managerLoginForm from '../login/managerLoginForm.vue'
    
    export default defineComponent({
      name: 'managerLoginPage',
      components: {
        managerLoginForm,
        NTag,
        NButton,
      },
      methods: {
        to_userLoginPage(){
          this.$router.push({path: '/userLoginPage'})
        },
        to_storeLoginPage(){
          this.$router.push({path: '/storeLoginPage'})
        }
      }
    })
  </script>
    
  <style>
    /*.el-header {*/
    /*  !* background-color: #f4d870; *!*/
    /*  height: 60px;*/
    /*  background-color: white;*/
    /*}*/
    
    /*.el-main {*/
    /*  height: 870px;*/
    /*}*/

    .becomeUserButtonClass {
      margin: 20px 0 0 0;
    }

    .becomeStoreButtonClass {
      margin: 20px 0 0 0;
    }
    
  </style>