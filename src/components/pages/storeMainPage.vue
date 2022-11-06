<!-- 商家主页 -->

<!-- TODO:
√1.Header中用户登录按钮跳转到userLoginPage，管理员登录按钮跳转到managerLoginPage，退出登录跳转到FisrtPage

2.根据左侧导航栏的按钮进行子组件的切换：
    初始化为storeInfoSheet
    店铺信息按钮切换到storeInfoSheet，
    数据统计暂无，
    商品管理按钮切换到foodManageSheet，
    订单管理按钮切换到orderManageSheet，
    用户评价按钮切换到userEvaluateSheet，
    账号管理按钮切换到storeIdManageSheet，
 -->

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
            default-active="2"
            text-color="#fff"
            >
                <el-menu-item index="1">
                    <el-icon><House /></el-icon>
                    <span>店铺信息</span>
                </el-menu-item>

                <el-sub-menu index="2">
                    <template #title>
                        <el-icon><DataAnalysis /></el-icon>
                    <span>数据统计</span>
                    </template>
                    <el-menu-item index="1-1">item one</el-menu-item>
                    <el-menu-item index="1-2">item two</el-menu-item>
                    <el-menu-item index="1-3">item three</el-menu-item>
                   
                </el-sub-menu>

                <el-menu-item index="3">
                    <el-icon><Dish /></el-icon>
                    <span>商品管理</span>
                </el-menu-item>

                <el-menu-item index="4"> 
                    <el-icon><Sell /></el-icon>
                    <span>订单管理</span>
                </el-menu-item>

                <el-menu-item index="5">
                    <el-icon><Star /></el-icon>
                    <span>用户评价</span>
                </el-menu-item>

                <el-menu-item index="6">
                    <el-icon><setting /></el-icon>
                    <span>账号管理</span>
                </el-menu-item>

            </el-menu>
        
          </el-aside>

          <el-main>
            <NMessageProvider>
                <storeInfoSheet/> 
                <foodManageSheet/>
                <orderManageSheet/>
                <userEvaluateSheet/>
                <storeIdManageSheet/>

            </NMessageProvider>

            
            
          </el-main>

        </el-container>
      </el-container>
    </div>
</template>

<script>
  
  
  import { defineComponent ,ref } from 'vue'
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
      }
    }
  })
</script>

<style>
    .el-menu-vertical-demo {
        width :200px;
    }

    .becomeUserButtonClass {
        margin-left :250px;
    }


</style>


