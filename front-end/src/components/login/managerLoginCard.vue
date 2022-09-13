<template>
  <el-card class="managerBoxCard">
    
    
    <el-row class = "managerLoginRow">
      <el-col :span="12" class = "managerLoginFormCol">
         <managerLoginForm class = "managerLoginFormClass"/>
      </el-col>


      <el-col :span="12" class = "managerLoginImageFormCol">
        <managerLoginImageForm class = "managerLoginImageFormClass"/>
      </el-col>


    </el-row>
  </el-card>
</template>

<script>
import managerLoginForm from './managerLoginForm.vue'
import managerLoginImageForm from './managerLoginImageForm.vue'
export default {
  name: 'managerLoginCard',
  components: {
    managerLoginForm,  
    managerLoginImageForm,
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

.managerLoginRow {
  padding-top: 0px;
}

.managerBoxCard {
  margin:auto;
  width: 1000px;
  height: 550px;
  padding-left: 0px;
  padding-top:0px;
}

.managerLoginFormCol {
  height: 510px;
  padding-top: 25px;

  
}

.managerLoginImageFormCol {
  padding-top: 25px;
  padding-left: 35px;
  height: 510px;
}



.managerLoginFormClass {
  margin:auto;
  
}

.managerLoginImageFormClass {
 
  border-radius: 20px;
  margin-top:0px;
}

</style>