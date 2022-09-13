<template>
      <el-row class = "storeRegisterRow">
        <el-col :span="12" class = "storeRegisterFormCol">
           <storeRegisterLeft1 class = "storeRegisterLeft1"/>
        </el-col>
  
  
        <el-col :span="12" class = "storeRegisterImageFormCol">
          <storeRegisterImageForm class = "storeRegisterImageFormClass"/>
        </el-col>
  
  
      </el-row>
    
  </template>
  
  <script>
  import storeRegisterLeft1 from './storeRegisterLeft1.vue'
  import storeRegisterImageForm from './storeRegisterImageForm.vue'
  export default {
    name: 'storeRegisterMain1',
    components: {
      storeRegisterLeft1,
      storeRegisterImageForm,
    }
  }
  </script>
  
  
  
  <style>
.storeRegisterRow {
    margin-right:0px;
    width:100%;
}


.storeRegisterLeft1 {
    margin:auto;
    
}

.storeRegisterImageFormClass {
    margin: auto;
}

  
  </style>