<!-- 管理员主页 -->

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
            default-active="1"
            text-color="#fff"
            >
                
            <el-menu-item index="1" @click.native="sub_verifySheet">
                <el-icon><CircleCheck /></el-icon>
                <span>商家审核</span>
            </el-menu-item>

            <el-menu-item index="2" @click.native="sub_infoSheet">
                <el-icon><Document /></el-icon>
                <span>查看信息</span>
            </el-menu-item>

            <el-menu-item index="3" @click.native="sub_dataSheet">
                <template #title>
                    <el-icon><DataAnalysis /></el-icon>
                    <span>数据统计</span>
                </template>
            </el-menu-item>

                
      </el-menu>
            
        
          </el-aside>

          <el-main>
            <router-view></router-view>
<!--            <infoSheet/>-->
<!--            <verifySheet/>-->
          </el-main>

        </el-container>
      </el-container>
    </div>
</template>

<script>
  import { defineComponent } from 'vue'
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
      },
      sub_verifySheet(){
        this.$router.push({path: '/managerMainPage/verify'})
      },
      sub_infoSheet(){
        this.$router.push({path: '/managerMainPage/info'})
      },
      sub_dataSheet(){
        this.$router.push({path: '/managerMainPage/data'})
      }
    }
  })
</script>

<style>

    .el-menu-vertical-demo {
        width: 200px;
    }
</style>