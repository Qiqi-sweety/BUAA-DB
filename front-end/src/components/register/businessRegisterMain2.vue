<template>
    
    <el-row class = "businessRegisterRow">
      <el-col :span="12" class = "businessRegisterFormCol">
         <businessRegisterLeft2 class = "businessRegisterLeft2"/>
      </el-col>


      <el-col :span="12" class = "businessRegisterImageFormCol">
        <businessRegisterImageForm class = "businessRegisterImageFormClass"/>
      </el-col>


    </el-row>
  
</template>

<script>
import businessRegisterLeft2 from './businessRegisterLeft2.vue'
import businessRegisterImageForm from './businessRegisterImageForm.vue'
export default {
  name: 'businessRegisterMain1',
  components: {
      businessRegisterLeft2,
      businessRegisterImageForm,
  }
}
</script>



<style>
.businessRegisterRow {
  margin-right:0px;
  width:100%;
}


.businessRegisterLeft2 {
  margin:auto;
  
}

.businessRegisterImageFormClass {
  margin: auto;
}


</style>