<!-- 用户个人中心页面 -->

<!-- TODO:
1.Header中返回主页按钮跳转到userMainPage，商家登录按钮跳转到storeLoginPage，管理员登录按钮跳转到managerLoginPage，退出登录跳转到FisrtPage

2.根据左侧导航栏的按钮进行子组件的切换：
    初始化为orderSheet，
    我的订单按钮切换到orderSheet，
    我的评价按钮切换到evaluateSheet，
    数据分析暂无，
    账号管理按钮切换到userManageSheet -->

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
                <n-button quaternary ghost class = "mainPageButtonClass" color = "black">
                    返回主页
                </n-button>
                <n-button quaternary ghost class = "becomeStoretButtonClass" color = "black">
                    商家登录
                </n-button>
                <n-button quaternary ghost class = "managerButtonClass" color = "black">
                    管理员登录
                </n-button>
                <n-button quaternary ghost class = "logoutButtonClass" color = "black">
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
            default-active="2"
            text-color="#fff"
            >
                <el-menu-item index="1">
                    <el-icon><Sell /></el-icon>
                    <span>我的订单</span>
                </el-menu-item>

                <el-menu-item index="2">
                    <el-icon><Star /></el-icon>
                    <span>我的评价</span>
                </el-menu-item>

                <el-menu-item index="3">
                    <el-icon><DataAnalysis /></el-icon>
                    <span>数据统计</span>
                </el-menu-item>

                <el-menu-item index="4">
                    <el-icon><setting /></el-icon>
                    <span>账号管理</span>
                </el-menu-item>

                
      </el-menu>
        
          </el-aside>

          <el-main>
            <orderSheet/>
            <evaluateSheet/>
            <userManageSheet/>
          </el-main>

        </el-container>
      </el-container>
    </div>
</template>

<script>
  import { defineComponent ,ref } from 'vue'
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
        margin-right: 0%;
    }

    .becomeStoreButtonClass {
        margin-top: 20px;
    }

    .managerButtonClass {
        margin-top: 20px;
    }

    .mainPageButtonClass {
        margin-top: 20px;
        margin-left: 200px;
    }

    .orderSheetRowClass {
        margin-left:30px;
    }


</style>