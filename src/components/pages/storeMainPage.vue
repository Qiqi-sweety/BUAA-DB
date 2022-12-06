<!-- 商家主页 -->

<template>
    <div class="storeMainLayout">
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
            <el-col :span="4"><div class="grid-content ep-bg-purple-light" /></el-col>
            
            <el-col :span="8">
                <n-button @click.native="to_userLoginPage" quaternary ghost class = "becomeUserButtonClass" color = "black">
                    用户登录
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
        <el-container>
          <el-aside width="200px" class = "AsideClass" style="background-color : #545c64;">
            <el-menu
            active-text-color="#ffd04b"
            background-color="#545c64"
            class="el-menu-vertical-demo"
            default-active="1"
            text-color="#fff"
            >
                <el-menu-item index="1" @click.native="sub_storeInfoSheet">
                    <el-icon><House /></el-icon>
                    <span>店铺信息</span>
                </el-menu-item>

                <el-sub-menu index="2" @click.native="sub_dataSheet">
                    <template #title>
                        <el-icon><DataAnalysis /></el-icon>
                        <span>数据统计</span>
                    </template>
                    <el-menu-item index="1-1">item one</el-menu-item>
                    <el-menu-item index="1-2">item two</el-menu-item>
                    <el-menu-item index="1-3">item three</el-menu-item>
                   
                </el-sub-menu>

                <el-menu-item index="3" @click.native="sub_foodManageSheet">
                    <el-icon><Dish /></el-icon>
                    <span>商品管理</span>
                </el-menu-item>

                <el-menu-item index="4" @click.native="sub_orderManageSheet">
                    <el-icon><Sell /></el-icon>
                    <span>订单管理</span>
                </el-menu-item>

                <el-menu-item index="5" @click.native="sub_userEvaluateSheet">
                    <el-icon><Star /></el-icon>
                    <span>用户评价</span>
                </el-menu-item>

                <el-menu-item index="6" @click.native="sub_storeIdManageSheet">
                    <el-icon><setting /></el-icon>
                    <span>账号管理</span>
                </el-menu-item>

            </el-menu>
        
          </el-aside>

          <el-main>
            <NMessageProvider>
              <router-view></router-view>
<!--                <storeInfoSheet/> -->
<!--                <foodManageSheet/>-->
<!--                <orderManageSheet/>-->
<!--                <userEvaluateSheet/>-->
<!--                <storeIdManageSheet/>-->
            </NMessageProvider>

            
            
          </el-main>

        </el-container>
      </el-container>
    </div>
</template>

<script>
  
  
  import { defineComponent } from 'vue'
  import { NTag,NButton,NMessageProvider} from 'naive-ui'
  import storeInfoSheet from '../storeMain/storeInfoSheet.vue'
  import foodManageSheet from '../storeMain/foodManageSheet.vue'
  import orderManageSheet from '../storeMain/orderManageSheet.vue'
  import userEvaluateSheet from '../storeMain/userEvaluateSheet.vue'
  import storeIdManageSheet from '../storeMain/storeIdManageSheet.vue'
  
  export default defineComponent({
    name: 'storeMainPage',
    components: {
      NTag,
      NButton,
      NMessageProvider,
      storeInfoSheet,
      foodManageSheet,
      orderManageSheet,
      userEvaluateSheet,
      storeIdManageSheet,
    },
    methods: {
      to_userLoginPage(){
        this.$router.push({path: '/userLoginPage'})
      },
      to_managerLoginPage(){
        this.$router.push({path: '/managerLoginPage'})
      },
      to_firstPage(){
        this.$router.push({path: '/'})
      },
      sub_storeInfoSheet(){
        this.$router.push({path: '/storeMainPage/info'})
      },
      sub_dataSheet(){
        this.$router.push({path: '/storeMainPage'})
      },
      sub_foodManageSheet(){
        this.$router.push({path: '/storeMainPage/foodManage'})
      },
      sub_orderManageSheet(){
        this.$router.push({path: '/storeMainPage/orderManage'})
      },
      sub_userEvaluateSheet(){
        this.$router.push({path: '/storeMainPage/comment'})
      },
      sub_storeIdManageSheet(){
        this.$router.push({path: '/storeMainPage/idManage'})
      }
    }
  })
</script>

<style>
    .el-menu-vertical-demo {
        width :200px;
    }

    .becomeUserButtonClass {
        margin-left: 250px;
    }


</style>


