<!-- 用户进入特定商家的点餐页面：不同商家有不同点餐界面 -->

<template>
    <div class="userOrderPageLayout">
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
            <el-col :span="4"><div class="grid-content ep-bg-purple-light" /></el-col>
            
            <el-col :span="8">
                <n-button @click.native="to_personalCenterPage" quaternary ghost class = "mainPageButtonClass" color = "black">
                    个人中心
                </n-button>
                <n-button @click.native="to_storeLoginPage" quaternary ghost class = "becomeStoretButtonClass" color = "black">
                    商家登录
                </n-button>
                <n-button @click.native="to_managerLoginPage" quaternary ghost class = "managerButtonClass" color = "black">
                    管理员登录
                </n-button>
                <n-button @click.native="to_firstPage" quaternary ghost class = "logoutButtonClass" color = "black">
                    退出登录
                </n-button>
            </el-col>
          </el-row>          
        </el-header>
        <el-main>

          <!-- 顶部菜单栏加上购物车功能 -->
          <NMessageProvider>
            <order-tabs :store_id="this.$route.query.store_id"></order-tabs>
          </NMessageProvider>

          <router-view></router-view>
          <!-- 主体部分：按照orderTab的信号进行切换 -->
<!--            <homePageCard/>-->
<!--            <menuPageCard/>-->
<!--            <evaluatePageCard/>-->
<!--            <resultPageCard/>-->
        </el-main>
      </el-container>
    </div>
    
</template>
  
  
<script>
  
  import orderTabs from '../orderPage/orderTabs.vue';
  import { defineComponent } from 'vue'
  import { NTag,NButton,NMessageProvider} from 'naive-ui'

  import menuPageCard from "../orderPage/menuPageCard.vue"
  import homePageCard from "../orderPage/homePageCard.vue"
  import evaluatePageCard from "../orderPage/evaluatePageCard.vue"
  import resultPageCard from "../orderPage/resultPageCard.vue"
  
  export default defineComponent({
    name: 'orderPage',
    components: {
      orderTabs,
      NTag,
      NButton,
      NMessageProvider,
      menuPageCard,
      homePageCard,
      evaluatePageCard,
      resultPageCard,
    },
    methods: {
      to_personalCenterPage() {
        this.$router.push({path: '/personalCenterPage'})
      },
      to_storeLoginPage() {
        this.$router.push({path: '/storeLoginPage'})
      },
      to_managerLoginPage() {
        this.$router.push({path: '/managerLoginPage'})
      },
      to_firstPage() {
        this.$router.push({path: '/'})
      },
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
    padding: 0;
  }
  

  
</style>
  