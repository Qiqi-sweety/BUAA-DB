<template>
  <el-card class="customerBoxCard">
    
    
    <el-row class = "customerLoginRow">
      <el-col :span="12" class = "customerLoginFormCol">
         <customerLoginForm class = "customerLoginFormClass"/>
      </el-col>


      <el-col :span="12" class = "customerLoginImageFormCol">
        <customerLoginImageForm class = "customerLoginImageFormClass"/>
      </el-col>


    </el-row>
  </el-card>
</template>

<script>
import customerLoginForm from './customerLoginForm.vue'
import customerLoginImageForm from './customerLoginImageForm.vue'
export default {
  name: 'loginCard',
  components: {
    customerLoginForm,  
    customerLoginImageForm,
  }
}
</script>



<style>
.text {
  font-size: 14px;
}

.item {
  padding: 0px;
  margin-bottom: 18px;
}

.customerLoginRow {
  padding-top: 0px;
}

.customerBoxCard {
  margin:auto;
  width: 1000px;
  height: 550px;
  padding-left: 0px;
  padding-top:0px;
}

.customerLoginFormCol {
  height: 510px;
  padding-top: 25px;

  
}

.customerLoginImageFormCol {
  padding-top: 25px;
  padding-left: 35px;
  height: 510px;
}



.customerLoginFormClass {
  margin:auto;
  
}

.customerLoginImageFormClass {
 
  border-radius: 20px;
  margin-top:0px;
}

</style>