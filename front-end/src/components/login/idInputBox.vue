<template>
  <el-input
    v-model="input"
    type="id"
    placeholder="账号"
    size = "large"
    class = "idInputBox"
  >
    <template #prefix>
          <el-icon class="el-input__icon"><user /></el-icon>
    </template>

  </el-input>
  
</template>

<script lang="ts" setup>


</script>

<style>
  .idInputBox {
    /* size */
    
    width: 300px;
    
  }

</style>





