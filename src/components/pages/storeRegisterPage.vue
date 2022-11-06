<!-- 商家注册页面 -->

<!-- TODO:
header的用户登录跳转到userLoginPage，管理员登录跳转到managerLoginPage

本页面有三种状态：storeRegisterCard1，storeRegisterCard2，storeRegisterCard3，需要根据这三个组件里面的反馈切换这三个组件。
实现商家的注册。 -->


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
                <div class="grid-content ep-bg-purple" />
                
            </el-col>
            <el-col :span="9"><div class="grid-content ep-bg-purple-light" /></el-col>
            
            <el-col :span="3">

                <n-button quaternary ghost class = "managerButtonClass" color = "black">
                    用户登录
                </n-button>

                <n-button quaternary ghost class = "logoutButtonClass" color = "black">
                    管理员登录
                </n-button>
            </el-col>
          </el-row> 
        </el-header>
        <el-main>
          <div style = "margin-top: 5%;">
            <storeRegisterCard1/>
            <storeRegisterCard2/>
            <StoreRegisterCard3/>
          </div>
        </el-main>
      </el-container>
    </div>
    
</template>
  
<script>
  import storeRegisterCard1 from '../register/storeRegisterCard1.vue'
  import storeRegisterCard2 from '../register/storeRegisterCard2.vue'
  import storeRegisterCard3 from '../register/storeRegisterCard3.vue'
  import { defineComponent ,ref } from 'vue'
  import { NTag,NButton} from 'naive-ui'

  export default defineComponent({
    name: 'registerPage',
    components: {
    storeRegisterCard1,
    storeRegisterCard2,
    storeRegisterCard3,
    NTag,
    NButton,
}
  })
</script>
  
<style>
  .el-header {
    height: 60px;
    background-color: white;
  }
  
  .el-main {
    height: 870px;
  }
</style>
  