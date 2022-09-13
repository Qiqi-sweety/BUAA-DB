<template>
    
    <el-row class = "storeRegisterRow">
      <el-col :span="12" class = "storeRegisterFormCol">
         <storeRegisterLeft2 class = "storeRegisterLeft2"/>
      </el-col>


      <el-col :span="12" class = "storeRegisterImageFormCol">
        <storeRegisterRight2 class = "storeRegisterRight2"/>
      </el-col>


    </el-row>
  
</template>

<script>
import storeRegisterLeft2 from './storeRegisterLeft2.vue'
import storeRegisterRight2 from './storeRegisterRight2.vue'
export default {
  name: 'storeRegisterMain2',
  components: {
    storeRegisterLeft2,
    storeRegisterRight2,
  }
}
</script>



<style>
.storeRegisterRow {
  margin-right:0px;
  width:100%;
}


.storeRegisterLeft2 {
  margin:auto;
  
}

.storeRegisterImageFormClass {
  margin: auto;
}


</style>