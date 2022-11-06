<!-- 首页 -->

<template>
    <router-view></router-view>
    <div>
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
            <el-col :span="4"></el-col>
            <el-col :span="4"></el-col>
            
            <el-col :span="8">
                <n-button @click.native="to_userLoginPage" quaternary ghost class = "becomeUserButtonClass" color = "black">
                    用户登录
                </n-button>
                <n-button @click.native="to_storeLoginPage" quaternary ghost class = "becomeStoreButtonClass" color = "black">
                    商家登录
                </n-button>
                <n-button @click.native="to_managerLoginPage" quaternary ghost class = "managerButtonClass" color = "black">
                    管理员登录
                </n-button>
            </el-col>
          </el-row>

        </el-header>
        <el-main>
          <el-row 
          style = "background-color:   #fdf9e7;
                  height: 455px;
                  margin-bottom: 0px;
                  margin-top: 0px;"
          >
            <intro/>
          </el-row>
            <cards/>
        </el-main>
      </el-container>
    </div>
    
</template>
  
  
<script>
  
  import cards from '../firstPage/cards.vue'
  import intro from '../firstPage/intro.vue'
  import { defineComponent ,ref } from 'vue'
  import { NTag,NButton} from 'naive-ui'
  
  export default defineComponent({
    name: 'firstPage',
    components: {
      cards,
      intro,
      NTag,
      NButton,
    },
    methods: {
      to_userLoginPage(){
        this.$router.push({path: '/userLoginPage'})
      },
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
  .el-header {
    background-color:white;
    border-radius: 10px;
  }
  
  .el-main {
    height: 870px;
    border-radius: 20px;
    padding-left: 0px;
    padding-right: 0px;
    padding-bottom: 0px;
    padding-top: 0px;
  }
  
</style>
  