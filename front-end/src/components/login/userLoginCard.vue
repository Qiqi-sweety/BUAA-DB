<template>
  <el-card class="userLoginBoxCard">
    <el-row class = "userLoginRow">
      <el-col :span="12" class = "userLoginFormCol">
         <userLoginForm class = "userLoginFormClass"/>
      </el-col>

      <el-col :span="12" class = "userLoginImageFormCol">
        <userLoginImageForm class = "userLoginImageFormClass"/>
      </el-col>

    </el-row>
  </el-card>
</template>

<script>
import userLoginForm from './userLoginForm.vue'
import userLoginImageForm from './userLoginImageForm.vue'
export default {
  name: 'userLoginCard',
  components: {
    userLoginForm,  
    userLoginImageForm,
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

.userLoginRow {
  padding-top: 0px;
}

.userLoginBoxCard {
  margin:auto;
  width: 1000px;
  height: 550px;
  padding-left: 0px;
  padding-top:0px;
}

.userLoginFormCol {
  height: 510px;
  padding-top: 25px;

  
}

.userLoginImageFormCol {
  padding-top: 25px;
  padding-left: 35px;
  height: 510px;
}



.userLoginFormClass {
  margin:auto;
  
}

.userLoginImageFormClass {
 
  border-radius: 20px;
  margin-top:0px;
}

</style>