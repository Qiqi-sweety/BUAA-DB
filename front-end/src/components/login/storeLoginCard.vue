<template>
  <el-card class="storeBoxCard">
    <el-row class = "storeLoginRow">
      <el-col :span="12" class = "storeLoginFormCol">
         <storeLoginForm class = "storeLoginFormClass"/>
      </el-col>

      <el-col :span="12" class = "storeLoginImageFormCol">
        <storeLoginImageForm class = "storeLoginImageFormClass"/>
      </el-col>

    </el-row>
  </el-card>
</template>

<script>
import storeLoginForm from './storeLoginForm.vue'
import storeLoginImageForm from './storeLoginImageForm.vue'
export default {
  name: 'storeLoginCard',
  components: {
    storeLoginForm,  
    storeLoginImageForm,
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

.storeLoginRow {
  padding-top: 0px;
}

.storeBoxCard {
  margin:auto;
  width: 1000px;
  height: 550px;
  padding-left: 0px;
  padding-top:0px;
}

.storeLoginFormCol {
  height: 510px;
  padding-top: 25px;

  
}

.storeLoginImageFormCol {
  padding-top: 25px;
  padding-left: 35px;
  height: 510px;
}



.storeLoginFormClass {
  margin:auto;
  
}

.storeLoginImageFormClass {
 
  border-radius: 20px;
  margin-top:0px;
}

</style>