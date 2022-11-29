<!-- storeRegisterPage的组件二:获得商家注册的店铺地址，店铺介绍，店铺头像，营业执照等信息-->
<!-- 包含子组件storeRegisterMain2 -->


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
          <el-steps :active="1" finish-status="success" 
          style = "width: 80%;
          margin-left: 10%;" align-center>
            <el-step title="注册商家账号" />
            <el-step title="填写店铺信息" />
            <el-step title="等待管理员审核" />
          </el-steps>
    
        </el-form-item>
  
  
        <el-form-item class = "storeRegisterMainItem">
<!--          {{name}}{{password}}-->
          <storeRegisterMain2 :name="name" :pw="password"/>
  
        </el-form-item>
  
      </el-form>
  
    </el-card>
  </template>
    
  <script>
    import storeRegisterMain2 from './storeRegisterMain2.vue'
    import {useRouter} from "vue-router";
    const router = useRouter()

    export default {
      name: 'storeRegisterCard2',
      components: {
        storeRegisterMain2,
      },
      props: {
        name: {type: String, required: true},
        password: {type: String, required: true},
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
  
  
    