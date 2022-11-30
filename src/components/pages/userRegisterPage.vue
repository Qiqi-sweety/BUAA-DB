<!-- 用户注册页面 -->


<template>
    <div class="registerLayout">
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
            </el-col>
            <el-col :span="9"></el-col>
            
            <el-col :span="3">

                <n-button @click.native="to_storeLoginPage" quaternary ghost class = "managerButtonClass" color = "black">
                    商家登录
                </n-button>

                <n-button @click.native="to_managerLoginPage" quaternary ghost class = "logoutButtonClass" color = "black">
                    管理员登录
                </n-button>
            </el-col>
          </el-row> 
  
        </el-header>
        <el-main>
          <div style = "margin-top: 5%;">
            <el-card 
            style = "margin:auto;
                width: 1000px;
                height: 650px;
                padding-left: 0;
                padding-top: 0;"
            >
              <el-row style = "padding-top: 0;">
                <el-col :span="12" 
                style = "height: 510px;
                        padding-top: 25px;">
                  <userRegisterForm style = "margin:auto;"/>
                </el-col>
                <el-col :span="12" 
                style = "padding-top: 150px;
                        padding-left: 35px;
                        height: 510px;"
                >
                  <img alt="userRegisterLogo" src="../../assets/userLogo.svg" >
                </el-col>
              </el-row>
            </el-card>
          </div>
        </el-main>
      </el-container>
    </div>
    
</template>
  
<script>
  import userRegisterForm from '../register/userRegisterForm.vue'
  import { defineComponent } from 'vue'
  import { NTag,NButton} from 'naive-ui'

  export default defineComponent({
    name: 'userRegisterPage',
    components: {
      userRegisterForm,
      NButton,
      NTag,
    },
    methods: {
      to_storeLoginPage(){
        this.$router.push({path: '/storeLoginPage'})
      },
      to_managerLoginPage(){
        this.$router.push({path: '/managerLoginPage'})
      }
    }
  })
</script>
  
<style>
  /*.el-header {*/
  /*  height: 60px;*/
  /*  background-color: white;*/
  /*}*/
  
  /*.el-main {*/
  /*  height: 870px;*/
  /*}*/
  
</style>