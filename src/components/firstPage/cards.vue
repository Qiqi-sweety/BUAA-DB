<!-- firstPage的一部分——下方的展示卡 -->

<template>
  <el-carousel :interval="4000" type="card" height="380px" class = "cardsClass">
    <el-carousel-item  class = "userCardItem" key = 1 shadow="always">
      <el-card class="userCardClass">
        <el-row class = "userCardRow">
          <el-col :span="12" class = "userForm1Col">
            <img alt="loginLogo" src="../../assets/userLogo.svg" class = "logo" >
            <p class = "details">
            吃饱了才有力气减肥！
            </p>
          </el-col>
          <el-col :span="6" >
            <h3 
            style = "width: 30px;
                    font-size: 30px;
                    font-weight: bold;
                    color: black;
                    margin-top: 40px;  
                    margin-left:50px;">
                我要点餐
            </h3>
          </el-col>
          <el-col :span = "6" >
            <n-button @click.native="to_userLoginPage" round type="warning" class = "startButtonClass">
              开始
            </n-button>
          </el-col>
        </el-row>
      </el-card>
    </el-carousel-item>

     
    <el-carousel-item class = "managerCardItem" key = 2 shadow="always">
      <el-card class="managerCardClass">
        <el-row class = "managerCardRow">
          <el-col :span="12">
            <img alt="loginLogo" src="../../assets/managerLogo.svg" class = "logo" >
            <p class = "details">
            专业管理为你保驾护航！
            </p>
          </el-col>
          <el-col :span="6" >
            <h3 
            style = "width: 30px;
                    font-size: 30px;
                    font-weight: bold;
                    color: black;
                    margin-top: 40px;  
                    margin-left:50px;">
                我是管理员
            </h3>
          </el-col>
          <el-col :span = "6" >
            <n-button @click.native="to_managerLoginPage" round type="warning" class = "startButtonClass">
              开始
            </n-button>
          </el-col>
          
        </el-row>
      </el-card>
    </el-carousel-item>


    <el-carousel-item class = "storeCardItem" key = 3 shadow="always">
      <el-card>
        <el-row class = "storeCardRow">
          <el-col :span="12">
            <img alt="loginLogo" src="../../assets/storeLogo.svg" class = "logo" >
            <p class = "details">
            连接千家万户的美食！
            </p>
          </el-col>

          <el-col :span="6" >
            <h3 
            style = "width: 30px;
                    font-size: 30px;
                    font-weight: bold;
                    color: black;
                    margin-top: 40px;  
                    margin-left:50px;"
            >
                我是商家
            </h3>
          </el-col>
          <el-col :span = "6" >
            <n-button @click.native="to_storeLoginPage" round type="warning" class = "startButtonClass">
              开始
            </n-button>
          </el-col>
          
        </el-row>
      </el-card>
    </el-carousel-item>


  </el-carousel>
</template>

<script>
import { defineComponent ,ref } from 'vue'
import {NButton} from 'naive-ui'



export default defineComponent({
  name: 'cards',
  components: {
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

.cardsClass {
  background-color: #f8d76c;
  border-radius: 20px;
}

.el-carousel__item:nth-child(2n){
  background-color:   #fdf9e7;
  border-radius: 20px;
  width: 660px;
  height: 330px;
  margin-left: 90px;
  margin-top:30px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.07), 
                0 2px 4px rgba(0,0,0,0.07), 
                0 4px 8px rgba(0,0,0,0.07), 
                0 8px 16px rgba(0,0,0,0.07),
                0 16px 32px rgba(0,0,0,0.07), 
                0 32px 64px rgba(0,0,0,0.07);
  
}

.el-carousel__item:nth-child(2n + 1) {
  /* background-color: white; */
  background-color:   #fdf9e7;
  border-radius: 20px;
  width: 660px;
  height: 330px;
  margin-left: 90px;
  margin-top:30px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.07), 
                0 2px 4px rgba(0,0,0,0.07), 
                0 4px 8px rgba(0,0,0,0.07), 
                0 8px 16px rgba(0,0,0,0.07),
                0 16px 32px rgba(0,0,0,0.07), 
                0 32px 64px rgba(0,0,0,0.07);
  
}


.startButtonClass {
  width: 100px;
  height: 100px;
  font-size: 30px;
  margin-top: 90px;
  margin-left :30px;
}

.details {
    margin-top: 0px;
    padding: 0px;
    color :#606266;
    font-family: "微软雅黑";
    font-weight:bold;
    font-size: 18px;
    margin-left: 50px;
}

.logo{
  width: 260px;
  height: 260px;
}


</style>
