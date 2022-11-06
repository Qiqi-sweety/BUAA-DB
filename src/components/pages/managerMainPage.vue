<!-- 管理员主页 -->

<!-- TODO:
√1.Header中用户登录按钮跳转到userLoginPage，商家登录按钮跳转到storeLoginPage，退出登录跳转到FisrtPage

2.根据左侧导航栏的按钮进行子组件的切换：
    初始化为verifySheet
    商家审核切换到verifySheet，
    数据统计暂无，
    查看信息切换到infoSheet
 -->

<template>
    <div class="managerMainLayout">
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
            <el-col :span="4"></el-col>           
            <el-col :span="8">
                <n-button @click.native="to_userLoginPage" quaternary ghost class = "becomeUserButtonClass" color = "black">
                    用户登录
                </n-button>
                <n-button @click.native="to_storeLoginPage" quaternary ghost class = "becomeStoreButtonClass" color = "black">
                    商家登录
                </n-button>
                <n-button @click.native="to_firstPage" quaternary ghost class = "logoutButtonClass" color = "black">
                    退出登录
                </n-button>
            </el-col>
          </el-row>
        </el-header>
        <el-container>
          <el-aside width="200px" style="background-color : #545c64;">
            
            <el-menu
            active-text-color="#ffd04b"
            background-color="#545c64"
            class="el-menu-vertical-demo"
            default-active="2"
            text-color="#fff"
            >
                
            <el-menu-item index="1">
                <el-icon><CircleCheck /></el-icon>
                <span>商家审核</span>
            </el-menu-item>

            <el-menu-item index="2">
                <el-icon><Document /></el-icon>
                <span>查看信息</span>
            </el-menu-item>

            <el-sub-menu index="3">
                <template #title>
                    <el-icon><DataAnalysis /></el-icon>
                    <span>数据统计</span>
                </template>
                <el-menu-item index="1-1">item one</el-menu-item>
                <el-menu-item index="1-2">item two</el-menu-item>
                <el-menu-item index="1-3">item three</el-menu-item>
                   
            </el-sub-menu>

                
      </el-menu>
            
        
          </el-aside>

          <el-main>
            <infoSheet/>
            <verifySheet/>
            
          </el-main>

        </el-container>
      </el-container>
    </div>
</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import { NTag,NButton} from 'naive-ui'
  import infoSheet from '../managerMain/infoSheet.vue'
  import verifySheet from '../managerMain/verifySheet.vue'
  
  export default defineComponent({
    name: 'managerMainPage',
    components: {
      NTag,
      NButton,
      infoSheet,
      verifySheet,
    },
    methods: {
      to_userLoginPage(){
        this.$router.push({path: '/userLoginPage'})
      },
      to_storeLoginPage(){
        this.$router.push({path: '/storeLoginPage'})
      },
      to_firstPage(){
        this.$router.push({path: '/'})
      }
    }
  })
</script>

<style>

    .el-menu-vertical-demo {
        width: 200px;
    }
</style>