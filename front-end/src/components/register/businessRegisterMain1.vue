<template>
    
      <el-row class = "businessRegisterRow">
        <el-col :span="12" class = "businessRegisterFormCol">
           <businessRegisterLeft1 class = "businessRegisterLeft1"/>
        </el-col>
  
  
        <el-col :span="12" class = "businessRegisterImageFormCol">
          <businessRegisterImageForm class = "businessRegisterImageFormClass"/>
        </el-col>
  
  
      </el-row>
    
  </template>
  
  <script>
  import businessRegisterLeft1 from './businessRegisterLeft1.vue'
  import businessRegisterImageForm from './businessRegisterImageForm.vue'
  export default {
    name: 'businessRegisterMain1',
    components: {
        businessRegisterLeft1,
        businessRegisterImageForm,
    }
  }
  </script>
  
  
  
  <style>
.businessRegisterRow {
    margin-right:0px;
    width:100%;
}


.businessRegisterLeft1 {
    margin:auto;
    
}

.businessRegisterImageFormClass {
    margin: auto;
}

  
  </style>