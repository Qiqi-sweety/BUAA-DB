<!-- 用户个人中心页面 -->

<template>
    <div class="personalCenterLayout">
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
            <el-col :span="4">
            </el-col>
            
            <el-col :span="8">
                <n-button @click.native="to_userMainPage" quaternary ghost class = "mainPageButtonClass" color = "black">
                    返回主页
                </n-button>
                <n-button @click.native="to_storeLoginPage" quaternary ghost class = "becomeStoreButtonClass" color = "black">
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
        <el-container>
          <el-aside width="200px" style="background-color : #545c64;" class = "AsideClass">
            
            <el-menu
            active-text-color="#ffd04b"
            background-color="#545c64"
            class="el-menu-vertical-demo"
            default-active="1"
            text-color="#fff"
            >
                <el-menu-item index="1" @click.native="sub_orderSheet">
                    <el-icon><Sell /></el-icon>
                    <span>我的订单</span>
                </el-menu-item>

                <el-menu-item index="2" @click.native="sub_evaluateSheet">
                    <el-icon><Star /></el-icon>
                    <span>我的评价</span>
                </el-menu-item>

                <el-menu-item index="3" @click.native="sub_dataSheet">
                    <el-icon><DataAnalysis /></el-icon>
                    <span>数据统计</span>
                </el-menu-item>

                <el-menu-item index="4" @click.native="sub_userManageSheet">
                    <el-icon><setting /></el-icon>
                    <span>账号管理</span>
                </el-menu-item>

                
      </el-menu>
        
          </el-aside>

          <el-main>
            <router-view></router-view>
<!--            <orderSheet/>-->
<!--            <evaluateSheet/>-->
<!--            <userManageSheet/>-->
          </el-main>

        </el-container>
      </el-container>
    </div>
</template>

<script>
  import { defineComponent } from 'vue'
  import { NTag,NButton} from 'naive-ui'
  import orderSheet from '../personalCenter/orderSheet.vue'
  import evaluateSheet from '../personalCenter/evaluateSheet.vue'
  import userManageSheet from '../personalCenter/userManageSheet.vue'
 

  export default defineComponent({
    components: {
      NTag,
      NButton,
      orderSheet,
      evaluateSheet,
      userManageSheet,
    },
    methods: {
      to_storeLoginPage(){
        this.$router.push({path: '/storeLoginPage'})
      },
      to_managerLoginPage(){
        this.$router.push({path: '/managerLoginPage'})
      },
      to_userMainPage(){
        this.$router.push({path: '/userMainPage'})
      },
      to_firstPage(){
        this.$router.push({path: '/'})
      },
      sub_orderSheet(){
        this.$router.push({path: '/personalCenterPage/order'})
      },
      sub_evaluateSheet(){
        this.$router.push({path: '/personalCenterPage/comment'})
      },
      sub_dataSheet(){
        this.$router.push({path: '/personalCenterPage/data'})
      },
      sub_userManageSheet(){
        this.$router.push({path: '/personalCenterPage/userManage'})
      }
    }
  })
  </script>


<style>
    .el-menu-vertical-demo {
        width: 200px;
    }

    .topLogoClass {
        width: 55px;
        height: 55px;
        margin-left: 30px;
    }

    .locationTagClass {
        margin-top: 20px;
    }

    .logoutButtonClass {
        margin-top: 20px;
        margin-right: 0;
    }

    .becomeStoreButtonClass {
        margin-top: 20px;
    }

    .managerButtonClass {
        margin-top: 20px;
    }

    .mainPageButtonClass {
        margin-top: 20px;
        margin-left: 150px;
    }

    /*.orderSheetRowClass {*/
    /*    margin-left:30px;*/
    /*}*/


</style>