<!-- storeRegisterPage的组件三:等待申请-->

<template>
    <el-card class="storeRegisterBoxCard">
      <el-form
        class="storeRegisterForm" 
      >
        <h3 
        style = "text-align: center;
              color :black;
              font-size: 35px;   
              margin: 0px 0px 0px 0px;"
        >
          商家入驻
        </h3>
        <el-form-item>
          <el-steps :active="2" finish-status="success" 
          style = "width: 80%;
  margin-left: 10%;" align-center>
            <el-step title="注册商家账号" />
            <el-step title="填写店铺信息" />
            <el-step title="等待管理员审核" />
          </el-steps>
    
        </el-form-item>
  
  
        <el-form-item class = "storeRegisterMainItem">

          <el-form style = "margin-right: 0; width:100%; height: 100px;">
            <el-form-item style = "margin-left: 45%; margin-bottom: 0; height: 40px;">
              <el-icon color="green" size = "large"><SuccessFilled /></el-icon>
              <h3>提交成功！</h3>
            </el-form-item>

            <p style = "text-align: center;
                        margin-top: 0;
                        font-weight: bold;
                        color :#606266;">
            请耐心等待审核消息
            </p>

            <el-form-item style = "margin-left:37%;">
              <img alt="storeWaitingLogo" src="../../assets/waitingLogo.svg" 
              style = "height: 250px;
                      width: 250px;">
            </el-form-item>
        
            <el-form-item 
            style = "width: 300px;
                    margin: 0 0 0 350px;
                    padding: 0 0 0 35px;">
              <el-row class = "row">
              <el-col :span="12">  
                  <el-link :underline="false" @click.native="to_storeLoginPage">
                  登录账号
                </el-link>
                </el-col>
              <el-col :span="12">
                <el-link :underline="false"  @click.native="to_firstPage">
                  返回首页
                </el-link>
              </el-col>
            </el-row>
                
            </el-form-item>
          </el-form>
          <!-- <storeRegisterMain3/> -->
        </el-form-item>
  
      </el-form>

    </el-card>
  
      
  </template>
    
  <script>
    export default {
      name: 'storeRegisterCard3',
      components: {
      },
      methods: {
        to_storeLoginPage(){
          this.$router.push({path: '/storeLoginPage'})
        },
        to_firstPage(){
          this.$router.push({path: '/'})
        }
      }
    }
    
  </script>
  
  <style>
  .storeRegisterBoxCard {
    margin:auto;
    width: 1000px;
    height: 550px;
    padding-left: 0;
    padding-top: 0;
  }
  
  .storeRegisterForm {
    height: 500px;
    margin: 0 0 0 0;
    width: 100%;
  }
  
  .storeRegisterMainItem {
    margin: auto;
  }
  
  
  
  </style>
  
  
    