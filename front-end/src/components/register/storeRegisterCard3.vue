<template>
    <el-card class="storeRegisterBoxCard">
      <el-form 
        :model="form"
        :rules="rules"
        ref="form"
        class="storeRegisterForm" 
      >
        <h3 class = "storeRegisterTitle">
          商家入驻
        </h3>
        <el-form-item class = "storeStepItem">
          <el-steps :active="2" finish-status="success" class = "storeStep"  align-center>
            <el-step title="注册商家账号" />
            <el-step title="填写店铺信息" />
            <el-step title="等待管理员审核" />
          </el-steps>
    
        </el-form-item>
  
  
        <el-form-item class = "storeRegisterMainItem">
          <storeRegisterMain3/>
  
        </el-form-item>
  
      </el-form>

    </el-card>
  
      
  </template>
    
  <script>
    
    import storeRegisterMain3 from './storeRegisterMain3.vue'
    
  
    export default {
      name: 'storeRegisterCard3',
      components: {
        storeRegisterMain3,
      }
    }
    
  </script>
  
  <style>
  .storeRegisterBoxCard {
    margin:auto;
    width: 1000px;
    height: 550px;
    padding-left: 0px;
    padding-top:0px;
  }
  
  .storeRegisterForm {
    height: 500px;
    margin: top 0%;
    margin: bottom 0%;
    margin: left 0%;
    margin: right 0%;
    width: 100%;
  }
  
  .storeRegisterTitle {
    text-align: center;
    color :black;
    font-size: 35px;   
    margin: 0px 0px 0px 0px;
  }
  
  
  .storeStep {
    width: 80%;
    margin-left: 10%;
  }
  
  .storeRegisterMainItem {
    margin: auto;
  }
  
  
  
  </style>
  
  
    