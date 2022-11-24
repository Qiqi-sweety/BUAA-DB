<!-- storeRegisterPage的子组件一:
  下属组件storeRegisterLeft1负责获得商家注册的店铺名和密码部分-->


<template>
  <el-card class="storeRegisterBoxCard">

    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="storeRegisterForm" 
    >
      <h3 
      style = "text-align: center;
              color :black;
              font-size: 35px;   
              margin: 0 0 0 0;"
      >
        商家入驻
      </h3>
      <el-form-item>
        <el-steps :active="0" finish-status="success" 
        style = "width: 80%;
        margin-left: 10%;" align-center>
          <el-step title="注册商家账号" />
          <el-step title="填写店铺信息" />
          <el-step title="等待管理员审核" />
        </el-steps>
  
      </el-form-item>


      <el-form-item class = "storeRegisterMainItem">
        <el-row 
        style = "margin-right: 0;
                width:100%;">
          <el-col :span="12" class = "storeRegisterFormCol">


            <storeRegisterLeft1 style = "margin:auto;"/>
          </el-col>
    
    
          <el-col :span="12" class = "storeRegisterImageFormCol">
            <img alt="storeRegisterLogo" src="../../assets/storeLogo.svg" >
          </el-col>
    
    
        </el-row>

      </el-form-item>

    </el-form>


  </el-card>

    
</template>
  
<script>
  
  import storeRegisterLeft1 from './storeRegisterLeft1.vue'
  

  export default {
    name: 'storeRegisterCard1',
    components: {
      storeRegisterLeft1,
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


  