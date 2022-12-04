<!-- 用户主页——可以按照商品和店铺搜索 -->
<!-- 子组件：userSearchResForm和userMainForm -->

<template>
    <div class="mainLayout">
      <el-container>
        <el-header style = "height: 60px;background-color: white;">
          <el-row>
            <el-col :span="4">
                <!-- <img alt="Logo" src="../../assets/logo.png" class = "topLogoClass">  -->
                
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
        <el-main style = "height: 870px;">
          <div class = "mainClass">
            <!-- 搜索栏 -->
              <el-row style = "height: 100px;width: 80%;margin-left: 13%;">
                <el-col :span="5">
                  
                  <img alt="Logo" src="../../assets/logo.png"
                  style = "margin-left : 100px;
                          margin-right: auto;
                          width: 95px;
                          height: 95px;
                          background-color: white;
                          border-radius: 20px;"> 
                </el-col>
                <el-col :span="15" style = "padding-top : 30px;height: 100%;">
                  <div>
                    <el-input
                      v-model="search.key"
                      placeholder="请输入"
                      size = "large"
                      clearable
                    >
                      <template #prepend>
                        <el-select v-model="search.label" placeholder="请选择" size="large" style="width: 115px">
                          <el-option v-for="item in typeList" :key="item.id" :label="item.title" :value="item.title">{{item.title}}</el-option>
<!--                          <el-option :label="店铺" :value="1" />-->
<!--                          <el-option :label="商品" :value="2" />-->
                        </el-select>
                      </template>
                      <template #append>
                        <el-button class = "searchButton" @click="act_search">
                            <el-icon>
                                <Search/>
                            </el-icon>
                        </el-button>
                      </template>
                    </el-input>
                  </div>
                
                </el-col>
                <el-col :span="4">
              
                </el-col>

            </el-row>
            <router-view></router-view>
            <!-- 轮播展示图 and 猜你喜欢推荐 -->
<!--            <user-main-form/>-->
            <!-- 搜索结果 -->
<!--            <UserSearchResForm/>-->
          </div>
        </el-main>
      </el-container>
    </div>
  </template>
    
  <script>
    import userMainForm from '../userMain/userMainForm.vue'
    import userSearchResForm from '../userMain/userSearchResForm.vue'
    import { defineComponent, ref } from 'vue'
    import { NTag,NButton} from 'naive-ui'
    
    export default defineComponent({
      name: 'userMainPage',
      components: {
        userMainForm,
        userSearchResForm,
        NButton,
        NTag
      },
      data() {
        return {
          typeList: [{id: 1, title: '店铺'}, {id: 2, title: '商品'}],
          search: {label: '店铺', key: ''}
        }
      },
      methods: {
        to_personalCenterPage(){
          this.$router.push({path: '/personalCenterPage'})
        },
        to_storeLoginPage(){
          this.$router.push({path: '/storeLoginPage'})
        },
        to_managerLoginPage(){
          this.$router.push({path: '/managerLoginPage'})
        },
        to_firstPage(){
          this.$router.push({path: '/'})
        },
        act_search(){
          this.$router.push({
            name: 'userSearchResForm',
            query: {key: this.search.key, label: this.search.label}
          })
        }
      }
    })
</script>
    
  <style>
    /*.el-header {*/
    /*  !* background-color: #f4d870; *!*/
    /*  height: 60px;*/
    /*  background-color: white;*/
    /*}*/
    
    /*.el-main {*/
    /*  height: 870px;*/
    /*}*/

    
  </style>