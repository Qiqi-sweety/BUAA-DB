<template>
  <el-card class="businessBoxCard">
    <el-row class = "businessLoginRow">
      <el-col :span="12" class = "businessLoginFormCol">
         <businessLoginForm class = "businessLoginFormClass"/>
      </el-col>

      <el-col :span="12" class = "businessLoginImageFormCol">
        <businessLoginImageForm class = "businessLoginImageFormClass"/>
      </el-col>


    </el-row>
  </el-card>
</template>

<script>
import businessLoginForm from './businessLoginForm.vue'
import businessLoginImageForm from './businessLoginImageForm.vue'
export default {
  name: 'loginCard',
  components: {
    businessLoginForm,  
    businessLoginImageForm,
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

.businessLoginRow {
  padding-top: 0px;
}

.businessBoxCard {
  margin:auto;
  width: 1000px;
  height: 550px;
  padding-left: 0px;
  padding-top:0px;
}

.businessLoginFormCol {
  height: 510px;
  padding-top: 25px;

  
}

.businessLoginImageFormCol {
  padding-top: 25px;
  padding-left: 35px;
  height: 510px;
}



.businessLoginFormClass {
  margin:auto;
  
}

.businessLoginImageFormClass {
 
  border-radius: 20px;
  margin-top:0px;
}

</style>