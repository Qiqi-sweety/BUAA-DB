<template>
  <el-card class="businessBoxCard">
    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="businessRegisterForm" 
    >
      <h3 class = "businessRegisterTitle">
        商家入驻
      </h3>


      <el-form-item class = "businessStepItem">
        <el-steps :active="active" finish-status="success" class = "businessStep"  align-center>
          <el-step title="注册商家账号" />
          <el-step title="填写店铺信息" />
          <el-step title="等待管理员审核" />
        </el-steps>
  
      </el-form-item>




      <el-form-item class = "businessRegisterMain1">

        
        <!-- <business-register-main-1/> -->
        <business-register-main-2/>
        <!-- <business-register-main-3/> -->


      </el-form-item>

    </el-form>


    
  
  </el-card>

    
</template>
  
<script>
  
  import businessRegisterMain1 from './businessRegisterMain1.vue'
  import businessRegisterMain2 from './businessRegisterMain2.vue'
  import businessRegisterMain3 from './businessRegisterMain3.vue'
  

  export default {
    name: 'customerRegisterCard',
    components: {
      businessRegisterMain1,
      businessRegisterMain2,
      businessRegisterMain3,
    }
  }
  
</script>

<style>
.businessBoxCard {
  margin:auto;
  width: 1000px;
  height: 550px;
  padding-left: 0px;
  padding-top:0px;
}

.businessRegisterForm {
  height: 500px;
  margin: top 0%;
  margin: bottom 0%;
  margin: left 0%;
  margin: right 0%;
  width: 100%;
}

.businessRegisterTitle {
  text-align: center;
  color :black;
  font-size: 35px;   
  margin: 0px 0px 0px 0px;
}


.businessStep {
  width: 80%;
  margin-left: 10%;
}

.businessRegisterMain1 {
  margin: auto;
}



</style>


  